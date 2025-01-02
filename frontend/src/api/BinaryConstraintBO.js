import BusinessObject from "./BusinessObject.js";

export default class BinaryConstraintBO extends BusinessObject {
    constructor(itemA, itemB, condition) {
        super();
        this.type = 'binary'; // Typ des Constraints
        this.itemA = itemA;   // Erstes Kleidungsstück oder Element
        this.itemB = itemB;   // Zweites Kleidungsstück oder Element
        this.condition = condition; // Bedingung für das Constraint
    }

    // Beispiel einer Methode, die überprüft, ob das Constraint erfüllt ist
    isValid() {
        // Hier könnten spezifische Logik zum Überprüfen der Bedingung implementiert werden
        // Beispiel: Wenn die Bedingung erfüllt ist, gibt die Methode 'true' zurück
        return this.condition(this.itemA, this.itemB);
    }

    // Beispiel für eine Methode zum Setzen oder Ändern der Bedingung
    setCondition(newCondition) {
        this.condition = newCondition;
    }

    // Eine Methode, die Informationen über das Constraint zurückgibt
    getInfo() {
        return `Binary constraint between ${this.itemA.name} and ${this.itemB.name} with condition: ${this.condition.toString()}`;
    }

    // Weitere spezifische Methoden, die in diesem Fall je nach Logik implementiert werden könnten
}
