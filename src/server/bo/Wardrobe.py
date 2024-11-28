class Wardrobe(BusinessObject):
    def __init__(self):
        super().__init__()
        self._person_id = ""
        self._name = ""

    def get_person_id(self):
        return self._person_id

    def set_person_id(self, value):
        self._person_id = value

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = Wardrobe()
        obj.set_id(dictionary.get('id'))
        obj.set_person_id(dictionary.get('person_id'))
        obj.set_name(dictionary.get('name'))
        return obj
