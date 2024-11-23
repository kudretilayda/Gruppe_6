import BusinessObject


class Kleiderschrank(BusinessObject):
    def __init__(self):
        super().__init__()
        # Eigentümer ID
        self._inhalt = list
        self._outfits = list

    # def get_eigentümer
    # def set_eigentümer

    def get_inhalt(self):           # Liste der Kleidungsstücke ausgeben
        return self._inhalt

    def set_inhalt(self, value):    # Kleidungsstücke der Liste hinzufügen
        self._inhalt = value

    def get_outfits(self):          # Liste der Outfits ausgeben
        return self._outfits

    def set_outfits(self, value):   # Eventuell nicht nötig, weil es bei Outfits hinzugefügt werden kann
        self._outfits = value

