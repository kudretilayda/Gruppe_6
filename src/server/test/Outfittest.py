import unittest
import sys
import os

# Add path to main directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from src.server.bo.Outfit import Outfit
# Dummy class for Style
class Style:
   def __init__(self, name):
       self.name = name
   
   def __call__(self):
       return self.name

class TestOutfit(unittest.TestCase):
   def setUp(self):
       # Create dummy Style object
       self.style = Style("Casual")
       
       # Create Outfit object  
       self.outfit = Outfit()
       self.outfit.set_outfit_id(1)
       self.outfit.set_clothing_items(["Shirt", "Jeans", "Sneakers"])
       self.outfit.set_style(self.style)
   
   def test_get_and_set_outfit_id(self):
       # Check if outfit ID is set and returned correctly
       self.outfit.set_outfit_id(2)
       self.assertEqual(self.outfit.get_outfit_id(), 2)
   
   def test_get_and_set_clothing_items(self):
       # Check if clothing items are set and returned correctly
       clothing_items = ["T-Shirt", "Shorts"]
       self.outfit.set_clothing_items(clothing_items)
       self.assertEqual(self.outfit.get_clothing_items(), clothing_items)
   
   def test_get_and_set_style(self):
       # Check if style is set and returned correctly
       new_style = Style("Formal")
       self.outfit.set_style(new_style)
       self.assertEqual(self.outfit.get_style(), new_style)
   
   def test_to_string(self):
       # Check if string representation is correct
       expected_string = "Outfit: 1, ['Shirt', 'Jeans', 'Sneakers'], Casual"
       self.assertEqual(str(self.outfit), expected_string)
   
   def test_from_dict(self):
       # Test data for dictionary
       test_data = {
           "outfit_id": 3,
           "clothing_items": ["Blazer", "Chinos", "Loafers"]
       }
       
       # Create instance using from_dict method
       outfit_from_dict = Outfit.from_dict(test_data, style_instance=self.style)
       
       self.assertEqual(outfit_from_dict.get_outfit_id(), 3)
       self.assertEqual(outfit_from_dict.get_clothing_items(), ["Blazer", "Chinos", "Loafers"])
       self.assertEqual(outfit_from_dict.get_style(), self.style)

if __name__ == "__main__":
   unittest.main()