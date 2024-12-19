from abc import ABC, abstractmethod


class Constraint(ABC):
    def __init__(self):
        self._constraint_id = int

    @abstractmethod
    def validate(self, *args, **kwargs):
        pass
