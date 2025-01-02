import ConstraintBO from "./ConstraintBO";

/**
 * Represents a Mutex Constraint between two objects.
 */
export default class MutexConstraintBO extends ConstraintBO {
  /**
   * Constructs a MutexConstraintBO object.
   *
   * @param {Object} object1 - The first object.
   * @param {Object} object2 - The second object.
   * @param {String} name - The name of the constraint.
   * @param {String} description - The description of the constraint.
   */
  constructor(object1 = null, object2 = null, name = "", description = "") {
    super(name, description);
    this.object1 = object1;
    this.object2 = object2;
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

  // String representation of the object
  toString() {
    return `MutexConstraint: object1=${JSON.stringify(this.getObject1())}, object2=${JSON.stringify(this.getObject2())}`;
  }

  /**
   * Converts a JSON structure into a MutexConstraintBO object.
   * @param {Object} dictionary - The JSON data describing the MutexConstraintBO.
   * @returns {MutexConstraintBO} - A new MutexConstraintBO object.
   */
  static fromJSON(dictionary = {}) {
    const mutexConstraint = new MutexConstraintBO();
    mutexConstraint.setObject1(dictionary.object1 || null);
    mutexConstraint.setObject2(dictionary.object2 || null);
    return mutexConstraint;
  }
}
