from abc import ABC

# Es gibt eine Möglichkeit, automatisch Primary Keys zu generieren, sobald eine Instanz von BO erstellt wird.

class BusinessObject(ABC):

    def __init__(self):
        self._id = 0

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value
