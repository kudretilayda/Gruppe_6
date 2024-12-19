from abc import ABC, abstractmethod


class Constraint(ABC):
    def __init__(self):
        self._constraint_id = int

    def get_id(self):
        return self._constraint_id

    def set_id(self, constraint_id):
        self._constraint_id = constraint_id

    @abstractmethod
    def validate(self, *args, **kwargs):
        pass
