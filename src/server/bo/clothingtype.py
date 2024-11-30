from .business_object import BusinessObject

class ClothingType(BusinessObject):
    def __init__(self):
        super().__init__()
        self._name = ""
        self._usage = ""
        
    def get_name(self):
        return self._name
        
    def set_name(self, name):
        self._name = name
        
    def get_usage(self):
        return self._usage
        
    def set_usage(self, usage):
        self._usage = usage