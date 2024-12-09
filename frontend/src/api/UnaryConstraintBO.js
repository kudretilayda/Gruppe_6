import ConstraintBO from "./ConstraintBO";

/**
 * Repräsentiert eine einstellige Einschränkung (Unary Constraint).
 */
export default class UnaryConstraintBO extends ConstraintBO {
  /**
   * Konstruiert ein UnaryConstraintBO-Objekt.
   *
   * @param {any} bezugsobjekt - Das Bezugsobjekt, auf das sich die Einschränkung bezieht.
   * @param {String} bedingung - Die Bedingung der Einschränkung.
   */
  constructor(bezugsobjekt = null, bedingung = "", name = "", beschreibung = "",) {
    super(name, beschreibung);
    this.bezugsobjekt = bezugsobjekt;
    this.bedingung = bedingung;
  }

  // Getter und Setter für bezugsobjekt
  getBezugsobjekt() {
    return this.bezugsobjekt;
  }

  setBezugsobjekt(value) {
    this.bezugsobjekt = value;
  }

  // Getter und Setter für bedingung
  getBedingung() {
    return this.bedingung;
  }

  setBedingung(value) {
    this.bedingung = value;
  }

  // String-Darstellung des Objekts
  toString() {
    return `UnaryConstraint: ${JSON.stringify(
      this.getBezugsobjekt()
    )}, ${this.getBedingung()}`;
  }

  /**
   * Wandelt eine JSON-Struktur in ein UnaryConstraintBO-Objekt um.
   * @param {Object} dictionary - Die JSON-Daten, die das UnaryConstraintBO beschreiben.
   * @returns {UnaryConstraintBO} - Ein neues UnaryConstraintBO-Objekt.
   */
  static fromJSON(dictionary = {}) {
    const unaryConstraint = new UnaryConstraintBO();
    unaryConstraint.setBezugsobjekt(dictionary.bezugsobjekt || null);
    unaryConstraint.setBedingung(dictionary.bedingung || "");
    return unaryConstraint;
  }
}
