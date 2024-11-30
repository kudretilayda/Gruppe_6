import ConstraintBO from "./ConstraintBO";

/**
 * Repräsentiert eine Kardinalitätseinschränkung (Cardinality Constraint).
 *
 * Eine CardinalityConstraint besitzt:
 * - Ein Objekt (object),
 * - Eine Mindestanzahl (minCount) und eine Höchstanzahl (maxCount).
 */
export default class CardinalityConstraintBO extends ConstraintBO {
  /**
   * Konstruiert ein CardinalityConstraintBO-Objekt.
   *
   * @param {Number} minCount - Minimale Kardinalität.
   * @param {Number} maxCount - Maximale Kardinalität.
   * @param {Object} object - Das Objekt, auf das sich die Kardinalität bezieht.
   * @param {String} name - Der Name der Einschränkung.
   * @param {String} beschreibung - Die Beschreibung der Einschränkung.
   */
  constructor(
    minCount = 0,
    maxCount = 0,
    object = null,
    name = "",
    beschreibung = ""
  ) {
    super(name, beschreibung);
    this.minCount = minCount;
    this.maxCount = maxCount;
    this.object = object;
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

  // Getter und Setter für object
  getObject() {
    return this.object;
  }

  setObject(value) {
    this.object = value;
  }

  // String-Darstellung des Objekts
  toString() {
    return `CardinalityConstraint: min=${this.getMinCount()}, max=${this.getMaxCount()}, object=${JSON.stringify(
      this.getObject()
    )}`;
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
    cardinalityConstraint.setObject(dictionary.object || null);
    return cardinalityConstraint;
  }
}

