import BusinessObject from './BusinessObject.js'

/**
 * Repräsentiert einen Kleidungstyp
 */
export default class ClothingTypeBO extends BusinessObject {
    
    /** 
     * Konstruktor für einen Kleidungstyp
     * 
     * @param {String} atype_name - Name des Kleidungstyps
     * @param {String} atype_description - Beschreibung des Kleidungstyps
     * @param {String} acategory - Kategorie des Kleidungstyps
     */
    constructor(atype_name, atype_description, acategory) {
        super();
        this.type_name = atype_name;
        this.type_description = atype_description;
        this.category = acategory;
    }

    setTypeName(atype_name) {
        this.type_name = atype_name;
    }

    getTypeName() {
        return this.type_name;
    }

    setTypeDescription(atype_description) {
        this.type_description = atype_description;
    }

    getTypeDescription() {
        return this.type_description;
    }

    setCategory(acategory) {
        this.category = acategory;
    }

    getCategory() {
        return this.category;
    }

    static fromJSON(types) {
        let result = [];

        if (Array.isArray(types)) {
            types.forEach((t) => {
                Object.setPrototypeOf(t, ClothingTypeBO.prototype);
                result.push(t);
            })
        } else {
            let t = types;
            Object.setPrototypeOf(t, ClothingTypeBO.prototype);
            result.push(t);
        }

        return result;
    }
}