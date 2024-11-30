import ConstraintBO from "./ConstraintBO";

/**
 * Repräsentiert eine Kardinalitätseinschränkung (Cardinality Constraint).
 *
 * Eine CardinalityConstraint besitzt:
 * - Zwei Objekte (obj1, obj2),
 * - Eine Mindestanzahl (minCount) und eine Höchstanzahl (maxCount).
 */
export default class CardinalityConstraintBO extends ConstraintBO {
  /**
   * Konstruiert ein CardinalityConstraintBO-Objekt.
   *
   * @param {Number} minCount - Minimale Kardinalität.
   * @param {Number} maxCount - Maximale Kardinalität.
   * @param {Object} obj1 - Erstes Objekt.
   * @param {Object} obj2 - Zweites Objekt.
   */
  constructor(
    minCount = 0,
    maxCount = 0,
    obj1 = null,
    obj2 = null,
    name = "",
    beschreibung = ""
  ) {
    super(name, beschreibung);
    this.minCount = minCount;
    this.maxCount = maxCount;
    this.obj1 = obj1;
    this.obj2 = obj2;
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

  // Getter und Setter für obj1
  getObj1() {
    return this.obj1;
  }

  setObj1(value) {
    this.obj1 = value;
  }

  // Getter und Setter für obj2
  getObj2() {
    return this.obj2;
  }

  setObj2(value) {
    this.obj2 = value;
  }

  // String-Darstellung des Objekts
  toString() {
    return `CardinalityConstraint: min=${this.getMinCount()}, max=${this.getMaxCount()}, obj1=${JSON.stringify(
      this.getObj1()
    )}, obj2=${JSON.stringify(this.getObj2())}`;
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
    cardinalityConstraint.setObj1(dictionary.obj1 || null);
    cardinalityConstraint.setObj2(dictionary.obj2 || null);
    return cardinalityConstraint;
  }
}
