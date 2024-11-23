from abc import ABC, abstractmethod


class Constraint(ABC):
    @abstractmethod
    def auswerten(self, obj):    # Validierung des Contraints auf das Objekt
        pass
