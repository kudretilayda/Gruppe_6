import BusinessObject from "./BusinessObject.js";

export default class CardinalityConstraintBO extends BusinessObject {
    constructor(min, max) {
        super();
        this.type = 'cardinality'; // Der Typ des Constraints
        this.min = min || 1;  // Minimale Anzahl von Elementen, die enthalten sein müssen
        this.max = max || Infinity; // Maximale Anzahl von Elementen, die enthalten sein können
    }

    // Methode, die überprüft, ob die Anzahl der Elemente im gegebenen Set mit den Kardinalitätsanforderungen übereinstimmt
    isValidSet(itemSet) {
        const itemCount = itemSet.length; // Anzahl der Elemente im Set
        return itemCount >= this.min && itemCount <= this.max;
    }

    // Methode, um zu prüfen, ob ein einzelnes Element im Set die Kardinalitätserfordernisse erfüllt
    isValidItem(item, itemSet) {
        // Hier könnte die Logik hinzukommen, wie ein einzelnes Item die Kardinalität beeinflusst
        // z.B., ob es die Anzahl der erlaubten Items überschreitet oder unterschreitet
        return this.isValidSet(itemSet);
    }

    // Eine Methode, die überprüft, ob das Constraint auf eine bestimmte Menge von Items angewendet werden kann
    checkCardinality(itemSet) {
        return this.isValidSet(itemSet);
    }

    // Eine Methode, um die Kardinalitätsanforderungen als String darzustellen
    toString() {
        return `Cardinality Constraint: Minimum ${this.min}, Maximum ${this.max}`;
    }

    // Eine Methode, um das Constraint in JSON zu serialisieren
    toJSON() {
        return {
            type: this.type,
            min: this.min,
            max: this.max,
        };
    }

    // Eine statische Methode, um aus einem JSON-Objekt ein CardinalityConstraintBO zu erstellen
    static fromJSON(json) {
        const constraint = new CardinalityConstraintBO(json.min, json.max);
        Object.setPrototypeOf(constraint, CardinalityConstraintBO.prototype);
        return constraint;
    }
}
