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