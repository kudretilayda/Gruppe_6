import BusinessObject from "frontend/src/api/BusinessObject.js";


/**
 * Represents a generic constraint.
 *
 * A Constraint has a name and a description.
 */
export default class ConstraintBO extends BusinessObject {
  /**
   * Constructs a ConstraintBO object.
   */
  constructor() {
    super();
    this.constraintID = 0
  }

  getConstraintID() {
    return this.constraintID
  }

  setConstraintID(c_id) {
    this.constraintID = c_id
  }

  /**
   * Validates the constraint.
   * This method should be overridden in subclasses to implement specific validation logic.
   * @param {...*} args - Arguments specific to the validation.
   * @returns {boolean} - Validation result.
   */
  validate(...args) {
    throw new Error("Validate method must be implemented in a subclass.");
  }


  /**
   * Converts a JSON structure into a ConstraintBO object.
   * @param {Object} dictionary - The JSON data describing the ConstraintBO.
   * @returns {ConstraintBO} - A new ConstraintBO object.
   */
  static fromJSON(dictionary = {}) {
    const constraint = new ConstraintBO();
    constraint.setConstraintID(dictionary.constraintID || 0);
    return constraint;
  }
}
