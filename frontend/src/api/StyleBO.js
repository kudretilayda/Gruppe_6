import BusinessObject from './BusinessObject.js'

/**
 * Repräsentiert ein Style-Objekt
 */
export default class StyleBO extends BusinessObject {
    
    /** 
     * Konstruktor für ein Style-Objekt
     * 
     * @param {String} astyle_name - Name des Styles
     * @param {String} adescription - Beschreibung des Styles 
     * @param {Array} aConstraints - Array von Constraint-Objekten
     */
    constructor(astyle_name, adescription, aConstraints) {
        super();
        this.style_name = astyle_name;
        this.description = adescription;
        this.constraints = aConstraints;
    }

    setStyleName(astyle_name) {
        this.style_name = astyle_name;
    }

    getStyleName() {
        return this.style_name;
    }

    setDescription(adescription) {
        this.description = adescription;
    }

    getDescription() {
        return this.description;
    }

    setConstraints(aConstraints) {
        this.constraints = aConstraints;
    }

    getConstraints() {
        return this.constraints;
    }

    static fromJSON(styles) {
        let result = [];

        if (Array.isArray(styles)) {
            styles.forEach((s) => {
                Object.setPrototypeOf(s, StyleBO.prototype);
                result.push(s);
            })
        } else {
            let s = styles;
            Object.setPrototypeOf(s, StyleBO.prototype);
            result.push(s);
        }

        return result;
    }
}