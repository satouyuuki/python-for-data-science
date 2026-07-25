from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        pass
    # def __new__(cls, *_, **__):
    #     try:
    #         if cls.__abstractmethods__:
    #             raise TypeError
    #             # print("TypeError")
    #             # sys.exit(1)
    #     except TypeError as e:
    #         print(f"{type(e).__name__}: {e}")
    #     return super().__new__(cls)

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False
