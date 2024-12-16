class BusinessObject:
    def __init__(self):
        self._id = None  # Basisklasse mit ID für alle BOs
        
    def get_id(self):
        return self._id
        
    def set_id(self, id):
        self._id = id