from abc import ABC
from datetime import datetime
import uuid

class BusinessObject(ABC):
    """Basisklasse für alle Business Objects

    Jedes Business Object verfügt über einen eindeutigen Identifier sowie ein 
    Erstellungsdatum.
    """

    def __init__(self):
        self._id = str(uuid.uuid4())  # Generiert eine UUID als ID
        self._create_time = datetime.now()

    def get_id(self):
        """Auslesen der ID."""
        return self._id

    def set_id(self, value):
        """Setzen der ID."""
        self._id = value

    def get_create_time(self):
        """Auslesen des Erstellungsdatums."""
        return self._create_time

    def set_create_time(self, date):
        """Setzen des Erstellungsdatums."""
        self._create_time = date