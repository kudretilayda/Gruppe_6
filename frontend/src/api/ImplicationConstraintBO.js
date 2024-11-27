import ConstraintBO from "./ConstraintBO";

/**
 * Repräsentiert eine Implikations-Einschränkung (Implication Constraint).
 *
 * Eine ImplicationConstraint besitzt eine Bedingung (condition_attribute, condition_value) 
 * und eine Implikation (implication_attribute, implication_value).
 */
export default class ImplicationConstraintBO extends ConstraintBO {
  /**
   * Konstruiert ein ImplicationConstraintBO-Objekt.
   *
   * @param {String} conditionAttribute - Das Attribut der Bedingung.
   * @param {String} conditionValue - Der Wert der Bedingung.
   * @param {String} implicationAttribute - Das Attribut der Implikation.
   * @param {String} implicationValue - Der Wert der Implikation.
   */
  constructor(
    conditionAttribute = "",
    conditionValue = "",
    implicationAttribute = "",
    implicationValue = "",
    name = "",
    beschreibung = "",
  ) {
    super(name, beschreibung);
    this.conditionAttribute = conditionAttribute;
    this.conditionValue = conditionValue;
    this.implicationAttribute = implicationAttribute;
    this.implicationValue = implicationValue;
  }

  // Getter und Setter für conditionAttribute
  getConditionAttribute() {
    return this.conditionAttribute;
  }

  setConditionAttribute(value) {
    this.conditionAttribute = value;
  }

  // Getter und Setter für conditionValue
  getConditionValue() {
    return this.conditionValue;
  }

  setConditionValue(value) {
    this.conditionValue = value;
  }

  // Getter und Setter für implicationAttribute
  getImplicationAttribute() {
    return this.implicationAttribute;
  }

  setImplicationAttribute(value) {
    this.implicationAttribute = value;
  }

  // Getter und Setter für implicationValue
  getImplicationValue() {
    return this.implicationValue;
  }

  setImplicationValue(value) {
    this.implicationValue = value;
  }

  // String-Darstellung des Objekts
  toString() {
    return `ImplicationConstraint: ${this.getConditionAttribute()}=${this.getConditionValue()} -> ${this.getImplicationAttribute()}=${this.getImplicationValue()}`;
  }

  /**
   * Wandelt eine JSON-Struktur in ein ImplicationConstraintBO-Objekt um.
   * @param {Object} dictionary - Die JSON-Daten, die das ImplicationConstraintBO beschreiben.
   * @returns {ImplicationConstraintBO} - Ein neues ImplicationConstraintBO-Objekt.
   */
  static fromJSON(dictionary = {}) {
    const implicationConstraint = new ImplicationConstraintBO();
    implicationConstraint.setConditionAttribute(dictionary.conditionAttribute || "");
    implicationConstraint.setConditionValue(dictionary.conditionValue || "");
    implicationConstraint.setImplicationAttribute(dictionary.implicationAttribute || "");
    implicationConstraint.setImplicationValue(dictionary.implicationValue || "");
    return implicationConstraint;
  }
}
