from src.server.bo.BusinessObject import BusinessObject

class Outfit(BusinessObject):
    def __init__(self):
        super().__init__()
        # self._outfit_id = self.get_id() # outfit_id wird nicht mehr benötigt, da die Superklasse eine id für Outfit erstellt
        self._outfit_name = ""
        self._item = []         # hier müssen wir uns überlegen ob ._item oder .item
        self._style = None      # hier auch: ._style oder.style. Je nachdem wie der Code läuft

#   def get_outfit_id(self):
#       return self._outfit_id

#   def set_outfit_id(self, outfit_id):
#       self._outfit_id = outfit_id

    def get_outfit_name(self):
        return self._outfit_name

    def set_outfit_name(self, outfit_name):
        self._outfit_name = outfit_name

    def get_item(self):
        return self._item

    def set_item(self, item):
        self._item.append(item)     # append, weil item eine Liste mit Items sein soll, aber es wurde item getauft

    def get_style(self):
        return self._style

    def set_style(self, style):
        self._style = style

    def __str__(self):
        return f"Outfit: {self._id}, {self._outfit_name}, {self._item}, {self._style}"

    @staticmethod
    def from_dict(dictionary=None, style_instance=None):
        if dictionary is None:
            dictionary = dict()

        obj = Outfit()
        obj.set_id(dictionary.get("id", 0))
        obj.set_outfit_name(dictionary.get("outfit_name", ""))

        # Wenn "item" eine Liste ist, fügen wir sie direkt hinzu
        items = dictionary.get("item", [])
        if isinstance(items, list):
            for item in items:
                obj.set_item(item)
        else:
            obj.set_item(items)  # Falls nur ein einzelnes Item angegeben ist

        # Setzt den Stil
        if style_instance is not None:
            obj.set_style(style_instance)
        else:
            obj.set_style(dictionary.get("style", None))

        return obj