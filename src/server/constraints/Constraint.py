from abc import ABC, abstractmethod


class Constraint(ABC):
    @abstractmethod
    def auswerten(self, obj):    # Validierung des Constraints auf das Objekt
        pass
