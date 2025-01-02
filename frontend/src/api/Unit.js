import BusinessObject from "./BusinessObject";

// Die Klasse `UnitBO` repräsentiert eine Einheit im digitalen Kleiderschrank, z.B. eine Kleidergröße oder Kategorie.
export default class UnitBO extends BusinessObject {

  /** Konstruktor für eine Einheit im digitalen Kleiderschrank
   * @param {String} adesignation - Bezeichnung der Einheit, z.B. "Größe", "Farbe", "Kleidungsart".
   * @param {String} awardrobe_id - ID des Kleiderschranks, dem diese Einheit zugeordnet ist.
   */
  constructor(adesignation, awardrobe_id) {
    super(); // Ruft den Konstruktor der übergeordneten Klasse (BusinessObject) auf.
    this.designation = adesignation; // Bezeichnung der Einheit (z.B. "Größe", "Farbe").
    this.wardrobe_id = awardrobe_id; // ID des Kleiderschranks, dem diese Einheit zugeordnet ist.
  }

  /** Gibt die Bezeichnung der Einheit zurück.
   * @returns {String} Die Bezeichnung der Einheit (z.B. "Größe", "Farbe").
   */
  getDesignation() {
    return this.designation;
  }

  /** Setzt eine neue Bezeichnung für die Einheit.
   * @param {String} adesignation - Neue Bezeichnung der Einheit.
   */
  setDesignation(adesignation) {
    this.designation = adesignation;
  }

  /** Gibt die ID des Kleiderschranks zurück.
   * @returns {String} Die ID des Kleiderschranks.
   */
  getWardrobeId() {
    return this.wardrobe_id;
  }

  /** Setzt die ID des Kleiderschranks für diese Einheit.
   * @param {String} awardrobe_id - Neue ID des Kleiderschranks.
   */
  setWardrobeId(awardrobe_id) {
    this.wardrobe_id = awardrobe_id;
  }

  /** Statische Methode zum Erzeugen von `UnitBO`-Instanzen aus JSON-Daten.
   * @param {Object|Array} units - JSON-Daten von Einheiten (kann ein Array oder ein einzelnes Objekt sein).
   * @returns {Array} Ein Array von `UnitBO`-Instanzen.
   */
  static fromJSON(units) {
    let result = [];
    // Überprüft, ob `units` ein Array ist. Wenn ja, iteriert durch jedes Element.
    if (Array.isArray(units)) {
      units.forEach((u) => {
        Object.setPrototypeOf(u, UnitBO.prototype);
        result.push(u);
      });
    } else {
      // Wenn `units` kein Array ist, behandelt es als singuläres Objekt.
      let u = units;
      Object.setPrototypeOf(u, UnitBO.prototype);
      result.push(u);
    }

    return result;
  }
}
