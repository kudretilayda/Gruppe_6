class BusinessObject:
    def __init__(self):
        self._id = 0

    def get_id(self):
        return self._id
        
    def set_id(self, id):
        self._id = id