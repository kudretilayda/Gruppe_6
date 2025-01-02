import BusinessObject from "./BusinessObject";

/**
 * Represents a generic constraint.
 *
 * A Constraint has a name and a description.
 */
export default class ConstraintBO extends BusinessObject {
  /**
   * Constructs a ConstraintBO object.
   *
   * @param {String} name - The name of the constraint.
   * @param {String} description - The description of the constraint.
   */
  constructor(name = "", description = "") {
    super();
    this.name = name;
    this.description = description;
  }

  // Getter and setter for name
  getName() {
    return this.name;
  }

  setName(value) {
    this.name = value;
  }

  // Getter and setter for description
  getDescription() {
    return this.description;
  }

  setDescription(value) {
    this.description = value;
  }

  // String representation of the object
  toString() {
    return `Constraint: ${this.getName()}, Description: ${this.getDescription()}`;
  }

  /**
   * Converts a JSON structure into a ConstraintBO object.
   * @param {Object} dictionary - The JSON data describing the ConstraintBO.
   * @returns {ConstraintBO} - A new ConstraintBO object.
   */
  static fromJSON(dictionary = {}) {
    const constraint = new ConstraintBO();
    constraint.setName(dictionary.name || "");
    constraint.setDescription(dictionary.description || "");
    return constraint;
  }
}
