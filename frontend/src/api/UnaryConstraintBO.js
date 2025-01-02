import ConstraintBO from './ConstraintBO.js'

export default class UnaryConstraintBO extends ConstraintBO {
  constructor(refObject) {
    super();
    this.refObject = refObject;  // Das Kleidungsstück, auf das die Einschränkung angewendet wird
  }

  // Überprüft, ob der Unary-Constraint gültig ist
  isValid() {
    // Beispiel-Logik: Ein T-Shirt kann nur einmal getragen werden
    return this.refObject.type !== "T-Shirt" || !this.refObject.isWorn;
  }

  static fromJSON(constraint) {
    let result = super.fromJSON(constraint);
    return result;
  }
}
