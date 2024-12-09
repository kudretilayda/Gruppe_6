import unittest
from src.server.bo.Style import Style


class TestStyle(unittest.TestCase):
    def setUp(self):
        # Beispielwerte für ein Style-Objekt
        self.style = Style()
        self.style.set_style_id(1)
        self.style.set_features("Casual Style with minimalistic elements")
        self.style.set_constraints(["No bright colors", "No formal shoes"])
        self.style.set_kleidungstypen(["Shirt", "Jeans", "Sneakers"])

    def test_get_and_set_style_id(self):
        # Testet das Setzen und Abrufen der style_id
        self.style.set_style_id(2)
        self.assertEqual(self.style.get_style_id(), 2)

    def test_get_and_set_features(self):
        # Testet das Setzen und Abrufen von features
        features = "Formal Style with elegant elements"
        self.style.set_features(features)
        self.assertEqual(self.style.get_features(), features)

    def test_get_and_set_constraints(self):
        # Testet das Setzen und Abrufen von constraints
        constraints = ["Only monochrome colors", "No sneakers"]
        self.style.set_constraints(constraints)
        self.assertEqual(self.style.get_constraints(), constraints)

    def test_get_and_set_kleidungstypen(self):
        # Testet das Setzen und Abrufen von kleidungstypen
        kleidungstypen = ["Blazer", "Chinos", "Loafers"]
        self.style.set_kleidungstypen(kleidungstypen)
        self.assertEqual(self.style.get_kleidungstypen(), kleidungstypen)

    def test_to_string(self):
        # Testet die String-Repräsentation (__str__)
        expected_string = (
            "Style: 1, Casual Style with minimalistic elements, "
            "['No bright colors', 'No formal shoes'], ['Shirt', 'Jeans', 'Sneakers']"
        )
        self.assertEqual(str(self.style), expected_string)

    def test_from_dict(self):
        # Testet das Erstellen eines Style-Objekts aus einem Dictionary
        test_data = {
            "style_id": 3,
            "features": "Sporty Style with breathable fabrics",
            "constraints": ["Only lightweight materials", "No denim"],
            "kleidungstypen": ["T-Shirt", "Shorts", "Running Shoes"]
        }

        style_from_dict = Style.from_dict(test_data)

        self.assertEqual(style_from_dict.get_style_id(), 3)
        self.assertEqual(style_from_dict.get_features(), "Sporty Style with breathable fabrics")
        self.assertEqual(style_from_dict.get_constraints(), ["Only lightweight materials", "No denim"])
        self.assertEqual(style_from_dict.get_kleidungstypen(), ["T-Shirt", "Shorts", "Running Shoes"])


if __name__ == "__main__":
    unittest.main()
