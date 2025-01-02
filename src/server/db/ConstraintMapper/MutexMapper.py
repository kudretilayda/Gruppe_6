from src.server.db.Mapper import Mapper


class MutexConstraintMapper(Mapper):

    def find_all(self):
        cursor = self._cnx.cursor()
        cursor.execute('select * from digital_wardrobe.mutex_constraint')
        result = cursor.fetchall()
        cursor.close()
        return result

    def find_by_key(self, key):
        cursor = self._cnx.cursor()
        cursor.execute('select * from digital_wardrobe.mutex_constraint where id = %s', (key,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def insert(self, obj):
        cursor = self._cnx.cursor()
        command = ("insert into digital_wardrobe.mutex_constraint (constraint_id, item_1_id, item_2_id) "
                   "values (%s, %s, %s)")
        cursor.execute(command, (obj.get_id(), obj.item_1.get_id(), obj.item_2.get_id()))
        self._cnx.commit()
        cursor.close()

    def update(self, obj):
        cursor = self._cnx.cursor()
        command = ("update digital_wardrobe.mutex_constraint "
                   "set item_1_id=%s, item_2_id=%s where id=%s")
        cursor.execute(command, (obj.item_1.get_id(), obj.item_2.get_id(), obj.get_id()))
        self._cnx.commit()
        cursor.close()

    def delete(self, obj):
        cursor = self._cnx.cursor()
        command = 'delete from digital_wardrobe.mutex_constraint where id = %s'
        cursor.execute(command, (obj.get_id(),))
        self._cnx.commit()
        cursor.close()


