from src.server.db.Mapper import Mapper


class BinaryConstraintMapper(Mapper):

    def find_all(self):
        cursor = self._cnx.cursor()
        cursor.execute('select * from digital_wardrobe.binary_constraint')
        result = cursor.fetchall()
        cursor.close()
        return result

    def find_by_key(self, key):
        cursor = self._cnx.cursor()
        cursor.execute('select * from digital_wardrobe.binary_constraint where id=%s', (key,))
        result = cursor.fetchall()
        cursor.close()
        return result

    def insert(self, obj):
        cursor = self._cnx.cursor()
        command = ("INSERT INTO digital_wardrobe.binary_constraint (constraint_id, item_1_id, item_2_id) "
                   "VALUES (%s, %s, %s)")
        cursor.execute(command, (obj.get_id(), obj.item_1.get_id(), obj.item_2.get_id()))
        self._cnx.commit()
        cursor.close()

    def update(self, obj):
        cursor = self._cnx.cursor()
        command = ("UPDATE digital_wardrobe.binary_constraint "
                   "SET item_1_id=%s, item_2_id=%s WHERE id=%s")
        cursor.execute(command, (obj.item_1.get_id(), obj.item_2.get_id(), obj.get_id()))
        self._cnx.commit()
        cursor.close()

    def delete(self, obj):
        cursor = self._cnx.cursor()
        command = "DELETE FROM digital_wardrobe.binary_constraint WHERE id=%s"
        cursor.execute(command, (obj.get_id(),))
        self._cnx.commit()
        cursor.close()
