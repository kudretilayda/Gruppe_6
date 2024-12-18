from src.server.db.Mapper import Mapper


class StyleMapper(Mapper):
    def __init__(self):
        super().__init__()
        self._constraint_mapper = ConstraintMapper()

    def insert(self, style):
        """Fügt einen neuen Style in die DB ein"""
        cursor = self._cnx.cursor()

        # Style-Basisdaten einfügen
        command = "INSERT INTO style (name) VALUES (%s)"
        cursor.execute(command, (style.get_name(),))
        style.set_id(cursor.lastrowid)

        # Clothing Types für den Style einfügen
        for clothing_type in style.get_clothing_types():
            command = """INSERT INTO style_clothing_type 
                        (style_id, clothing_type_id) 
                        VALUES (%s, %s)"""
            cursor.execute(command, (style.get_id(), clothing_type.get_id()))

        # Constraints werden über den ConstraintMapper gespeichert
        for constraint in style.get_constraints():
            constraint.set_style_id(style.get_id())
            self._constraint_mapper.insert(constraint)

        self._cnx.commit()
        cursor.close()
        return style

    def find_by_id(self, id):
        """Lädt einen Style mit allen zugehörigen Daten"""
        cursor = self._cnx.cursor()

        # Style-Basisdaten laden
        command = "SELECT * FROM style WHERE id=%s"
        cursor.execute(command, (id,))
        style_data = cursor.fetchone()

        if not style_data:
            return None

        style = Style()
        style.set_id(style_data[0])
        style.set_name(style_data[1])

        # Zugehörige ClothingTypes laden
        command = """SELECT ct.* FROM clothing_type ct
                    JOIN style_clothing_type sct ON ct.id = sct.clothing_type_id
                    WHERE sct.style_id=%s"""
        cursor.execute(command, (id,))

        for ct_data in cursor.fetchall():
            clothing_type = ClothingType()
            clothing_type.set_id(ct_data[0])
            clothing_type.set_name(ct_data[1])
            clothing_type.set_usage(ct_data[2])
            style.add_clothing_type(clothing_type)

        # Constraints über ConstraintMapper laden
        constraints = self._constraint_mapper.find_by_style(id)
        for constraint in constraints:
            style.add_constraint(constraint)

        cursor.close()
        return style

    def update(self, style):
        """Aktualisiert einen Style"""
        cursor = self._cnx.cursor()

        # Style-Basisdaten aktualisieren
        command = "UPDATE style SET name=%s WHERE id=%s"
        cursor.execute(command, (style.get_name(), style.get_id()))

        # Clothing Types aktualisieren
        # Zunächst alle bestehenden Verknüpfungen löschen
        command = "DELETE FROM style_clothing_type WHERE style_id=%s"
        cursor.execute(command, (style.get_id(),))

        # Dann neue Verknüpfungen einfügen
        for clothing_type in style.get_clothing_types():
            command = """INSERT INTO style_clothing_type 
                        (style_id, clothing_type_id) 
                        VALUES (%s, %s)"""
            cursor.execute(command, (style.get_id(), clothing_type.get_id()))

        # Constraints aktualisieren würde über ConstraintMapper erfolgen

        self._cnx.commit()
        cursor.close()
        return style


"Speichern und Laden von Styles"
"Verwaltung der Beziehungen zu ClothingTypes"
"Integration mit dem ConstraintMapper"