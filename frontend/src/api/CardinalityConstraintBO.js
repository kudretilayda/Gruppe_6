import ConstraintBO from "./ConstraintBO.js";

export default class CardinalityConstraintBO extends ConstraintBO {
    constructor(min, max) {
        super();
        this.min = min;  // Minimum Anzahl
        this.max = max;  // Maximum Anzahl
    }

    // Getter und Setter für jedes Attribut
    getMin() {
        return this.min;
    }

    setMin(min) {
        this.min = min;
    }

    getMax() {
        return this.max;
    }

    setMax(max) {
        this.max = max;
    }

    static fromJSON(cardinalityConstraints) {
        let result = [];
        if (Array.isArray(cardinalityConstraints)) {
            cardinalityConstraints.forEach((cc) => {
                Object.setPrototypeOf(cc, CardinalityConstraintBO.prototype);
                result.push(cc);
            });
        } else {
            let cc = cardinalityConstraints;
            Object.setPrototypeOf(cc, CardinalityConstraintBO.prototype);
            result.push(cc);
        }
        return result;
    }
}
