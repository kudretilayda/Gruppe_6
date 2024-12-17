from src.server.UserMapper import UserMapper
from src.server.db.WardrobeMapper import WardrobeMapper
from src.server.db.ClothingItemMapper import ClothingItemMapper
from src.server.db.ClothingTypeMapper import ClothingTypeMapper
from src.server.db.StyleMapper import StyleMapper
from src.server.db.OutfitMapper import OutfitMapper
from src.server.db.ConstraintMapper import ConstraintMapper
from src.server.bo.User import User
from src.server.bo.Wardrobe import Wardrobe
from src.server.bo.ClothingItem import ClothingItem
from src.server.bo.ClothingType import ClothingType
from src.server.bo.Style import Style
from src.server.bo.Outfit import Outfit
from src.server.bo.Constraints import (
    UnaryConstraint,
    BinaryConstraint,
    ImplicationConstraint,
    MutexConstraint,
    CardinalityConstraint, ConstraintRule)


class Administration(object):
    """Diese Klasse aggregiert nahezu sämtliche Applikationslogik (engl. Business Logic).
    Sie ist wie eine Spinne, die sämtliche Zusammenhänge in ihrem Netz (in unserem
    Fall die Daten der Applikation) überblickt und für einen geordneten Ablauf und
    dauerhafte Konsistenz der Daten und Abläufe sorgt.
    Die Applikationslogik findet sich in den Methoden dieser Klasse. Jede dieser
    Methoden kann als *Transaction Script* bezeichnet werden. Dieser Name
    lässt schon vermuten, dass hier analog zu Datenbanktransaktion pro
    Transaktion gleiche mehrere Teilaktionen durchgeführt werden, die das System
    von einem konsistenten Zustand in einen anderen, auch wieder konsistenten
    Zustand überführen. Wenn dies zwischenzeitig scheitern sollte, dann ist das
    jeweilige Transaction Script dafür verwantwortlich, eine Fehlerbehandlung
    durchzuführen.
    Diese Klasse steht mit einer Reihe weiterer Datentypen in Verbindung. Diese
    sind:
    - die Klassen BusinessObject und deren Subklassen,
    - die Mapper-Klassen für den DB-Zugriff."""

    def __init__(self):
        pass

#### User-spezifische Methoden ####

    def create_user(self, user_id, google_id, vorname="", nachname="", nickname="", email=""):
        user = User()
        user.set_user_id(user_id)
        user.set_google_id(google_id)
        user.set_firstname(vorname)
        user.set_lastname(nachname)
        user.set_nickname(nickname)
        user.set_email(email)

        with UserMapper() as mapper:
            return mapper.insert(user)

    def get_user_by_id(self, user_id):
        """Den User mit gegebener ID ausgeben."""
        with UserMapper() as mapper:
            return mapper.find_by_id(user_id)

    def get_user_by_google_id(self, google_id):
        """Den User mit der gegebenen google_id ausgeben."""
        with UserMapper() as mapper:
            return mapper.find_user_by_google_id(google_id)

def get_user_by_vorname(self, vorname):
    """Alle User mit dem Vornamen auslesen."""
    with UserMapper() as mapper:
        return mapper.find_user_by_vorname(vorname)

def get_user_by_nickname(self, nickname):
    """Alle User mit dem Nickname auslesen."""
    with UserMapper() as mapper:
        return mapper.find_user_by_nickname(nickname)

def get_user_by_email(self, email):
    """Alle User mit gegebener E-Mail-Adresse auslesen."""
    with UserMapper() as mapper:
        return mapper.find_user_by_email(email)

def get_user_by_id(self, number):
    """Den User mit gegebener ID ausgeben."""
    with UserMapper() as mapper:
        return mapper.find_by_id(number)

def get_user_by_google_id(self, id):
    """Den User mit der gegebenen google_id ausgeben."""
    with UserMapper() as mapper:
        return mapper.find_user_by_google_id(id)

def get_all_users(self):
    """Alle User ausgeben."""
    with UserMapper() as mapper:
        return mapper.find_all()

