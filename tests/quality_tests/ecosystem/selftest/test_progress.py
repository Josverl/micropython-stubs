from io import StringIO

from rich.console import Console

from ..progress import RichProgressReporter


def test_rich_progress_renders_nested_catalog_and_testing_feedback():
    output = StringIO()
    console = Console(file=output, force_terminal=True, color_system=None, width=72)
    reporter = RichProgressReporter(console=console, enabled=True)

    with reporter:
        reporter.start_catalog("mim")
        reporter.set_catalog_total(3)
        reporter.advance_catalog("MIM sitemap")
        reporter.advance_catalog("package-a")
        reporter.advance_catalog("package-b")
        reporter.finish_catalog()
        reporter.start_testing(2)
        reporter.start_package("package-a")
        reporter.finish_package("package-a")
        reporter.start_package("package-b")
        reporter.finish_package("package-b")
        reporter.finish_testing()

    rendered = output.getvalue()
    assert "Ecosystem QA" in rendered
    assert "Fetching mim catalog" in rendered
    assert "Testing packages" in rendered
    assert "3/3" in rendered
    assert "2/2" in rendered


def test_rich_progress_is_silent_for_non_interactive_output():
    output = StringIO()
    console = Console(file=output, force_terminal=False, color_system=None)
    reporter = RichProgressReporter(console=console)

    with reporter:
        reporter.start_testing(1)
        reporter.start_package("package-a")
        reporter.finish_package("package-a")
        reporter.finish_testing()

    assert reporter.enabled is False
    assert output.getvalue() == ""
