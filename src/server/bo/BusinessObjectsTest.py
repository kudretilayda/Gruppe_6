import unittest
from server.bo.Style import Style

class StyleTest(unittest.TestCase):
    def setUp(self):
        self.style = Style()
        self.style.set_style_name("Casual")
        self.style.set_created_by("user1")

    def test_style_basics(self):
        self.assertEqual(self.style.get_style_name(), "Casual")
        self.assertEqual(self.style.get_created_by(), "user1")