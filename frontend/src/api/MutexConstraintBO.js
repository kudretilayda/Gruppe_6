import ConstraintBO from "./ConstraintBO";

/**
 * Repräsentiert eine wechselseitige Einschränkung (Mutex Constraint) zwischen zwei Objekten.
 */
export default class MutexConstraintBO extends ConstraintBO {
  /**
   * Konstruiert ein MutexConstraintBO-Objekt.
   *
   * @param {Object} obj1 - Das erste Objekt.
   * @param {Object} obj2 - Das zweite Objekt.
   * @param {String} name - Der Name der Einschränkung.
   * @param {String} beschreibung - Die Beschreibung der Einschränkung.
   */
  constructor(obj1 = null, obj2 = null, name = "", beschreibung = "") {
    super(name, beschreibung);
    this.obj1 = obj1;
    this.obj2 = obj2;
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
    return `MutexConstraint: obj1=${JSON.stringify(this.getObj1())}, obj2=${JSON.stringify(this.getObj2())}`;
  }

  /**
   * Wandelt eine JSON-Struktur in ein MutexConstraintBO-Objekt um.
   * @param {Object} dictionary - Die JSON-Daten, die das MutexConstraintBO beschreiben.
   * @returns {MutexConstraintBO} - Ein neues MutexConstraintBO-Objekt.
   */
  static fromJSON(dictionary = {}) {
    const mutexConstraint = new MutexConstraintBO();
    mutexConstraint.setObj1(dictionary.obj1 || null);
    mutexConstraint.setObj2(dictionary.obj2 || null);
    return mutexConstraint;
  }
}

