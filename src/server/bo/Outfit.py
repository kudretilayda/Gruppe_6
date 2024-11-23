from src.server.bo.BusinessObject import BusinessObject


class Outfit (BusinessObject):

    def __init__(self):
        self.__outfit_id = 0
        self.__kleidungsstuecke = []  
        self.__style = None           

    def get_outfit_id(self):
        return self.__outfit_id

    def set_outfit_id(self, outfit_id: int):
        self.__outfit_id = outfit_id

    
    def get_kleidungsstuecke(self):
        return self.__kleidungsstuecke

    def set_kleidungsstuecke(self, kleidungsstuecke: list):
        self.__kleidungsstuecke = kleidungsstuecke

    
    def get_style(self):
        return self.__style

    def set_style(self, style):
        self.__style = style

    def __str__(self):
        
        return "Outfit: {}, {}, {}, {}".format(
            self.__outfit_id(), 
            self.__kleidungsstuecke(), 
            self.__style()
        )

    @staticmethod
    def from_dict(dictionary=dict(), style_instance=None):
        
        obj = Outfit()
        obj.set_outfit_id(dictionary.get("outfit_id", 0))
        obj.set_kleidungsstuecke(dictionary.get("kleidungsstuecke", []))
        obj.set_style(style_instance)
        return obj
