from abc import ABCMeta, abstractmethod

class FileSystemComponent(metaclass = ABCMeta):

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def display(self) -> None:
        pass