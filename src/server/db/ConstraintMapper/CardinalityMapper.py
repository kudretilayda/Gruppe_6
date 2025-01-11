from src.server.db.Mapper import Mapper


class CardinalityConstraintMapper(Mapper):

    def find_all(self):
        cursor = self._cnx.cursor()
        cursor.execute("select * from digital_wardrobe.cardinality_constraint")
        result = cursor.fetchall()
        cursor.close()
        return result

    def find_by_key(self, key):
        cursor = self._cnx.cursor()
        cursor.execute("select * from digital_wardrobe.cardinality_constraint where id=%s", (key,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def insert(self, obj):
        cursor = self._cnx.cursor()
        command = ("insert into digital_wardrobe.cardinality_constraint (constraint_id, min_count, max_count) "
                   "value (%s, %s, %s)")
        cursor.execute(command, (obj.get_id(), obj.min_count, obj.max_count))
        self._cnx.commit()
        cursor.close()

    def update(self, obj):
        cursor = self._cnx.cursor()
        command = ("update digital_wardrobe.cardinality_constraint "
                   "set min_count=%s, max_count=%s where id=%s")
        cursor.execute(command, (obj.min_count, obj.max_count, obj.get_id()))
        self._cnx.commit()
        cursor.close()

    def delete(self, obj):
        cursor = self._cnx.cursor()
        command = "delete from digital_wardrobe.cardinality_constraint WHERE id=%s"
        cursor.execute(command, (obj.get_id(),))
        self._cnx.commit()
        cursor.close()
