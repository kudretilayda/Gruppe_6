import ConstraintBO from './ConstraintBO.js'

export default class BinaryConstraintBO extends ConstraintBO {
  constructor(refObject1, refObject2) {
    super();
    this.refObject1 = refObject1;  // Erstes Kleidungsstück
    this.refObject2 = refObject2;  // Zweites Kleidungsstück
  }

  // Überprüft, ob der Binary-Constraint gültig ist
  isValid() {
    // Beispiel-Logik: Überprüft, ob die beiden Kleidungsstücke miteinander kombiniert werden können.
    return !(this.refObject1.type === "Hose" && this.refObject2.type === "Rock");
  }

  static fromJSON(constraint) {
    let result = super.fromJSON(constraint);
    return result;
  }
}
