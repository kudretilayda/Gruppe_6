import unittest
import sys
import os

# Pfad zum Hauptverzeichnis hinzufügen
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from src.server.bo.Outfit import Outfit

# Dummy-Klasse für Style
class Style:
    def __init__(self, name):
        self.name = name
    
    def __call__(self):
        return self.name

class TestOutfit(unittest.TestCase):
    def setUp(self):
        # Dummy-Style-Objekt erstellen
        self.style = Style("Casual")
        
        # Outfit-Objekt erstellen
        self.outfit = Outfit()
        self.outfit.set_outfit_id(1)
        self.outfit.set_kleidungsstuecke(["Shirt", "Jeans", "Sneakers"])
        self.outfit.set_style(self.style)
    
    def test_get_and_set_outfit_id(self):
        # Überprüfen, ob das Outfit-ID korrekt gesetzt und zurückgegeben wird
        self.outfit.set_outfit_id(2)
        self.assertEqual(self.outfit.get_outfit_id(), 2)
    
    def test_get_and_set_kleidungsstuecke(self):
        # Überprüfen, ob Kleidungsstücke korrekt gesetzt und zurückgegeben werden
        kleidungsstuecke = ["T-Shirt", "Shorts"]
        self.outfit.set_kleidungsstuecke(kleidungsstuecke)
        self.assertEqual(self.outfit.get_kleidungsstuecke(), kleidungsstuecke)
    
    def test_get_and_set_style(self):
        # Überprüfen, ob der Style korrekt gesetzt und zurückgegeben wird
        new_style = Style("Formal")
        self.outfit.set_style(new_style)
        self.assertEqual(self.outfit.get_style(), new_style)
    
    def test_to_string(self):
        # Überprüfen, ob die String-Repräsentation korrekt ist
        expected_string = "Outfit: 1, ['Shirt', 'Jeans', 'Sneakers'], Casual"
        self.assertEqual(str(self.outfit), expected_string)
    
    def test_from_dict(self):
        # Testdaten für das Dictionary
        test_data = {
            "outfit_id": 3,
            "kleidungsstuecke": ["Blazer", "Chinos", "Loafers"]
        }
        
        # Instanz über die from_dict-Methode erstellen
        outfit_from_dict = Outfit.from_dict(test_data, style_instance=self.style)
        
        self.assertEqual(outfit_from_dict.get_outfit_id(), 3)
        self.assertEqual(outfit_from_dict.get_kleidungsstuecke(), ["Blazer", "Chinos", "Loafers"])
        self.assertEqual(outfit_from_dict.get_style(), self.style)

if __name__ == "__main__":
    unittest.main()