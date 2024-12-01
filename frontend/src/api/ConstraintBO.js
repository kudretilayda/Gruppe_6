import BusinessObject from "./BusinessObject";

/**
 * Repräsentiert eine generische Einschränkung (Constraint).
 *
 * Eine Constraint besitzt einen Namen und eine Beschreibung.
 */
export default class ConstraintBO extends BusinessObject {
  /**
   * Konstruiert ein ConstraintBO-Objekt.
   *
   * @param {String} name - Der Name der Einschränkung.
   * @param {String} beschreibung - Die Beschreibung der Einschränkung.
   */
  constructor(name = "", beschreibung = "") {
    super();
    this.name = name;
    this.beschreibung = beschreibung;
  }

  // Getter und Setter für name
  getName() {
    return this.name;
  }

  setName(value) {
    this.name = value;
  }

  // Getter und Setter für beschreibung
  getBeschreibung() {
    return this.beschreibung;
  }

  setBeschreibung(value) {
    this.beschreibung = value;
  }

  // String-Darstellung des Objekts
  toString() {
    return `Constraint: ${this.getName()}, Beschreibung: ${this.getBeschreibung()}`;
  }

  /**
   * Wandelt eine JSON-Struktur in ein ConstraintBO-Objekt um.
   * @param {Object} dictionary - Die JSON-Daten, die das ConstraintBO beschreiben.
   * @returns {ConstraintBO} - Ein neues ConstraintBO-Objekt.
   */
  static fromJSON(dictionary = {}) {
    const constraint = new ConstraintBO();
    constraint.setName(dictionary.name || "");
    constraint.setBeschreibung(dictionary.beschreibung || "");
    return constraint;
  }
}
