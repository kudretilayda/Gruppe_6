from src.server.bo.BusinessObject import BusinessObject

# Die Klasse ClothingItem stellt ein Kleidungsstück dar und erbt von BusinessObject

class ClothingItem(BusinessObject):

    def __init__(self): 
        super().__init__() # Initialisiert die Basisklasse BusinessObject
        self._item_id = 0
        self._wardrobe_id = 0
        self.item_name = ""
        self.clothing_type = None
        self.selected = False

    def get_id(self): # Getter und Setter Methoden
        return self._item_id

    def set_id(self, item_id: int):
        self._item_id = item_id

    def get_clothing_type(self):
        return self.clothing_type

    def set_clothing_type(self, clothing_type):
        self.clothing_type = clothing_type

    def get_item_name(self):
        return self.item_name

    def set_item_name(self, item_name: str):
        self.item_name = item_name

    def set_wardrobe_id(self, wardrobe_id):
        self._wardrobe_id = wardrobe_id

    def is_selected(self):
        return self.selected

    def __str__(self): # String-Darstellung des Objekts für Debugging oder Logging
        return "Kleidungsstück ID: {}, Typ: {}, Name: {}".format(
            self.get_id(),
            self.get_clothing_type(),
            self.get_item_name(),
        )
