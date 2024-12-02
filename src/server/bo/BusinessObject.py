# src/server/bo/BusinessObject.py

class BusinessObject:
    """Basisklasse für alle BusinessObjects"""
    def __init__(self):
        self._id = None
        self._creation_date = None

    def get_id(self):
        """Auslesen der ID."""
        return self._id

    def set_id(self, value):
        """Setzen der ID."""
        self._id = value

    def get_creation_date(self):
        """Auslesen des Erstellungsdatums."""
        return self._creation_date

    def set_creation_date(self, value):
        """Setzen des Erstellungsdatums."""
        self._creation_date = value

    def to_dict(self):
        """Umwandeln des BusinessObject in ein Python dict()."""
        return {
            'id': self.get_id(),
            'creation_date': self.get_creation_date()
        }