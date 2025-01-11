# Importiere die Basisklasse Constraint aus dem angegebenen Pfad
from src.server.bo.Constraints.Constraint import Constraint

# Definiere die Klasse UnaryConstraint, die von der Basisklasse Constraint erbt
class UnaryConstraint(Constraint):

    # Initialisierungsmethode für die Klasse
    def __init__(self):
        # Rufe den Initialisierer der Elternklasse auf
        super().__init__()
        # Attribut zur Darstellung des Stils eines Outfits
        self.style = None

    
    # Überprüft, ob alle Kleidungsstücke im Outfit zum definierten Stil passen
    def validate(self, outfit):
        # Iteriere über alle Kleidungsstücke im Outfit
        for item in outfit.item:
            # Überprüfe, ob der Kleidungstyp des Items im Stil des Outfits enthalten ist
            if item.clothing_type in outfit.style.get_clothing_type():
                # Gibt True zurück, wenn der Kleidungstyp zum Stil passt
                return True
            else:
                # Gibt eine Fehlermeldung aus, wenn ein Kleidungstyp nicht zum Stil passt
                print(f'{item.item_name} entspricht nicht dem Style des Outfits')
                # Gibt False zurück, wenn die Validierung fehlschlägt
                return False
