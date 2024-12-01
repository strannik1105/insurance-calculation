from typing import Generic, TypeVar

T = TypeVar("T")


class Singleton(Generic[T]):
    _instance: T
    _instance = None

    @classmethod
    def get_instance(cls) -> T:
        if cls._instance is None:
            cls._instance = cls()

        return cls._instance
