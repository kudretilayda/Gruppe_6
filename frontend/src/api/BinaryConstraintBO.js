import ConstraintBO from "./ConstraintBO";

/**
 * Represents an object with conditions between two reference objects.
 */
export default class BinaryConstraintBO extends ConstraintBO {
  /**
   * Constructs a BinaryConstraintBO object.
   *
   * @param {any} object1 - Reference object 1.
   * @param {any} object2 - Reference object 2.
   * @param {String} condition - The condition between the two objects.
   * @param {String} name - The name of the constraint.
   * @param {String} description - A description of the constraint.
   */
  constructor(
    object1 = null,
    object2 = null,
    condition = "",
    name = "",
    description = ""
  ) {
    super(name, description);
    this.object1 = object1;
    this.object2 = object2;
    this.condition = condition;
  }

  // Getter and setter for object1
  getObject1() {
    return this.object1;
  }

  setObject1(value) {
    this.object1 = value;
  }

  // Getter and setter for object2
  getObject2() {
    return this.object2;
  }

  setObject2(value) {
    this.object2 = value;
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
    return `BinaryConstraint: ${JSON.stringify(
      this.getObject1()
    )}, ${JSON.stringify(this.getObject2())}, ${this.getCondition()}`;
  }

  /**
   * Converts a JSON structure into a BinaryConstraintBO object.
   * @param {Object} dictionary - The JSON data describing the BinaryConstraintBO.
   * @returns {BinaryConstraintBO} - A new BinaryConstraintBO object.
   */
  static fromJSON(dictionary = {}) {
    const binaryconstraint = new BinaryConstraintBO();
    binaryconstraint.setObject1(dictionary.object1 || null);
    binaryconstraint.setObject2(dictionary.object2 || null);
    binaryconstraint.setCondition(dictionary.condition || "");
    return binaryconstraint;
  }
}
