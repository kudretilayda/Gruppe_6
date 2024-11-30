import ConstraintBO from "./ConstraintBO";

/**
 * Repräsentiert ein Objekt mit Bedingungen zwischen zwei Bezugsobjekten.
 */
export default class BinaryConstraintBO extends ConstraintBO {
  /**
   * Konstruiert ein BinaryConstraintBO-Objekt.
   *
   * @param {any} object1 - Bezugsobjekt 1.
   * @param {any} object2 - Bezugsobjekt 2.
   * @param {String} bedingung - Die Bedingung zwischen den beiden Objekten.
   */
  constructor(
    object1 = null,
    object2 = null,
    bedingung = "",
    name = "",
    beschreibung = ""
  ) {
    super(name, beschreibung);
    this.object1 = object1;
    this.object2 = object2;
    this.bedingung = bedingung;
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
      this.getObject1()
    )}, ${JSON.stringify(this.getObject2())}, ${this.getBedingung()}`;
  }

  /**
   * Wandelt eine JSON-Struktur in ein ConditionBO-Objekt um.
   * @param {Object} dictionary - Die JSON-Daten, die das ConditionBO beschreiben.
   * @returns {ConditionBO} - Ein neues ConditionBO-Objekt.
   */
  static fromJSON(dictionary = {}) {
    const binaryconstraint = new BinaryConstraintBO();
    binaryconstraint.setObject1(dictionary.object1 || null);
    binaryconstraint.setObject2(dictionary.object2 || null);
    binaryconstraint.setBedingung(dictionary.bedingung || "");
    return binaryconstraint;
  }
}

