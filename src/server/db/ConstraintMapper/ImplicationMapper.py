from src.server.db.Mapper import Mapper


class ImplicationConstraintMapper(Mapper):

    def find_all(self):
        cursor = self._cnx.cursor()
        cursor.execute('select * from digital_wardrobe.implication_constraint')
        result = cursor.fetchall()
        cursor.close()
        return result

    def find_by_key(self, key):
        cursor = self._cnx.cursor()
        cursor.execute("select * from digital_wardrobe.implication_constraint where id=%s", (key,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def insert(self, obj):
        cursor = self._cnx.cursor()
        command = ("insert into digital_wardrobe.implication_constraint (constraint_id, if_type_id, then_type_id) "
                   "values (%s, %s, %s)")
        cursor.execute(command, (obj.get_id(), obj.if_type.get_id(), obj.then_type.get_id()))
        self._cnx.commit()
        cursor.close()

    def update(self, obj):
        cursor = self._cnx.cursor()
        command = "update digital_wardrobe.implication_constraint SET if_type_id=%s, then_type_id=%s WHERE id=%s"
        cursor.execute(command, (obj.if_type.get_id(), obj.then_type.get_id(), obj.get_id()))
        self._cnx.commit()
        cursor.close()

    def delete(self, obj):
        cursor = self._cnx.cursor()
        command = 'delete from digital_wardrobe.implication_constraint where id=%s'
        cursor.execute(command, (obj.get_id(),))
        self._cnx.commit()
        cursor.close()
