import ConstraintBO from "./ConstraintBO";

/**
 * Repräsentiert eine Kardinalitätseinschränkung (Cardinality Constraint).
 *
 * Eine CardinalityConstraint besitzt:
 * - Zwei Attribute (obj1Attribute, obj2Attribute),
 * - Zwei Werte (obj1Value, obj2Value),
 * - Eine Mindestanzahl (minCount) und eine Höchstanzahl (maxCount),
 * - Eine Bedingung zur Bewertung.
 */
export default class CardinalityConstraintBO extends ConstraintBO {
  /**
   * Konstruiert ein CardinalityConstraintBO-Objekt.
   *
   * @param {Number} minCount - Minimale Kardinalität.
   * @param {Number} maxCount - Maximale Kardinalität.
   * @param {String} obj1Attribute - Das Attribut des ersten Objekts.
   * @param {String} obj1Value - Der Wert des Attributs des ersten Objekts.
   * @param {String} obj2Attribute - Das Attribut des zweiten Objekts.
   * @param {String} obj2Value - Der Wert des Attributs des zweiten Objekts.
   */
  constructor(
    minCount = 0,
    maxCount = 0,
    obj1Attribute = "",
    obj1Value = "",
    obj2Attribute = "",
    obj2Value = "",
    name = "",
    beschreibung = "",
  ) {
    super(name, beschreibung);
    this.minCount = minCount;
    this.maxCount = maxCount;
    this.obj1Attribute = obj1Attribute;
    this.obj1Value = obj1Value;
    this.obj2Attribute = obj2Attribute;
    this.obj2Value = obj2Value;
  }

  // Getter und Setter für minCount
  getMinCount() {
    return this.minCount;
  }

  setMinCount(value) {
    this.minCount = value;
  }

  // Getter und Setter für maxCount
  getMaxCount() {
    return this.maxCount;
  }

  setMaxCount(value) {
    this.maxCount = value;
  }

  // Getter und Setter für obj1Attribute
  getObj1Attribute() {
    return this.obj1Attribute;
  }

  setObj1Attribute(value) {
    this.obj1Attribute = value;
  }

  // Getter und Setter für obj1Value
  getObj1Value() {
    return this.obj1Value;
  }

  setObj1Value(value) {
    this.obj1Value = value;
  }

  // Getter und Setter für obj2Attribute
  getObj2Attribute() {
    return this.obj2Attribute;
  }

  setObj2Attribute(value) {
    this.obj2Attribute = value;
  }

  // Getter und Setter für obj2Value
  getObj2Value() {
    return this.obj2Value;
  }

  setObj2Value(value) {
    this.obj2Value = value;
  }

  // String-Darstellung des Objekts
  toString() {
    return `CardinalityConstraint: min=${this.getMinCount()}, max=${this.getMaxCount()}, ${this.getObj1Attribute()}=${this.getObj1Value()}, ${this.getObj2Attribute()}=${this.getObj2Value()}`;
  }

  /**
   * Wandelt eine JSON-Struktur in ein CardinalityConstraintBO-Objekt um.
   * @param {Object} dictionary - Die JSON-Daten, die das CardinalityConstraintBO beschreiben.
   * @returns {CardinalityConstraintBO} - Ein neues CardinalityConstraintBO-Objekt.
   */
  static fromJSON(dictionary = {}) {
    const cardinalityConstraint = new CardinalityConstraintBO();
    cardinalityConstraint.setMinCount(dictionary.minCount || 0);
    cardinalityConstraint.setMaxCount(dictionary.maxCount || 0);
    cardinalityConstraint.setObj1Attribute(dictionary.obj1Attribute || "");
    cardinalityConstraint.setObj1Value(dictionary.obj1Value || "");
    cardinalityConstraint.setObj2Attribute(dictionary.obj2Attribute || "");
    cardinalityConstraint.setObj2Value(dictionary.obj2Value || "");
    return cardinalityConstraint;
  }
}
