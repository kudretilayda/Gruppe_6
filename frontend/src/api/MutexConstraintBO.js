import ConstraintBO from "./ConstraintBO";

/**
 * Repräsentiert eine wechselseitige Einschränkung (Mutex Constraint) zwischen zwei Objekten.
 */
export default class MutexConstraintBO extends ConstraintBO {
  /**
   * Konstruiert ein MutexConstraintBO-Objekt.
   *
   * @param {Object} object1 - Das erste Objekt.
   * @param {Object} object2 - Das zweite Objekt.
   * @param {String} name - Der Name der Einschränkung.
   * @param {String} beschreibung - Die Beschreibung der Einschränkung.
   */
  constructor(object1 = null, object2 = null, name = "", beschreibung = "") {
    super(name, beschreibung);
    this.object1 = object1;
    this.object2 = object2;
  }

  // Getter und Setter für object1
  getObject1() {
    return this.object1;
  }

  setObject1(value) {
    this.object1 = value;
  }

  // Getter und Setter für object2
  getObject2() {
    return this.object2;
  }

  setObject2(value) {
    this.object2 = value;
  }

  // String-Darstellung des Objekts
  toString() {
    return `MutexConstraint: object1=${JSON.stringify(this.getObject1())}, object2=${JSON.stringify(this.getObject2())}`;
  }

  /**
   * Wandelt eine JSON-Struktur in ein MutexConstraintBO-Objekt um.
   * @param {Object} dictionary - Die JSON-Daten, die das MutexConstraintBO beschreiben.
   * @returns {MutexConstraintBO} - Ein neues MutexConstraintBO-Objekt.
   */
  static fromJSON(dictionary = {}) {
    const mutexConstraint = new MutexConstraintBO();
    mutexConstraint.setObject1(dictionary.object1 || null);
    mutexConstraint.setObject2(dictionary.object2 || null);
    return mutexConstraint;
  }
}


