import ConstraintBO from "./ConstraintBO";

/**
 * Represents a Cardinality Constraint.
 *
 * A CardinalityConstraint has:
 * - An object (object),
 * - A minimum count (minCount) and a maximum count (maxCount).
 */
export default class CardinalityConstraintBO extends ConstraintBO {
  /**
   * Constructs a CardinalityConstraintBO object.
   *
   * @param {Number} minCount - The minimum cardinality.
   * @param {Number} maxCount - The maximum cardinality.
   * @param {Object} object - The object the cardinality applies to.
   * @param {String} name - The name of the constraint.
   * @param {String} description - The description of the constraint.
   */
  constructor(
    minCount = 0,
    maxCount = 0,
    object = null,
    name = "",
    description = ""
  ) {
    super(name, description);
    this.minCount = minCount;
    this.maxCount = maxCount;
    this.object = object;
  }

  // Getter and setter for minCount
  getMinCount() {
    return this.minCount;
  }

  setMinCount(value) {
    this.minCount = value;
  }

  // Getter and setter for maxCount
  getMaxCount() {
    return this.maxCount;
  }

  setMaxCount(value) {
    this.maxCount = value;
  }

  // Getter and setter for object
  getObject() {
    return this.object;
  }

  setObject(value) {
    this.object = value;
  }

  // String representation of the object
  toString() {
    return `CardinalityConstraint: min=${this.getMinCount()}, max=${this.getMaxCount()}, object=${JSON.stringify(
      this.getObject()
    )}`;
  }

  /**
   * Converts a JSON structure into a CardinalityConstraintBO object.
   * @param {Object} dictionary - The JSON data describing the CardinalityConstraintBO.
   * @returns {CardinalityConstraintBO} - A new CardinalityConstraintBO object.
   */
  static fromJSON(dictionary = {}) {
    const cardinalityConstraint = new CardinalityConstraintBO();
    cardinalityConstraint.setMinCount(dictionary.minCount || 0);
    cardinalityConstraint.setMaxCount(dictionary.maxCount || 0);
    cardinalityConstraint.setObject(dictionary.object || null);
    return cardinalityConstraint;
  }
}
