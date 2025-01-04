import BusinessObject from './BusinessObject.js'

export default class ConstraintBO extends BusinessObject {
  constructor() {
    super();  // Ruft den Konstruktor der Basisklasse BusinessObject auf
  }

  // Überprüft, ob der Constraint erfüllt ist
  // Diese Methode muss von den Unterklassen überschrieben werden
  isValid() {
    throw new Error("Methode 'isValid()' muss von der Unterklasse implementiert werden.");
  }

  static fromJSON(constraints) {
    let result = [];
    if (Array.isArray(constraints)) {
      constraints.forEach((c) => {
        Object.setPrototypeOf(c, ConstraintBO.prototype);
        result.push(c);
      });
    } else {
      let c = constraints;
      Object.setPrototypeOf(c, ConstraintBO.prototype);
      result.push(c);
    }
    return result;
  }
}
