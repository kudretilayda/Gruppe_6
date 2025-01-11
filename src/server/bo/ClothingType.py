from src.server.bo.BusinessObject import BusinessObject


class ClothingType(BusinessObject):
    def __init__(self):
        super().__init__()
        self._name = ""
        self._usage = ""

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    