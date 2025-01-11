from src.server.db.Mapper import Mapper

# Die Klasse BinaryConstraintMapper erbt von Mapper und dient der Interaktion mit der Tabelle „binary_constraint“ in der Datenbank.
class BinaryConstraintMapper(Mapper):

    # Diese Methode holt alle binären Constraints aus der Datenbank und gibt sie zurück
    def find_all(self):
        cursor = self._cnx.cursor()
        cursor.execute('select * from digital_wardrobe.binary_constraint')
        result = cursor.fetchall()
        cursor.close()
        return result

    # Diese Methode sucht einen binären Constraint basierend auf der übergebenen ID
    def find_by_key(self, key):
        cursor = self._cnx.cursor()
        cursor.execute('select * from digital_wardrobe.binary_constraint where id=%s', (key,))
        result = cursor.fetchall()
        cursor.close()
        return result

    # Diese Methode fügt einen neuen binären Constraint in die Datenbank ein
    def insert(self, obj):
        cursor = self._cnx.cursor()
        command = ("INSERT INTO digital_wardrobe.binary_constraint (constraint_id, item_1_id, item_2_id) "
                   "VALUES (%s, %s, %s)")
        cursor.execute(command, (obj.get_id(), obj.item_1.get_id(), obj.item_2.get_id()))
        self._cnx.commit()
        cursor.close()

    # Diese Methode aktualisiert einen bestehenden binären Constraint in der Datenbank
    def update(self, obj):
        cursor = self._cnx.cursor()
        command = ("UPDATE digital_wardrobe.binary_constraint "
                   "SET item_1_id=%s, item_2_id=%s WHERE id=%s")
        cursor.execute(command, (obj.item_1.get_id(), obj.item_2.get_id(), obj.get_id()))
        self._cnx.commit()
        cursor.close()

    # Diese Methode löscht einen binären Constraint aus der Datenbank
    def delete(self, obj):
        cursor = self._cnx.cursor()
        command = "DELETE FROM digital_wardrobe.binary_constraint WHERE id=%s"
        cursor.execute(command, (obj.get_id(),))
        self._cnx.commit()
        cursor.close()