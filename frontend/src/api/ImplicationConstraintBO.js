import ConstraintBO from "./ConstraintBO";

/**
 * Repräsentiert eine Implikations-Einschränkung (Implication Constraint).
 *
 * Eine ImplicationConstraint besitzt eine Bedingung (condition) 
 * und eine Implikation (implication).
 */
export default class ImplicationConstraintBO extends ConstraintBO {
  /**
   * Konstruiert ein ImplicationConstraintBO-Objekt.
   *
   * @param {Object} condition - Die Bedingung.
   * @param {Object} implication - Die Implikation.
   * @param {String} name - Der Name der Einschränkung.
   * @param {String} beschreibung - Die Beschreibung der Einschränkung.
   */
  constructor(
    condition = null,
    implication = null,
    name = "",
    beschreibung = ""
  ) {
    super(name, beschreibung);
    this.condition = condition;
    this.implication = implication;
  }

  // Getter und Setter für condition
  getCondition() {
    return this.condition;
  }

  setCondition(value) {
    this.condition = value;
  }

  // Getter und Setter für implication
  getImplication() {
    return this.implication;
  }

  setImplication(value) {
    this.implication = value;
  }

  // String-Darstellung des Objekts
  toString() {
    return `ImplicationConstraint: ${JSON.stringify(this.getCondition())} -> ${JSON.stringify(this.getImplication())}`;
  }

  /**
   * Wandelt eine JSON-Struktur in ein ImplicationConstraintBO-Objekt um.
   * @param {Object} dictionary - Die JSON-Daten, die das ImplicationConstraintBO beschreiben.
   * @returns {ImplicationConstraintBO} - Ein neues ImplicationConstraintBO-Objekt.
   */
  static fromJSON(dictionary = {}) {
    const implicationConstraint = new ImplicationConstraintBO();
    implicationConstraint.setCondition(dictionary.condition || null);
    implicationConstraint.setImplication(dictionary.implication || null);
    return implicationConstraint;
  }
}

