import ConstraintBO from "./ConstraintBO.js";

export default class BinaryConstraintBO extends ConstraintBO {
    constructor(referenceObject1, referenceObject2) {
        super();
        this.referenceObject1 = referenceObject1; // Erstes Referenzobjekt
        this.referenceObject2 = referenceObject2; // Zweites Referenzobjekt
    }

    // Getter und Setter für jedes Attribut
    getReferenceObject1() {
        return this.referenceObject1;
    }

    setReferenceObject1(referenceObject1) {
        this.referenceObject1 = referenceObject1;
    }

    getReferenceObject2() {
        return this.referenceObject2;
    }

    setReferenceObject2(referenceObject2) {
        this.referenceObject2 = referenceObject2;
    }

    static fromJSON(binaryConstraints) {
        let result = [];
        if (Array.isArray(binaryConstraints)) {
            binaryConstraints.forEach((bc) => {
                Object.setPrototypeOf(bc, BinaryConstraintBO.prototype);
                result.push(bc);
            });
        } else {
            let bc = binaryConstraints;
            Object.setPrototypeOf(bc, BinaryConstraintBO.prototype);
            result.push(bc);
        }
        return result;
    }
}
