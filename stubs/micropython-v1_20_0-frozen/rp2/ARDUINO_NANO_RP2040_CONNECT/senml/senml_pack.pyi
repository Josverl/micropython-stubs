from _typeshed import Incomplete
from senml.senml_base import SenmlBase as SenmlBase
from senml.senml_record import SenmlRecord as SenmlRecord

class SenmlPackIterator:
    """an iterator to walk over all records in a pack"""

    _list: Incomplete
    _index: int
    def __init__(self, list) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...

class SenmlPack(SenmlBase):
    """
    represents a sneml pack object. This can contain multiple records but also other (child) pack objects.
    When the pack object only contains records, it represents the data of a device.
    If the pack object has child pack objects, then it represents a gateway
    """

    json_mappings: Incomplete
    _data: Incomplete
    name: Incomplete
    _base_value: Incomplete
    _base_time: Incomplete
    _base_sum: Incomplete
    base_unit: Incomplete
    _parent: Incomplete
    actuate: Incomplete
    def __init__(self, name, callback: Incomplete | None = ...) -> None:
        """
        initialize the object
        :param name: {string} the name of the pack
        """
    def __iter__(self): ...
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
    @property
    def base_value(self):
        """
        the base value of the pack.
        :return: a number
        """
    @base_value.setter
    def base_value(self, value) -> None:
        """
        set the base value.
        :param value: only number allowed
        :return:
        """
    @property
    def base_sum(self):
        """
        the base sum of the pack.
        :return: a number
        """
    @base_sum.setter
    def base_sum(self, value) -> None:
        """
        set the base value.
        :param value: only number allowed
        :return:
        """
    @property
    def base_time(self): ...
    @base_time.setter
    def base_time(self, value) -> None: ...
    def _check_value_type(self, value, field_name) -> None:
        """
        checks if the type of value is allowed for senml
        :return: None, raisee exception if not ok.
        """
    def from_json(self, data) -> None:
        """
        parse a json string and convert it to a senml pack structure
        :param data: a string containing json data.
        :return: None, will r
        """
    def _process_incomming_data(self, records, naming_map) -> None:
        """
        generic processor for incomming data (actuators.
        :param records: the list of raw senml data, parsed from a json or cbor structure
        :param naming_map: translates cbor to json field names (when needed).
        :return: None
        """
    def do_actuate(self, raw, naming_map, device: Incomplete | None = ...) -> None:
        """
        called while parsing incoming data for a record that is not yet part of this pack object.
        adds a new record and raises the actuate callback of the pack with the newly created record as argument
        :param naming_map:
        :param device: optional: if the device was not found
        :param raw: the raw record definition, as found in the json structure. this still has invalid labels.
        :return: None
        """
    def to_json(self):
        """
        render the content of this object to a string.
        :return: a string representing the senml pack object
        """
    def _build_rec_dict(self, naming_map, appendTo) -> None:
        """
        converts the object to a senml object with the proper naming in place.
        This can be recursive: a pack can contain other packs.
        :param naming_map: a dictionary used to pick the correct field names for either senml json or senml cbor
        :return:
        """
    def from_cbor(self, data) -> None:
        """
        parse a cbor data byte array to a senml pack structure.
        :param data: a byte array.
        :return: None
        """
    def to_cbor(self):
        """
        render the content of this object to a cbor byte array
        :return: a byte array
        """
    def add(self, item) -> None:
        """
        adds the item to the list of records
        :param item: {SenmlRecord} the item that needs to be added to the pack
        :return: None
        """
    def remove(self, item) -> None:
        """
        removes the item from the list of records
        :param item: {SenmlRecord} the item that needs to be removed
        :return: None
        """
    def clear(self) -> None:
        """
        clear the list of the pack
        :return: None
        """