def change_user(self, user):
    """Den gegebenen User speichern."""
    with UserMapper() as mapper:
        return mapper.update(user)

def delete_user(self, user: User):
    """Den gegebenen User aus unserem System löschen."""
    all_styles = self.get_all_styles()
    if not isinstance(all_styles, list):
        all_styles = [all_styles]
    all_outfits = self.get_all_outfits()
    if not isinstance(all_outfits, list):
        all_outfits = [all_outfits]
    all_kleidungstypen = self.get_all_kleidungstypen()
    if not isinstance(all_kleidungstypen, list):
        all_kleidungstypen = [all_kleidungstypen]
    all_kleidungsstuecke = self.get_all_kleidungsstuecke()
    if not isinstance(all_kleidungsstuecke, list):
        all_kleidungsstuecke = [all_kleidungsstuecke]
    all_kleiderschraenke = self.get_all_kleiderschraenke()
    if not isinstance(all_kleiderschraenke, list):
        all_kleiderschraenke = [all_kleiderschraenke]

    # Alle Constraint-Typen abrufen
    all_constraints = self.get_all_constraints()
    if not isinstance(all_constraints, list):
        all_constraints = [all_constraints]    
    all_cardinality_constraints = self.get_all_cardinality_constraints()
    if not isinstance(all_cardinality_constraints, list):
        all_cardinality_constraints = [all_cardinality_constraints]
    all_unary_constraints = self.get_all_unary_constraints()
    if not isinstance(all_unary_constraints, list):
        all_unary_constraints = [all_unary_constraints]
    all_binary_constraints = self.get_all_binary_constraints()
    if not isinstance(all_binary_constraints, list):
        all_binary_constraints = [all_binary_constraints]
    all_implication_constraints = self.get_all_implication_constraints()
    if not isinstance(all_implication_constraints, list):
        all_implication_constraints = [all_implication_constraints]
    all_mutex_constraints = self.get_all_mutex_constraints()
    if not isinstance(all_mutex_constraints, list):
        all_mutex_constraints = [all_mutex_constraints]

    # delete user implication_constraints
    for constraint in all_implication_constraints:
        if constraint.get_user_id() == user.get_id():
            self.delete_implication_constraint(constraint)
    # delete user mutex_constraints           
    for constraint in all_mutex_constraints:
        if constraint.get_user_id() == user.get_id():
            self.delete_mutex_constraint(constraint)
    # delete binary_constraints
    for constraint in all_binary_constraints:
        if constraint.get_user_id() == user.get_id():
            self.delete_binary_constraint(constraint)
    # delete cardinality_constraints        
    for constraint in all_cardinality_constraints:
        if constraint.get_user_id() == user.get_id():
            self.delete_cardinality_constraint(constraint)
    # delete unary_constraints       
    for constraint in all_unary_constraints:
        if constraint.get_user_id() == user.get_id():
            self.delete_unary_constraint(constraint)
    # delete user constraints       
    for constraint in all_constraints:
        if constraint.get_user_id() == user.get_id():
            self.delete_constraint(constraint)            
    # delete user styles
    for style in all_styles:
        if style.get_user_id() == user.get_id():
            self.delete_style(style)
    # delete user outfits
    for outfit in all_outfits:
        if outfit.get_user_id() == user.get_id():
            self.delete_outfit(outfit)
    # delete user kleidungstypen
    for typ in all_kleidungstypen:
        if typ.get_user_id() == user.get_id():
            self.delete_kleidungstyp(typ)
    # delete user kleidungsstuecke
    for stueck in all_kleidungsstuecke:
        if stueck.get_user_id() == user.get_id():
            self.delete_kleidungsstueck(stueck)
    # delete user kleiderschraenke
    for schrank in all_kleiderschraenke:
        if schrank.get_user_id() == user.get_id():
            self.delete_kleiderschrank(schrank)

    with UserMapper() as mapper:
        mapper.delete(user)

    #####################################
    #### Style-spezifische Methoden #####
    #####################################

    def create_style(self, style: Style):
        """Erstellt einen neuen Style."""

        with StyleMapper() as mapper:
            return mapper.insert(style)

    def get_all_style(self):
        """Auslesen von allen Style"""

        with StyleMapper() as mapper:
            return mapper.find_all()

    def get_style_by_id(self, style_id):
        """ChatMessage mit gegebener ID ausgeben"""

        with StyleMapper() as mapper:
            return mapper.find_by_id(style_id)

    def get_style_by_user_id(self, user_id):
        """ChatMessage mit gegebener user ID ausgeben"""

        with StyleMapper() as mapper:
            return mapper.find_by_style_id(user_id)

    def get_style_by_style_id(self, style_id):
        """ChatMessage mit gegebener chat ID ausgeben"""

        all_styles = self.get_all_style()
        if not isinstance(all_styles, list):
            all_styles = [all_styles]

        styles = []
        for style in all_styles:
            if style.get_style_id() == int(style_id):
                styles.append(style)

        return styles

    def change_style(self, style):
        """Style Update"""

        with StyleMapper() as mapper:
            return mapper.update(style)

    def delete_style(self, style):
        """Style löschen"""

        with StyleMapper() as mapper:
            return mapper.delete(style)
        
    #####################################
    #### Outfit-spezifische Methoden ####
    #####################################

    def create_outfit(self, outfit: Outfit):
        """Erstellt ein neues Outfit."""

        with OutfitMapper() as mapper:
            return mapper.insert(outfit)

    def get_all_outfit(self):
        """Auslesen von allen Outfits."""

        with OutfitMapper() as mapper:
            return mapper.find_all()

    def get_outfit_by_id(self, outfit_id):
        """Outfit mit gegebener ID ausgeben."""

        with OutfitMapper() as mapper:
            return mapper.find_by_id(outfit_id)

    def get_outfit_by_user_id(self, user_id):
        """Outfits mit gegebener User ID ausgeben."""

        with OutfitMapper() as mapper:
            return mapper.find_by_user_id(user_id)

    def get_outfit_by_outfit_id(self, outfit_id):
        """Outfits mit gegebener Outfit ID ausgeben."""

        all_outfits = self.get_all_outfit()
        if not isinstance(all_outfits, list):
            all_outfits = [all_outfits]

        outfits = []
        for outfit in all_outfits:
            if outfit.get_outfit_id() == int(outfit_id):
                outfits.append(outfit)

        return outfits

    def change_outfit(self, outfit):
        """Outfit Update."""

        with OutfitMapper() as mapper:
            return mapper.update(outfit)

    def delete_outfit(self, outfit):
        """Outfit löschen."""

        with OutfitMapper() as mapper:
            return mapper.delete(outfit)

    ###########################################
    #### Kleidungstyp-spezifische Methoden ####
    ###########################################

    def create_kleidungstyp(self, kleidungstyp: ClothingType):
        """Erstellt einen neuen Kleidungstyp."""

        with ClothingTypeMapper() as mapper:
            return mapper.insert(kleidungstyp)

    def get_all_kleidungstyp(self):
        """Auslesen von allen Kleidungstypen."""

        with ClothingTypeMapper() as mapper:
            return mapper.find_all()

    def get_kleidungstyp_by_id(self, kleidungstyp_id):
        """Kleidungstyp mit gegebener ID ausgeben."""

        with ClothingTypeMapper() as mapper:
            return mapper.find_by_id(kleidungstyp_id)

    def get_kleidungstyp_by_name(self, name):
        """Kleidungstyp mit gegebenem Namen ausgeben."""

        with ClothingTypeMapper() as mapper:
            return mapper.find_by_name(name)

    def get_kleidungstyp_by_verwendung(self, verwendung):
        """Kleidungstyp mit gegebener Verwendung ausgeben."""

        with ClothingTypeMapper() as mapper:
            return mapper.find_by_verwendung(verwendung)

    def change_kleidungstyp(self, kleidungstyp):
        """Kleidungstyp Update."""

        with ClothingTypeMapper() as mapper:
            return mapper.update(kleidungstyp)

    def delete_kleidungstyp(self, kleidungstyp):
        """Kleidungstyp löschen."""

        with ClothingTypeMapper() as mapper:
            return mapper.delete(kleidungstyp)

    #############################################
    #### Kleidungsstueck-spezifische Methoden ###
    #############################################

    def create_kleidungsstueck(self, kleidungsstueck: ClothingItem):
        """Erstellt ein neues Kleidungsstück."""

        with ClothingItemMapper() as mapper:
            return mapper.insert(kleidungsstueck)

    def get_all_kleidungsstueck(self):
        """Auslesen von allen Kleidungsstücken."""

        with ClothingItemMapper() as mapper:
            return mapper.find_all()

    def get_kleidungsstueck_by_id(self, kleidungsstueck_id):
        """Kleidungsstück mit gegebener ID ausgeben."""

        with ClothingItemMapper() as mapper:
            return mapper.find_by_id(kleidungsstueck_id)

    def get_kleidungsstueck_by_name(self, name):
        """Kleidungsstück mit gegebenem Namen ausgeben."""

        with ClothingItemMapper() as mapper:
            return mapper.find_by_name(name)

    def get_kleidungsstueck_by_size(self, size):
        """Kleidungsstücke mit gegebener Größe ausgeben."""

        with ClothingItemMapper() as mapper:
            return mapper.find_by_size(size)

    def get_kleidungsstueck_by_color(self, color):
        """Kleidungsstücke mit gegebener Farbe ausgeben."""

        with ClothingItemMapper() as mapper:
            return mapper.find_by_color(color)

    def get_kleidungsstueck_by_kleidungstyp(self, kleidungstyp_id):
        """Kleidungsstücke mit gegebenem Kleidungstyp ausgeben."""

        with ClothingItemMapper() as mapper:
            return mapper.find_by_kleidungstyp(kleidungstyp_id)

    def change_kleidungsstueck(self, kleidungsstueck):
        """Kleidungsstück Update."""

        with ClothingItemMapper() as mapper:
            return mapper.update(kleidungsstueck)

    def delete_kleidungsstueck(self, kleidungsstueck):
        """Kleidungsstück löschen."""

        with ClothingItemMapper() as mapper:
            return mapper.delete(kleidungsstueck)

    #############################################
    #### Kleiderschrank-spezifische Methoden ####
    #############################################

    def create_kleiderschrank(self, kleiderschrank: Wardrobe):
        """Erstellt einen neuen Kleiderschrank."""

        with WardrobeMapper() as mapper:
            return mapper.insert(kleiderschrank)

    def get_all_kleiderschrank(self):
        """Auslesen von allen Kleiderschränken."""

        with WardrobeMapper() as mapper:
            return mapper.find_all()

    def get_kleiderschrank_by_id(self, kleiderschrank_id):
        """Kleiderschrank mit gegebener ID ausgeben."""

        with WardrobeMapper() as mapper:
            return mapper.find_by_id(kleiderschrank_id)

    def get_kleiderschrank_by_eigentuemer(self, eigentuemer_id):
        """Kleiderschrank mit gegebenem Eigentümer ausgeben."""

        with WardrobeMapper() as mapper:
            return mapper.find_by_eigentuemer(eigentuemer_id)

    def get_inhalt_of_kleiderschrank(self, kleiderschrank_id):
        """Inhalt eines Kleiderschranks mit gegebener ID ausgeben."""

        kleiderschrank = self.get_kleiderschrank_by_id(kleiderschrank_id)
        return kleiderschrank._inhalt if kleiderschrank else []

    def get_outfits_of_kleiderschrank(self, kleiderschrank_id):
        """Outfits eines Kleiderschranks mit gegebener ID ausgeben."""

        kleiderschrank = self.get_kleiderschrank_by_id(kleiderschrank_id)
        return kleiderschrank._outfits if kleiderschrank else []

    def change_kleiderschrank(self, kleiderschrank):
        """Kleiderschrank Update."""

        with WardrobeMapper() as mapper:
            return mapper.update(kleiderschrank)

    def delete_kleiderschrank(self, kleiderschrank):
        """Kleiderschrank löschen."""

        with WardrobeMapper() as mapper:
            return mapper.delete(kleiderschrank)

    #############################################
    ### BinaryConstraint-spezifische Methoden ###
    #############################################

    def create_binary_constraint(self, constraint: BinaryConstraint):
        """Erstellt einen neuen BinaryConstraint."""

        with ConstraintMapper() as mapper:
            return mapper.insert(constraint)

    def get_all_binary_constraint(self):
        """Auslesen von allen BinaryConstraints."""

        with ConstraintMapper() as mapper:
            return mapper.find_all()

    def get_binary_constraint_by_id(self, constraint_id):
        """BinaryConstraint mit gegebener ID ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_id(constraint_id)

    def get_binary_constraint_by_objects(self, obj1_id, obj2_id):
        """BinaryConstraint mit gegebenen Objekten ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_objects(obj1_id, obj2_id)

    def get_binary_constraint_by_bedingung(self, bedingung):
        """BinaryConstraints mit gegebener Bedingung ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_bedingung(bedingung)

    def change_binary_constraint(self, constraint):
        """BinaryConstraint Update."""

        with ConstraintMapper() as mapper:
            return mapper.update(constraint)

    def delete_binary_constraint(self, constraint):
        """BinaryConstraint löschen."""

        with ConstraintMapper() as mapper:
            return mapper.delete(constraint)

    #############################################
    #### UnaryConstraint-spezifische Methoden ###
    #############################################

    def create_unary_constraint(self, constraint: UnaryConstraint):
        """Erstellt einen neuen UnaryConstraint."""

        with ConstraintMapper() as mapper:
            return mapper.insert(constraint)

    def get_all_unary_constraint(self):
        """Auslesen von allen UnaryConstraints."""

        with ConstraintMapper() as mapper:
            return mapper.find_all()

    def get_unary_constraint_by_id(self, constraint_id):
        """UnaryConstraint mit gegebener ID ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_id(constraint_id)

    def get_unary_constraint_by_bezugsobjekt(self, bezugsobjekt_id):
        """UnaryConstraints mit gegebenem Bezugsobjekt ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_bezugsobjekt(bezugsobjekt_id)

    def get_unary_constraint_by_bedingung(self, bedingung):
        """UnaryConstraints mit gegebener Bedingung ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_bedingung(bedingung)

    def change_unary_constraint(self, constraint):
        """UnaryConstraint Update."""

        with ConstraintMapper() as mapper:
            return mapper.update(constraint)

    def delete_unary_constraint(self, constraint):
        """UnaryConstraint löschen."""

        with ConstraintMapper() as mapper:
            return mapper.delete(constraint)

    ################################################
    ## ImplicationConstraint-spezifische Methoden ##
    ################################################

    def create_implication_constraint(self, constraint: ImplicationConstraint):
        """Erstellt einen neuen ImplicationConstraint."""

        with ConstraintMapper() as mapper:
            return mapper.insert(constraint)

    def get_all_implication_constraints(self):
        """Auslesen von allen ImplicationConstraints."""

        with ConstraintMapper() as mapper:
            return mapper.find_all()

    def get_implication_constraint_by_id(self, constraint_id):
        """ImplicationConstraint mit gegebener ID ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_id(constraint_id)

    def get_implication_constraints_by_condition(self, condition_attribute, condition_value):
        """ImplicationConstraints mit einer bestimmten Bedingung ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_condition(condition_attribute, condition_value)

    def get_implication_constraints_by_implication(self, implication_attribute, implication_value):
        """ImplicationConstraints mit einer bestimmten Implikation ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_implication(implication_attribute, implication_value)

    def change_implication_constraint(self, constraint):
        """ImplicationConstraint Update."""

        with ConstraintMapper() as mapper:
            return mapper.update(constraint)

    def delete_implication_constraint(self, constraint):
        """ImplicationConstraint löschen."""

        with ConstraintMapper() as mapper:
            return mapper.delete(constraint)

    #############################################
    ### MutexConstraint-spezifische Methoden ####
    #############################################

    def create_mutex_constraint(self, constraint: MutexConstraint):
        """Erstellt eine neue MutexConstraint."""

        with ConstraintMapper() as mapper:
            return mapper.insert(constraint)

    def get_all_mutex_constraints(self):
        """Auslesen von allen MutexConstraints."""

        with ConstraintMapper() as mapper:
            return mapper.find_all()

    def get_mutex_constraint_by_id(self, constraint_id):
        """MutexConstraint mit gegebener ID ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_id(constraint_id)

    def get_mutex_constraints_by_obj1(self, obj1_attribute, obj1_value):
        """MutexConstraints mit gegebenem Attribut und Wert für das erste Objekt ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_obj1(obj1_attribute, obj1_value)

    def get_mutex_constraints_by_obj2(self, obj2_attribute, obj2_value):
        """MutexConstraints mit gegebenem Attribut und Wert für das zweite Objekt ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_obj2(obj2_attribute, obj2_value)

    def get_mutex_constraints_by_objects(self, obj1_attribute, obj1_value, obj2_attribute, obj2_value):
        """MutexConstraints mit spezifischen Attributen und Werten für beide Objekte ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_objects(obj1_attribute, obj1_value, obj2_attribute, obj2_value)

    def change_mutex_constraint(self, constraint):
        """MutexConstraint Update."""

        with ConstraintMapper() as mapper:
            return mapper.update(constraint)

    def delete_mutex_constraint(self, constraint):
        """MutexConstraint löschen."""

        with ConstraintMapper() as mapper:
            return mapper.delete(constraint)

    ################################################
    ## CardinalityConstraint-spezifische Methoden ##
    ################################################

    def create_cardinality_constraint(self, constraint: CardinalityConstraint):
        """Erstellt eine neue CardinalityConstraint."""

        with ConstraintMapper() as mapper:
            return mapper.insert(constraint)

    def get_all_cardinality_constraints(self):
        """Auslesen von allen CardinalityConstraints."""

        with ConstraintMapper() as mapper:
            return mapper.find_all()

    def get_cardinality_constraint_by_id(self, constraint_id):
        """CardinalityConstraint mit gegebener ID ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_id(constraint_id)

    def get_cardinality_constraints_by_obj1(self, obj1_attribute, obj1_value):
        """CardinalityConstraints mit gegebenem Attribut und Wert für das erste Objekt ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_obj1(obj1_attribute, obj1_value)

    def get_cardinality_constraints_by_obj2(self, obj2_attribute, obj2_value):
        """CardinalityConstraints mit gegebenem Attribut und Wert für das zweite Objekt ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_obj2(obj2_attribute, obj2_value)

    def get_cardinality_constraints_by_objects(self, obj1_attribute, obj1_value, obj2_attribute, obj2_value):
        """CardinalityConstraints mit spezifischen Attributen und Werten für beide Objekte ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_objects(obj1_attribute, obj1_value, obj2_attribute, obj2_value)

    def get_cardinality_constraints_by_min_count(self, min_count):
        """CardinalityConstraints mit einer Mindestanzahl ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_min_count(min_count)

    def get_cardinality_constraints_by_max_count(self, max_count):
        """CardinalityConstraints mit einer Höchstanzahl ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_max_count(max_count)

    def get_cardinality_constraints_by_count_range(self, min_count, max_count):
        """CardinalityConstraints innerhalb eines bestimmten Bereichs von Anzahlen ausgeben."""

        with ConstraintMapper() as mapper:
            return mapper.find_by_count_range(min_count, max_count)

    def change_cardinality_constraint(self, constraint):
        """CardinalityConstraint Update."""

        with ConstraintMapper() as mapper:
            return mapper.update(constraint)

    def delete_cardinality_constraint(self, constraint):
        """CardinalityConstraint löschen."""

        with ConstraintMapper() as mapper:
            return mapper.delete(constraint)

    #########################################
    #### Constraint-spezifische Methoden ####
    #########################################

    ##################################
    ###### Generator Algorithmus #####
    ##################################
