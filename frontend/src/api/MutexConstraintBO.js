import ConstraintBO from "./ConstraintBO.js";

export default class MutexConstraintBO extends ConstraintBO {
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

    static fromJSON(mutexConstraints) {
        let result = [];
        if (Array.isArray(mutexConstraints)) {
            mutexConstraints.forEach((mc) => {
                Object.setPrototypeOf(mc, MutexConstraintBO.prototype);
                result.push(mc);
            });
        } else {
            let mc = mutexConstraints;
            Object.setPrototypeOf(mc, MutexConstraintBO.prototype);
            result.push(mc);
        }
        return result;
    }
}
