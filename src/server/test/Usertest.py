import unittest
from src.server.bo.User import User


class TestUser(unittest.TestCase):
    def setUp(self):
        # Erstellen eines Beispiel-User-Objekts
        self.user = User()
        self.user.set_user_id(1)
        self.user.set_nachname("Mustermann")
        self.user.set_vorname("Max")
        self.user.set_nickname("maxm")
        self.user.set_google_id("google-1234")
        self.user.set_email("max.mustermann@example.com")

    def test_get_and_set_user_id(self):
        # Testet das Setzen und Abrufen der user_id
        self.user.set_user_id(2)
        self.assertEqual(self.user.get_user_id(), 2)

    def test_get_and_set_nachname(self):
        # Testet das Setzen und Abrufen des Nachnamens
        self.user.set_nachname("Musterfrau")
        self.assertEqual(self.user.get_nachname(), "Musterfrau")

    def test_get_and_set_vorname(self):
        # Testet das Setzen und Abrufen des Vornamens
        self.user.set_vorname("Erika")
        self.assertEqual(self.user.get_vorname(), "Erika")

    def test_get_and_set_nickname(self):
        # Testet das Setzen und Abrufen des Nicknames
        self.user.set_nickname("erikam")
        self.assertEqual(self.user.get_nickname(), "erikam")

    def test_get_and_set_google_id(self):
        # Testet das Setzen und Abrufen der Google-ID
        self.user.set_google_id("google-5678")
        self.assertEqual(self.user.get_google_id(), "google-5678")

    def test_get_and_set_email(self):
        # Testet das Setzen und Abrufen der Email-Adresse
        self.user.set_email("erika.musterfrau@example.com")
        self.assertEqual(self.user.get_email(), "erika.musterfrau@example.com")

    def test_to_string(self):
        # Testet die String-Repräsentation (__str__)
        expected_string = "User: 1, Mustermann, max.mustermann@example.com, Max"
        self.assertEqual(str(self.user), expected_string)

    def test_from_dict(self):
        # Testet das Erstellen eines User-Objekts aus einem Dictionary
        test_data = {
            "user_id": 3,
            "nachname": "Schmidt",
            "vorname": "Anna",
            "nickname": "annas",
            "google_id": "google-9876",
            "email": "anna.schmidt@example.com"
        }

        user_from_dict = User.from_dict(test_data)

        self.assertEqual(user_from_dict.get_user_id(), 3)
        self.assertEqual(user_from_dict.get_nachname(), "Schmidt")
        self.assertEqual(user_from_dict.get_vorname(), "Anna")
        self.assertEqual(user_from_dict.get_nickname(), "annas")
        self.assertEqual(user_from_dict.get_google_id(), "google-9876")
        self.assertEqual(user_from_dict.get_email(), "anna.schmidt@example.com")


if __name__ == "__main__":
    unittest.main()
