import ConstraintBO from "./ConstraintBO";

/**
 * Repräsentiert eine wechselseitige Einschränkung (Mutex Constraint) zwischen Attributen und Werten zweier Objekte.
 */
export default class MutexConstraintBO extends ConstraintBO {
  /**
   * Konstruiert ein MutexConstraintBO-Objekt.
   *
   * @param {String} obj1Attribute - Das Attribut des ersten Objekts.
   * @param {String} obj1Value - Der Wert des Attributs des ersten Objekts.
   * @param {String} obj2Attribute - Das Attribut des zweiten Objekts.
   * @param {String} obj2Value - Der Wert des Attributs des zweiten Objekts.
   */
  constructor(obj1Attribute = "", obj1Value = "", obj2Attribute = "", obj2Value = "", name = "", beschreibung = "",) {
    super(name, beschreibung);
    this.obj1Attribute = obj1Attribute;
    this.obj1Value = obj1Value;
    this.obj2Attribute = obj2Attribute;
    this.obj2Value = obj2Value;
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
    return `MutexConstraint: ${this.getObj1Attribute()}=${this.getObj1Value()}, ${this.getObj2Attribute()}=${this.getObj2Value()}`;
  }

  /**
   * Wandelt eine JSON-Struktur in ein MutexConstraintBO-Objekt um.
   * @param {Object} dictionary - Die JSON-Daten, die das MutexConstraintBO beschreiben.
   * @returns {MutexConstraintBO} - Ein neues MutexConstraintBO-Objekt.
   */
  static fromJSON(dictionary = {}) {
    const mutexConstraint = new MutexConstraintBO();
    mutexConstraint.setObj1Attribute(dictionary.obj1Attribute || "");
    mutexConstraint.setObj1Value(dictionary.obj1Value || "");
    mutexConstraint.setObj2Attribute(dictionary.obj2Attribute || "");
    mutexConstraint.setObj2Value(dictionary.obj2Value || "");
    return mutexConstraint;
  }
}
