# test/ClothingItemTest.py
import unittest
from server.bo.ClothingItems import ClothingItem
from server.bo.ClothingType import ClothingType

class ClothingItemTest(unittest.TestCase):
    def setUp(self):
        self.item = ClothingItem()
        self.item.set_product_name("Blue Jeans")
        self.item.set_wardrobe_id("wardrobe1")
        self.item.set_clothing_type_id("type1")
        self.item.set_color("blue")
        self.item.set_brand("Levis")
        self.item.set_season("Summer")

    def test_clothing_item_basics(self):
        self.assertEqual(self.item.get_product_name(), "Blue Jeans")
        self.assertEqual(self.item.get_wardrobe_id(), "wardrobe1")
        self.assertEqual(self.item.get_color(), "blue")
        self.assertEqual(self.item.get_brand(), "Levis")
        self.assertEqual(self.item.get_season(), "Summer")

class ClothingItemMapperTest(unittest.TestCase):
    def setUp(self):
        self.mapper = ClothingItemMapperTest()
        self.test_item = ClothingItem()
        self.test_item.set_product_name("Test Item")

    def test_insert(self):
        saved_item = self.mapper.insert(self.test_item)
        self.assertIsNotNone(saved_item.get_id())