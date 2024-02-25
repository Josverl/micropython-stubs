from _typeshed import Incomplete
from senml.senml_base import SenmlBase as SenmlBase

class SenmlRecord(SenmlBase):
    """represents a single value in a senml pack object"""

    __parent: Incomplete
    _unit: Incomplete
    _value: Incomplete
    _time: Incomplete
    _sum: Incomplete
    _update_time: Incomplete
    name: Incomplete
    unit: Incomplete
    actuate: Incomplete
    def __init__(self, name, **kwargs) -> None:
        """
        create a new senml record
        :param kwargs:  optional parameters:
            - value: the value to store in the record
            - time: the timestamp to use (when was the value measured)
            - name: the name of hte record
            - unit: unit value
            - sum: sum value
            - update_time: max time before sensor will provide an updated reading
            - callback: a callback function taht will be called when actuator data has been found. Expects no params
        """
    def __enter__(self):
        """
        for supporting the 'with' statement
        :return: self
        """
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None:
        """
        when destroyed in a 'with' statement, make certain that the item is removed from the parent list.
        :return: None
        """
    def _check_value_type(self, value) -> None:
        """
        checks if the type of value is allowed for senml
        :return: None, raisee exception if not ok.
        """
    def _check_number_type(self, value, field_name) -> None:
        """
        checks if the type of value is allowed for senml
        :return: None, raisee exception if not ok.
        """
    @property
    def value(self):
        """get the value currently assigned to the object"""
    @value.setter
    def value(self, value) -> None:
        """set the current value. Will not automatically update the time stamp. This has to be done seperatly for more
        finegrained control
        Note: when the value is a float, you can control rounding in the rendered output by using the function
        round() while assigning the value. ex: record.value = round(12.2 / 1.5423, 2)
        """
    @property
    def time(self): ...
    @time.setter
    def time(self, value) -> None: ...
    @property
    def update_time(self): ...
    @update_time.setter
    def update_time(self, value) -> None: ...
    @property
    def sum(self): ...
    @sum.setter
    def sum(self, value) -> None: ...
    @property
    def _parent(self):
        """
        the parent pack object for this record. This is a property so that inheriters can override and do custom
        actions when the parent is set (like passing it on to their children
        :return:
        """
    @_parent.setter
    def _parent(self, value) -> None:
        """
        the parent pack object for this record. This is a property so that inheriters can override and do custom
        actions when the parent is set (like passing it on to their children
        :return:
        """
    def _build_rec_dict(self, naming_map, appendTo) -> None:
        """
        converts the object to a dictionary that can be rendered to senml.
        :param naming_map: a dictionary that maps the field names to senml json or senml cbor. keys are in the
        form 'n', 'v',...  values for 'n' are either 'n' or 0 (number is for cbor)
        :return: a senml dictionary representation of the record
        """
    def _from_raw(self, raw, naming_map) -> None:
        """
        extracts te data from the raw record. Used during parsing of incoming data.
        :param raw: a raw senml record which still contains the original field names
        :param naming_map: used to map cbor names to json field names
        :return:
        """
    def do_actuate(self, raw, naming_map) -> None:
        """
        called when a raw senml record was found for this object. Stores the data and if there is a callback, calls it.
        :param raw: raw senml object
        :return: None
        """
