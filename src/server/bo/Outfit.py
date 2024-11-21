from server.bo import BusinessObject as bo


class Outfit(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self.__outfit_id = 0
        self.__kleidungsstuecke = []  # Liste von Kleidungsstücken
        self.__style = None           # Style-Objekt oder None

    # Properties
    @property
    def outfit_id(self):
        return self.__outfit_id

    @outfit_id.setter
    def outfit_id(self, outfit_id: int):
        self.__outfit_id = outfit_id

    @property
    def kleidungsstuecke(self):
        return self.__kleidungsstuecke

    @kleidungsstuecke.setter
    def kleidungsstuecke(self, kleidungsstuecke: list):
        self.__kleidungsstuecke = kleidungsstuecke

    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style):
        self.__style = style

    # String-Repräsentation
    def __str__(self):
        return f"Outfit: {self.__outfit_id}, {self.__kleidungsstuecke}, {self.__style}"

    # Statische Methode zum Erstellen eines Objekts aus einem Dictionary
    @staticmethod
    def from_dict(dictionary=dict(), style_instance=None):
        obj = Outfit()
        obj.outfit_id = dictionary.get("outfit_id", 0)
        obj.kleidungsstuecke = dictionary.get("kleidungsstuecke", [])
        obj.style = style_instance
        return obj
