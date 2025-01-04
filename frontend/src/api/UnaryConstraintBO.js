import ConstraintBO from "./ConstraintBO.js";

export default class UnaryConstraintBO extends ConstraintBO {
    constructor(referenceObject) {
        super();
        this.referenceObject = referenceObject; // Das referenzierte Objekt
    }

    // Getter und Setter für jedes Attribut
    getReferenceObject() {
        return this.referenceObject;
    }

    setReferenceObject(referenceObject) {
        this.referenceObject = referenceObject;
    }

    static fromJSON(unaryConstraints) {
        let result = [];
        if (Array.isArray(unaryConstraints)) {
            unaryConstraints.forEach((uc) => {
                Object.setPrototypeOf(uc, UnaryConstraintBO.prototype);
                result.push(uc);
            });
        } else {
            let uc = unaryConstraints;
            Object.setPrototypeOf(uc, UnaryConstraintBO.prototype);
            result.push(uc);
        }
        return result;
    }
}
