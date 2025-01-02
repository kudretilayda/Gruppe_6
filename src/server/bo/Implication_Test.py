class Kleidungstyp:
    """Repräsentiert einen Kleidungstyp, z. B. Pulli oder Hose."""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Kleidungstyp({self.name})"


class Kleidungsstueck:
    """Repräsentiert ein Kleidungsstück, das zu einem Kleidungstyp gehört."""
    def __init__(self, name):
        self.name = name
        self.kleidungstyp = None

    def __repr__(self):
        return f"Kleidungsstueck({self.name})"


class Style:
    """Repräsentiert einen Stil, der aus mehreren Kleidungstypen bestehen kann."""
    def __init__(self):
        self.clothing_types = []

    def append_clothing_type(self, kleidungstyp):
        self.clothing_types.append(kleidungstyp)

    def get_clothing_type(self):
        return self.clothing_types

    def __repr__(self):
        return f"Style({', '.join([str(ct) for ct in self.clothing_types])})"


class Outfit:
    """Repräsentiert ein Outfit, das Kleidungsstücke enthält und zu einem Stil gehört."""
    def __init__(self):
        self.inhalt = []
        self.style = None

    def set_style(self, style):
        self.style = style

    def __repr__(self):
        return f"Outfit({', '.join([str(k) for k in self.inhalt])}, Style={self.style})"


class Constraint:
    """Basisklasse für Constraints."""
    def validate(self, outfit):
        """Basismethode, die in abgeleiteten Klassen überschrieben wird."""
        raise NotImplementedError("Diese Methode muss in der Unterklasse implementiert werden.")


class Implikation(Constraint):
    """Repräsentiert ein Implikations-Constraint."""
    def __init__(self, kleidungstyp_if, kleidungstyp_then):
        """
        Initialisiert die Implikation.
        :param kleidungstyp_if: Der Kleidungstyp, der die Bedingung erfüllt.
        :param kleidungstyp_then: Der Kleidungstyp, der vorhanden sein muss, wenn die Bedingung erfüllt ist.
        """
        self.kleidungstyp_if = kleidungstyp_if
        self.kleidungstyp_then = kleidungstyp_then

    def validate(self, outfit):
        """
        Validiert das Constraint anhand eines Outfits.
        :param outfit: Das zu überprüfende Outfit.
        :return: True, wenn die Implikation erfüllt ist, False ansonsten.
        """
        # Prüfen, ob der Bedingungskleidungstyp (kleidungstyp_if) vorhanden ist
        if any(k.kleidungstyp == self.kleidungstyp_if for k in outfit.inhalt):
            # Wenn ja, prüfen, ob der "dann"-Kleidungstyp (kleidungstyp_then) auch vorhanden ist
            return any(k.kleidungstyp == self.kleidungstyp_then for k in outfit.inhalt)
        # Wenn die Bedingung nicht erfüllt ist, ist die Implikation automatisch wahr
        return True

    def __repr__(self):
        return f"Implikation({self.kleidungstyp_if} -> {self.kleidungstyp_then})"



# Erstellen von Objekten
pulli = Kleidungstyp("Pulli")
hose = Kleidungstyp("Hose")
style1 = Style()
rollkragenpulli = Kleidungsstueck("Rollkragenpulli")
jeans = Kleidungsstueck("Jeans")
outfit1 = Outfit()

# Beziehungen setzen
rollkragenpulli.kleidungstyp = pulli
jeans.kleidungstyp = hose
outfit1.inhalt = [rollkragenpulli]  # Das Outfit enthält nur den Rollkragenpulli
outfit1.set_style(style1)
style1.append_clothing_type(pulli)

# Constraint erstellen
constraint = Implikation(pulli, hose)  # Wenn Pulli, dann Hose

# Validierung
print(constraint.validate(outfit1))  # False, weil keine Hose im Outfit ist

# Hose hinzufügen und erneut validieren
outfit1.inhalt.append(jeans)
print(constraint.validate(outfit1))  # True, weil jetzt auch eine Hose im Outfit ist
