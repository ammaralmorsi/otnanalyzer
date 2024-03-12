from abc import ABC, abstractmethod


class FieldGenerator(ABC):
    @abstractmethod
    def get_next_value(self):
        pass
