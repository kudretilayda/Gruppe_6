import unittest
from server.bo.Outfit import Outfit

class OutfitTest(unittest.TestCase):
    def setUp(self):
        self.outfit = Outfit()
        self.outfit.set_outfit_name("Summer Office")
        self.outfit.set_style_id("style1")
        self.outfit.set_created_by("user1")
        self.outfit.set_items(["item1", "item2"])

    def test_outfit_basics(self):
        self.assertEqual(self.outfit.get_outfit_name(), "Summer Office")
        self.assertEqual(self.outfit.get_style_id(), "style1")
        self.assertEqual(self.outfit.get_created_by(), "user1")
        self.assertEqual(len(self.outfit.get_items()), 2)

class OutfitMapperTest(unittest.TestCase):
    def setUp(self):
        self.mapper = OutfitMapperTest()
        self.test_outfit = Outfit()
        self.test_outfit.set_outfit_name("Test Outfit")
        self.test_outfit.set_created_by("test_user")

    def test_insert(self):
        saved_outfit = self.mapper.insert(self.test_outfit)
        self.assertIsNotNone(saved_outfit.get_id())

    def test_find_by_person(self):
        saved_outfit = self.mapper.insert(self.test_outfit)
        found_outfits = self.mapper.find_by_person("test_user")
        self.assertTrue(len(found_outfits) > 0)