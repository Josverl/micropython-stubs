from abc import get_cache_token, update_abstractmethods, ABC, abstractmethod


class C(ABC):
    @abstractmethod
    def my_abstract_method(self, arg1): ...
    @classmethod
    @abstractmethod
    def my_abstract_classmethod(cls, arg2): ...
    @staticmethod
    @abstractmethod
    def my_abstract_staticmethod(arg3): ...

    @property
    @abstractmethod
    def my_abstract_property(self): ...
    @my_abstract_property.setter
    @abstractmethod
    def my_abstract_property(self, val): ...

    @abstractmethod
    def _get_x(self): ...
    @abstractmethod
    def _set_x(self, val): ...

    x = property(_get_x, _set_x)


token = get_cache_token()

cls = update_abstractmethods(C)
