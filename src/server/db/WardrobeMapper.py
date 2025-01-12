from src.server.db.Mapper import Mapper
from src.server.bo.Wardrobe import Wardrobe

# WardrobeMapper Klasse erbt von Mapper und handhabt die Datenbankoperationen für Wardrobe-Objekte
class WardrobeMapper(Mapper):
    def find_all(self):
        """
        Gibt alle Wardrobe-Einträge aus der Datenbank zurück
        Returns: Liste von Wardrobe-Objekten
        """
        result = []
        cursor = self._cnx.cursor()
        # SQL-Query um alle Einträge aus der wardrobe-Tabelle zu selektieren
        cursor.execute("SELECT * FROM digital_wardrobe.wardrobe")
        tuples = cursor.fetchall()

        # Konvertiert die Datenbankeinträge in Wardrobe-Objekte
        for (wardrobe_id, wardrobe_owner) in tuples:
            wardrobe = Wardrobe()
            wardrobe.set_id(wardrobe_id)
            wardrobe.set_wardrobe_owner(wardrobe_owner)
            result.append(wardrobe)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_key(self, key):
        """
        Findet einen Wardrobe-Eintrag anhand seiner ID
        Args:
            key: Die ID des gesuchten Wardrobe-Eintrags
        Returns: Wardrobe-Objekt oder None wenn nicht gefunden
        """
        result = None
        cursor = self._cnx.cursor()
        # SQL-Query mit WHERE-Klausel für spezifische ID
        command = f"SELECT * FROM wardrobe WHERE id={key}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        # Wenn Eintrag gefunden wurde, konvertiere zu Wardrobe-Objekt
        if tuples:
            (wardrobe_id, wardrobe_owner) = tuples[0]
            result = Wardrobe()
            result.set_id(wardrobe_id)
            result.set_wardrobe_owner(wardrobe_owner)

        self._cnx.commit()
        cursor.close()
        return result