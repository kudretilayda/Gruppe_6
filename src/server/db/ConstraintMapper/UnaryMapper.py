from ..Mapper import Mapper


class UnaryConstraintMapper(Mapper):

    def find_all(self):
        cursor = self._cnx.cursor()
        cursor.execute('select * from digital_wardrobe.unary_constraint')
        result = cursor.fetchall()
        cursor.close()
        return result

    def find_by_key(self, key):
        cursor = self._cnx.cursor()
        cursor.execute('select * from digital_wardrobe.unary_constraint where id=%s', (key,))
        result = cursor.fetchall()
        cursor.close()
        return result

    def insert(self, obj):
        cursor = self._cnx.cursor()
        command = 'insert into digital_wardrobe.unary_constraint (constraint_id, style_id) values (%s, %s)'
        cursor.execute(command, (obj.get_id(), obj.style.get_id()))
        self._cnx.commit()
        cursor.close()

    def update(self, obj):
        cursor = self._cnx.cursor()
        command = 'update digital_wardrobe.unary_constraint set style_id=%s where id=%s'
        cursor.execute(command, (obj.style.get_id(), obj.get_id()))
        self._cnx.commit()
        cursor.close()

    def delete(self, obj):
        cursor = self._cnx.cursor()
        command = 'delete from digital_wardrobe.unary_constraint where id=%s'
        cursor.execute(command, (obj.get_id(),))
        self._cnx.commit()
        cursor.close()
