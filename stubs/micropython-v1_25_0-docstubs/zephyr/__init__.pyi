"""
Functionality specific to Zephyr.

MicroPython module: https://docs.micropython.org/en/v1.25.0/library/zephyr.html

The ``zephyr`` module contains functions and classes specific to the Zephyr port.
"""

# source version: v1.25.0
# origin module:: repos/micropython/docs/library/zephyr.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing_extensions import TypeVar, TypeAlias, Awaitable
from zephyr.DiskAccess import DiskAccess
from zephyr.FlashArea import FlashArea

def is_preempt_thread() -> Incomplete:
    """
    Returns true if the current thread is a preemptible thread.

    Zephyr preemptible threads are those with non-negative priority values (low priority levels), which therefore,
    can be supplanted as soon as a higher or equal priority thread becomes ready.
    """
    ...

def current_tid() -> Incomplete:
    """
    Returns the thread id of the current thread, which is used to reference the thread.
    """
    ...

def thread_analyze() -> Incomplete:
    """
    Runs the Zephyr debug thread analyzer on the current thread and prints stack size statistics in the format:

     "``thread_name``-20s: STACK: unused ``available_stack_space`` usage ``stack_space_used``
     / ``stack_size`` (``percent_stack_space_used`` %); CPU: ``cpu_utilization`` %"

     * *CPU utilization is only printed if runtime statistics are configured via the ``CONFIG_THREAD_RUNTIME_STATS`` kconfig*

    This function can only be accessed if ``CONFIG_THREAD_ANALYZER`` is configured for the port in ``zephyr/prj.conf``.
    For more information, see documentation for Zephyr `thread analyzer
    <https://docs.zephyrproject.org/latest/guides/debug_tools/thread-analyzer.html#thread-analyzer>`_.
    """
    ...

def shell_exec(cmd_in) -> Incomplete:
    """
    Executes the given command on an UART backend. This function can only be accessed if ``CONFIG_SHELL_BACKEND_SERIAL``
    is configured for the port in ``zephyr/prj.conf``.

    A list of possible commands can be found in the documentation for Zephyr `shell commands <https://docs.zephyrproject.org/latest/reference/shell/index.html?highlight=shell_execute_cmd#commands>`_.
    """
    ...
