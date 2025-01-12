from src.server.bo.Constraints.Constraint import Constraint

# Mutex verhindert, dass bestimmte Kleidundsstücke zusammen getragen werden

class MutexConstraint(Constraint): # Definiert Ausschlussregeln zwischen Kleidungsstücken
    def __init__(self, mutex):
        super().__init__()
        self.mutex = mutex

    def validate(self, outfit): # Die Methode prüft, ob im Outfit Kleidungsstücke kombiniert sind, die laut Regel nicht zusammen getragen werden dürfen
        for pair in self.mutex: # Die Methode durchläuft alle Paare in der Mutex-Liste
            item_1, item_2 = pair # Jedes Paar besteht aus zwei Kleidungsstücken 
            if item_1 in outfit.get_items() and item_2 in outfit.get_items(): # Prüfen, ob beide Kleidungsstücke im Outfit enthalten sind
                print(f"Regel verletzt: {item_1.item_name} und {item_2.item_name} können nicht gleichzeitig im Outfit sein.") # Wenn beide Kleidungsstücke im Outfit enthalten sind, wurde die Regel verletzt
                return False
            else: # Wenn keine Regel verletzt wurde, ist das Outfit gültig
                print("Outfit erfüllt die Mutex-Bedingungen.")
                return True
