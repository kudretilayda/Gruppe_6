import BusinessObject from './BusinessObject.js';

/**
 * Repräsentiert einen Style
 */
export default class StyleBO extends BusinessObject {
    constructor(features = [], constraints = []) {
        super();
        this.features = features; // Array von Merkmalen
        this.constraints = constraints; // Array von Constraints
    }

    // Getter und Setter für Features
    getFeatures() {
        return this.features;
    }

    setFeatures(features) {
        this.features = features;
    }

    // Getter und Setter für Constraints
    getConstraints() {
        return this.constraints;
    }

    setConstraints(constraints) {
        this.constraints = constraints;
    }

    static fromJSON(styles) {
        let result = [];
        if (Array.isArray(styles)) {
            styles.forEach((s) => {
                Object.setPrototypeOf(s, StyleBO.prototype);
                result.push(s);
            });
        } else {
            let s = styles;
            Object.setPrototypeOf(s, StyleBO.prototype);
            result.push(s);
        }
        return result;
    }
}
