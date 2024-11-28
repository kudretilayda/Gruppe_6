from .bo.User import User
from .bo.Clothing import Clothing
from .bo.Outfit import Outfit
from .bo.Category import Category

from .db.UserMapper import UserMapper
from .db.ClothingMapper import ClothingMapper
from .db.OutfitMapper import OutfitMapper
from .db.CategoryMapper import CategoryMapper


class WardrobeAdministration(object):
    """Diese Klasse aggregiert die Applikationslogik für einen digitalen Kleiderschrank.
    
    Sie verwaltet Kleidungsstücke, Outfits, Kategorien und Benutzer und stellt 
    sicher, dass alle Operationen konsistent durchgeführt werden.
    """
    def __init__(self):
        pass

    """
    User-spezifische Methoden
    """
    def create_user(self, name, email, google_user_id):
        """Einen Benutzer anlegen"""
        user = User()
        user.set_name(name)
        user.set_email(email)
        user.set_user_id(google_user_id)
        user.set_id(1)

        with UserMapper() as mapper:
            return mapper.insert(user)

    def get_user_by_name(self, name):
        """Benutzer mit Namen name auslesen."""
        with UserMapper() as mapper:
            return mapper.find_by_name(name)

    def get_user_by_id(self, number):
        """Den Benutzer mit der ID auslesen."""
        with UserMapper() as mapper:
            return mapper.find_by_key(number)

    def get_user_by_email(self, email):
        """Benutzer mit E-Mail-Adresse auslesen."""
        with UserMapper() as mapper:
            return mapper.find_by_email(email)

    def get_all_users(self):
        """Alle Benutzer auslesen."""
        with UserMapper() as mapper:
            return mapper.find_all()

    def save_user(self, user):
        """Benutzer speichern."""
        with UserMapper() as mapper:
            mapper.update(user)

    def delete_user(self, user):
        """Benutzer löschen."""
        with UserMapper() as mapper:
            mapper.delete(user)

    """
    Clothing-spezifische Methoden
    """
    def create_clothing(self, name, category, color, season, user_id):
        """Ein Kleidungsstück anlegen."""
        clothing = Clothing()
        clothing.set_name(name)
        clothing.set_category(category)
        clothing.set_color(color)
        clothing.set_season(season)
        clothing.set_user_id(user_id)
        clothing.set_id(1)

        with ClothingMapper() as mapper:
            return mapper.insert(clothing)

    def get_clothing_by_name(self, name):
        """Kleidungsstücke mit Namen auslesen."""
        with ClothingMapper() as mapper:
            return mapper.find_by_name(name)

    def get_clothing_by_category(self, category):
        """Kleidungsstücke nach Kategorie auslesen."""
        with ClothingMapper() as mapper:
            return mapper.find_by_category(category)

    def get_clothing_by_season(self, season):
        """Kleidungsstücke nach Saison auslesen."""
        with ClothingMapper() as mapper:
            return mapper.find_by_season(season)

    def get_clothing_by_user(self, user_id):
        """Alle Kleidungsstücke eines Benutzers auslesen."""
        with ClothingMapper() as mapper:
            return mapper.find_by_user_id(user_id)

    def save_clothing(self, clothing):
        """Kleidungsstück speichern."""
        with ClothingMapper() as mapper:
            mapper.update(clothing)

    def delete_clothing(self, clothing):
        """Kleidungsstück löschen."""
        with ClothingMapper() as mapper:
            # Zuerst alle Outfits anpassen, die dieses Kleidungsstück enthalten
            outfits = self.get_outfits_by_clothing(clothing)
            if outfits:
                for outfit in outfits:
                    outfit.remove_clothing(clothing)
                    self.save_outfit(outfit)
            mapper.delete(clothing)

    """
    Outfit-spezifische Methoden
    """
    def create_outfit(self, name, user_id, clothing_items=None):
        """Ein Outfit anlegen."""
        outfit = Outfit()
        outfit.set_name(name)
        outfit.set_user_id(user_id)
        if clothing_items:
            outfit.set_clothing_items(clothing_items)
        outfit.set_id(1)

        with OutfitMapper() as mapper:
            return mapper.insert(outfit)

    def get_outfit_by_name(self, name):
        """Outfit mit Namen auslesen."""
        with OutfitMapper() as mapper:
            return mapper.find_by_name(name)

    def get_outfits_by_user(self, user_id):
        """Alle Outfits eines Benutzers auslesen."""
        with OutfitMapper() as mapper:
            return mapper.find_by_user_id(user_id)

    def get_outfits_by_clothing(self, clothing):
        """Alle Outfits finden, die ein bestimmtes Kleidungsstück enthalten."""
        with OutfitMapper() as mapper:
            return mapper.find_by_clothing_id(clothing.get_id())

    def save_outfit(self, outfit):
        """Outfit speichern."""
        with OutfitMapper() as mapper:
            mapper.update(outfit)

    def delete_outfit(self, outfit):
        """Outfit löschen."""
        with OutfitMapper() as mapper:
            mapper.delete(outfit)

    """
    Category-spezifische Methoden
    """
    def create_category(self, name, description):
        """Eine Kategorie anlegen."""
        category = Category()
        category.set_name(name)
        category.set_description(description)
        category.set_id(1)

        with CategoryMapper() as mapper:
            return mapper.insert(category)

    def get_all_categories(self):
        """Alle Kategorien auslesen."""
        with CategoryMapper() as mapper:
            return mapper.find_all()

    def get_category_by_name(self, name):
        """Kategorie nach Namen auslesen."""
        with CategoryMapper() as mapper:
            return mapper.find_by_name(name)

    def save_category(self, category):
        """Kategorie speichern."""
        with CategoryMapper() as mapper:
            mapper.update(category)

    def delete_category(self, category):
        """Kategorie löschen."""
        with CategoryMapper() as mapper:
            # Überprüfen, ob noch Kleidungsstücke in dieser Kategorie existieren
            clothes = self.get_clothing_by_category(category)
            if clothes:
                # Optional: Kleidungsstücke einer Standard-Kategorie zuordnen
                default_category = self.get_category_by_name("Sonstiges")
                for item in clothes:
                    item.set_category(default_category)
                    self.save_clothing(item)
            mapper.delete(category)