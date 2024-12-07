import unittest
from server.bo.Wardrobe import Wardrobe

class WardrobeTest(unittest.TestCase):
    def setUp(self):
        self.wardrobe = Wardrobe()
        self.wardrobe.set_owner_name("Test User")
        self.wardrobe.set_person_id("user1")

    def test_wardrobe_basics(self):
        self.assertEqual(self.wardrobe.get_owner_name(), "Test User")
        self.assertEqual(self.wardrobe.get_person_id(), "user1")

class WardrobeMapperTest(unittest.TestCase):
    def setUp(self):
        self.mapper = WardrobeMapperTest()
        self.test_wardrobe = Wardrobe()
        self.test_wardrobe.set_owner_name("Test Wardrobe")
        self.test_wardrobe.set_person_id("test_user")

    def test_insert(self):
        saved_wardrobe = self.mapper.insert(self.test_wardrobe)
        self.assertIsNotNone(saved_wardrobe.get_id())