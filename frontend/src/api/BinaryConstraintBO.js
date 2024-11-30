import ConstraintBO from "./ConstraintBO";

/**
 * Repräsentiert ein Objekt mit Bedingungen zwischen zwei Bezugsobjekten.
 */
export default class BinaryConstraintBO extends ConstraintBO {
  /**
   * Konstruiert ein BinaryConstraintBO-Objekt.
   *
   * @param {any} obj1 - Bezugsobjekt 1.
   * @param {any} obj2 - Bezugsobjekt 2.
   * @param {String} bedingung - Die Bedingung zwischen den beiden Objekten.
   */
  constructor(
    obj1 = null,
    obj2 = null,
    bedingung = "",
    name = "",
    beschreibung = ""
  ) {
    super(name, beschreibung);
    this.obj1 = obj1;
    this.obj2 = obj2;
    this.bedingung = bedingung;
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

  // Getter und Setter für bedingung
  getBedingung() {
    return this.bedingung;
  }

  setBedingung(value) {
    this.bedingung = value;
  }

  // String-Darstellung des Objekts
  toString() {
    return `BinaryConstraint: ${JSON.stringify(
      this.getObj1()
    )}, ${JSON.stringify(this.getObj2())}, ${this.getBedingung()}`;
  }

  /**
   * Wandelt eine JSON-Struktur in ein ConditionBO-Objekt um.
   * @param {Object} dictionary - Die JSON-Daten, die das ConditionBO beschreiben.
   * @returns {ConditionBO} - Ein neues ConditionBO-Objekt.
   */
  static fromJSON(dictionary = {}) {
    const binaryconstraint = new BinaryConstraintBO();
    binaryconstraint.setObj1(dictionary.obj1 || null);
    binaryconstraint.setObj2(dictionary.obj2 || null);
    binaryconstraint.setBedingung(dictionary.bedingung || "");
    return binaryconstraint;
  }
}
