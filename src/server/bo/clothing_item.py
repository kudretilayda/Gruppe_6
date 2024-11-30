from .business_object import BusinessObject

class ClothingItem(BusinessObject):
    def __init__(self):
        super().__init__()
        self._type = None  # Reference to ClothingType
        
    def get_type(self):
        return self._type
        
    def set_type(self, type):
        self._type = type