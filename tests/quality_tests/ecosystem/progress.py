"""Progress reporting for interactive ecosystem QA runs."""

from __future__ import annotations

from types import TracebackType
from typing import Protocol

from rich.console import Console, Group
from rich.live import Live
from rich.progress import BarColumn, MofNCompleteColumn, Progress, SpinnerColumn, TaskID, TextColumn, TimeElapsedColumn
from rich.table import Column
from typing_extensions import Self


class ProgressReporter(Protocol):
    def __enter__(self) -> Self: ...

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None: ...

    def start_catalog(self, catalog: str) -> None: ...

    def set_catalog_total(self, total: int) -> None: ...

    def advance_catalog(self, item: str) -> None: ...

    def finish_catalog(self) -> None: ...

    def start_testing(self, total: int) -> None: ...

    def start_package(self, package: str) -> None: ...

    def finish_package(self, package: str) -> None: ...

    def finish_testing(self) -> None: ...


class NullProgressReporter:
    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        return None

    def start_catalog(self, catalog: str) -> None:
        return None

    def set_catalog_total(self, total: int) -> None:
        return None

    def advance_catalog(self, item: str) -> None:
        return None

    def finish_catalog(self) -> None:
        return None

    def start_testing(self, total: int) -> None:
        return None

    def start_package(self, package: str) -> None:
        return None

    def finish_package(self, package: str) -> None:
        return None

    def finish_testing(self) -> None:
        return None


class RichProgressReporter:
    def __init__(self, *, console: Console | None = None, enabled: bool | None = None) -> None:
        self.console = console or Console(stderr=True)
        self.enabled = self.console.is_terminal if enabled is None else enabled
        self._overall = Progress(
            SpinnerColumn(),
            TextColumn("{task.description}", table_column=Column(ratio=1, no_wrap=True, overflow="ellipsis")),
            BarColumn(bar_width=20),
            MofNCompleteColumn(),
            TimeElapsedColumn(),
            console=self.console,
            auto_refresh=False,
            expand=True,
        )
        self._details = Progress(
            TextColumn("  "),
            SpinnerColumn(),
            TextColumn("{task.description}", table_column=Column(ratio=1, no_wrap=True, overflow="ellipsis")),
            BarColumn(bar_width=16),
            MofNCompleteColumn(),
            TimeElapsedColumn(),
            console=self.console,
            auto_refresh=False,
            expand=True,
        )
        self._live = Live(Group(self._overall, self._details), console=self.console, refresh_per_second=10)
        self._started = False
        self._overall_task: TaskID | None = None
        self._catalog_task: TaskID | None = None
        self._testing_task: TaskID | None = None
        self._catalog = ""

    def __enter__(self) -> Self:
        if self.enabled:
            self._live.start(refresh=True)
            self._started = True
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        if self._started:
            self._live.stop()
            self._started = False

    def start_catalog(self, catalog: str) -> None:
        self._catalog = catalog
        self._ensure_overall(2)
        self._catalog_task = self._details.add_task(f"Fetching {catalog} catalog", total=None)
        self._refresh()

    def set_catalog_total(self, total: int) -> None:
        if self._catalog_task is not None:
            task = self._details.tasks[self._catalog_task]
            self._details.update(self._catalog_task, total=total, completed=min(task.completed, total))
            self._refresh()

    def advance_catalog(self, item: str) -> None:
        if self._catalog_task is not None:
            self._details.update(self._catalog_task, advance=1, description=f"Fetching {self._catalog} catalog: {item}")
            self._refresh()

    def finish_catalog(self) -> None:
        if self._catalog_task is not None:
            task = self._details.tasks[self._catalog_task]
            if task.total is not None:
                self._details.update(self._catalog_task, completed=task.total)
        self._advance_overall()
        self._refresh()

    def start_testing(self, total: int) -> None:
        self._ensure_overall(1)
        self._testing_task = self._details.add_task("Testing packages", total=total)
        self._refresh()

    def start_package(self, package: str) -> None:
        if self._testing_task is not None:
            self._details.update(self._testing_task, description=f"Testing packages: {package}")
            self._refresh()

    def finish_package(self, package: str) -> None:
        if self._testing_task is not None:
            self._details.update(self._testing_task, advance=1, description=f"Testing packages: {package}")
            self._refresh()

    def finish_testing(self) -> None:
        if self._testing_task is not None:
            task = self._details.tasks[self._testing_task]
            if task.total is not None:
                self._details.update(self._testing_task, completed=task.total)
        self._advance_overall()
        self._refresh()

    def _ensure_overall(self, total: int) -> None:
        if self._overall_task is None:
            self._overall_task = self._overall.add_task("Ecosystem QA", total=total)

    def _advance_overall(self) -> None:
        if self._overall_task is not None:
            self._overall.update(self._overall_task, advance=1)

    def _refresh(self) -> None:
        if self._started:
            self._live.refresh()
