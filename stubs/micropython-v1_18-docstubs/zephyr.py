"""
functionality specific to Zephyr. See: https://docs.micropython.org/en/v1.18/library/zephyr.html

The ``zephyr`` module contains functions and classes specific to the Zephyr port.
"""

# + module: zephyr.rst
# source version: v1_18
# origin module:: micropython/docs/library/zephyr.rst
# + module: zephyr.DiskAccess.rst
# + module: zephyr.FlashArea.rst
from typing import Any, Optional


class DiskAccess:
    """
    Gets an object for accessing disk memory of the specific disk.
    For accessing an SD card on the mimxrt1050_evk, ``disk_name`` would be ``SDHC``. See board documentation and
    devicetree for usable disk names for your board (ex. RT boards use style USDHC#).
    """

    def __init__(self, disk_name) -> None:
        ...

    def readblocks(self, block_num, buf, offset: Optional[int]) -> Any:
        ...

    def writeblocks(self, block_num, buf, offset: Optional[int]) -> Any:
        ...

    def ioctl(self, cmd, arg) -> Any:
        """
        These methods implement the simple and extended
        :ref:`block protocol <block-device-interface>` defined by
        :class:`uos.AbstractBlockDev`.
        """
        ...


class FlashArea:
    """
    Gets an object for accessing flash memory at partition specified by ``id`` and with block size of ``block_size``.

    ``id`` values are integers correlating to fixed flash partitions defined in the devicetree.
    A commonly used partition is the designated flash storage area defined as ``FlashArea.STORAGE`` if
    ``FLASH_AREA_LABEL_EXISTS(storage)`` returns true at boot.
    Zephyr devicetree fixed flash partitions are ``boot_partition``, ``slot0_partition``, ``slot1_partition``, and
    ``scratch_partition``. Because MCUBoot is not enabled by default for MicroPython, these fixed partitions can be accessed by
    ID integer values 1, 2, 3, and 4, respectively.
    """

    def __init__(self, id, block_size) -> None:
        ...

    def readblocks(self, block_num, buf, offset: Optional[int]) -> Any:
        ...

    def writeblocks(self, block_num, buf, offset: Optional[int]) -> Any:
        ...

    def ioctl(self, cmd, arg) -> Any:
        """
        These methods implement the simple and extended
        :ref:`block protocol <block-device-interface>` defined by
        :class:`uos.AbstractBlockDev`.
        """
        ...


def is_preempt_thread() -> Any:
    """
    Returns true if the current thread is a preemptible thread.

    Zephyr preemptible threads are those with non-negative priority values (low priority levels), which therefore,
    can be supplanted as soon as a higher or equal priority thread becomes ready.
    """
    ...


def current_tid() -> Any:
    """
    Returns the thread id of the current thread, which is used to reference the thread.
    """
    ...


def thread_analyze() -> Any:
    """
    Runs the Zephyr debug thread analyzer on the current thread and prints stack size statistics in the format:

     "``thread_name``-20s: STACK: unused ``available_stack_space`` usage ``stack_space_used``
     / ``stack_size`` (``percent_stack_space_used`` %); CPU: ``cpu_utilization`` %"

     * *CPU utilization is only printed if runtime statistics are configured via the ``CONFIG_THREAD_RUNTIME_STATS`` kconfig*

    This function can only be accessed if ``CONFIG_THREAD_ANALYZER`` is configured for the port in ``zephyr/prj.conf``.
    For more infomation, see documentation for Zephyr `thread analyzer
    <https://docs.zephyrproject.org/latest/guides/debug_tools/thread-analyzer.html#thread-analyzer>`_.
    """
    ...


def shell_exec(cmd_in) -> Any:
    """
    Executes the given command on an UART backend. This function can only be accessed if ``CONFIG_SHELL_BACKEND_SERIAL``
    is configured for the port in ``zephyr/prj.conf``.

    A list of possible commands can be found in the documentation for Zephyr `shell commands <https://docs.zephyrproject.org/latest/reference/shell/index.html?highlight=shell_execute_cmd#commands>`_.
    """
    ...
