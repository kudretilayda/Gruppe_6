import ConstraintBO from "./ConstraintBO";

/**
 * Represents a unary constraint.
 */
export default class UnaryConstraintBO extends ConstraintBO {
  /**
   * Constructs a UnaryConstraintBO object.
   *
   * @param {any} referenceObject - The reference object the constraint refers to.
   * @param {String} condition - The condition of the constraint.
   */
  constructor(referenceObject = null, condition = "", name = "", description = "") {
    super(name, description);
    this.referenceObject = referenceObject;
    this.condition = condition;
  }

  // Getter and setter for referenceObject
  getReferenceObject() {
    return this.referenceObject;
  }

  setReferenceObject(value) {
    this.referenceObject = value;
  }

  // Getter and setter for condition
  getCondition() {
    return this.condition;
  }

  setCondition(value) {
    this.condition = value;
  }

  // String representation of the object
  toString() {
    return `UnaryConstraint: ${JSON.stringify(this.getReferenceObject())}, ${this.getCondition()}`;
  }

  /**
   * Converts a JSON structure into a UnaryConstraintBO object.
   * @param {Object} dictionary - The JSON data describing the UnaryConstraintBO.
   * @returns {UnaryConstraintBO} - A new UnaryConstraintBO object.
   */
  static fromJSON(dictionary = {}) {
    const unaryConstraint = new UnaryConstraintBO();
    unaryConstraint.setReferenceObject(dictionary.referenceObject || null);
    unaryConstraint.setCondition(dictionary.condition || "");
    return unaryConstraint;
  }
}
