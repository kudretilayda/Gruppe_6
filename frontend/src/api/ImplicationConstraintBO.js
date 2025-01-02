import ConstraintBO from "./ConstraintBO";

/**
 * Represents an Implication Constraint.
 *
 * An ImplicationConstraint has a condition and an implication.
 */
export default class ImplicationConstraintBO extends ConstraintBO {
  /**
   * Constructs an ImplicationConstraintBO object.
   *
   * @param {Object} condition - The condition.
   * @param {Object} implication - The implication.
   * @param {String} name - The name of the constraint.
   * @param {String} description - The description of the constraint.
   */
  constructor(
    condition = null,
    implication = null,
    name = "",
    description = ""
  ) {
    super(name, description);
    this.condition = condition;
    this.implication = implication;
  }

  // Getter and setter for condition
  getCondition() {
    return this.condition;
  }

  setCondition(value) {
    this.condition = value;
  }

  // Getter and setter for implication
  getImplication() {
    return this.implication;
  }

  setImplication(value) {
    this.implication = value;
  }

  // String representation of the object
  toString() {
    return `ImplicationConstraint: ${JSON.stringify(this.getCondition())} -> ${JSON.stringify(this.getImplication())}`;
  }

  /**
   * Converts a JSON structure into an ImplicationConstraintBO object.
   * @param {Object} dictionary - The JSON data describing the ImplicationConstraintBO.
   * @returns {ImplicationConstraintBO} - A new ImplicationConstraintBO object.
   */
  static fromJSON(dictionary = {}) {
    const implicationConstraint = new ImplicationConstraintBO();
    implicationConstraint.setCondition(dictionary.condition || null);
    implicationConstraint.setImplication(dictionary.implication || null);
    return implicationConstraint;
  }
}
