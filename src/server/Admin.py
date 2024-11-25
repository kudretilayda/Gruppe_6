from .bo.BinaryConstraint import BinaryConstraint
from .bo.BusinessObject import BusinessObject
from .bo.CardinalityConstraint import CardinalityConstraint
from .bo.Constraint import Constraint
from .bo.ImplicationConstraint import ImplicationConstraint
from .bo.Kleiderschrank import Kleiderschrank
from .bo.Kleidungsstueck import Kleidungsstueck
from .bo.Kleidungstyp import Kleidungstyp
from .bo.MutexConstraint import MutexConstraint
from .bo.Outfit import Outfit
from .bo.Style import Style
from .bo.UnaryConstraint import UnaryConstraint
from .bo.User import User

from .db.ConstraintMapper import 
from .db.KleiderschrankMapper import 
from .db.KleidungsstueckMapper import Kleidungsstueck
from .db.KleidungstypMapper import Kleidungstyp
from .db.Mapper import Mapper
from .db.StyleMapper import StyleMapper
from .db.UserMapper import 



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

    #####################################
    #### User-spezifische Methoden ######
    #####################################
    
def create_user(
    self, user_id, google_id, email, vorname="", nachname="", nickname=""
):
    """Einen User anlegen"""
    user = User()
    user.set_user_id(user_id)
    user.set_google_id(google_id)
    user.set_email(email)
    user.set_vorname(vorname)
    user.set_nachname(nachname)
    user.set_nickname(nickname)

    with UserMapper() as mapper:
        mapper.insert(user)

    db_user = self.get_user_by_google_id(google_id)
    return db_user

def get_user_by_nachname(self, nachname):
    """Alle User mit dem Nachnamen auslesen."""
    with UserMapper() as mapper:
        return mapper.find_user_by_nachname(nachname)

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
    #####################################
    #### Outfit-spezifische Methoden ####
    #####################################

    ####################################
    #### Style-spezifische Methoden ####
    ####################################

    #####################################
    #### Outfit-spezifische Methoden ####
    #####################################

    ###########################################
    #### Kleidungstyp-spezifische Methoden ####
    ###########################################

    #############################################
    #### Kleidungsstueck-spezifische Methoden ###
    #############################################

    #############################################
    #### Kleiderschrank-spezifische Methoden ####
    #############################################

    #############################################
    ### BinaryConstraint-spezifische Methoden ###
    #############################################

    #############################################
    #### UnaryConstraint-spezifische Methoden ###
    #############################################

    ################################################
    ## ImplicationConstraint-spezifische Methoden ##
    ################################################

    #############################################
    ### MutexConstraint-spezifische Methoden ####
    #############################################

    ################################################
    ## CardinalityConstraint-spezifische Methoden ##
    ################################################

    #########################################
    #### Constraint-spezifische Methoden ####
    #########################################

    ##################################
    ###### Generator Algorithmus #####
    ##################################
