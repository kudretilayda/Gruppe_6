import BusinessObject from './BusinessObject.js'

/**
 * Repräsentiert einen Kleiderschrank
 */
export default class WardrobeBO extends BusinessObject {
    
    /** 
     * Konstruktor für einen Kleiderschrank
     * 
     * @param {String} awardrobe_name - Name des Kleiderschranks
     * @param {Number} aperson_id - ID des Besitzers
     */
    constructor(awardrobe_name, aperson_id) {
        super();
        this.wardrobe_name = awardrobe_name;
        this.person_id = aperson_id;
    }

    setWardrobeName(awardrobe_name) {
        this.wardrobe_name = awardrobe_name;
    }

    getWardrobeName() {
        return this.wardrobe_name;
    }

    setPersonId(aperson_id) {
        this.person_id = aperson_id;
    }

    getPersonId() {
        return this.person_id;
    }

    static fromJSON(wardrobes) {
        let result = [];

        if (Array.isArray(wardrobes)) {
            wardrobes.forEach((w) => {
                Object.setPrototypeOf(w, WardrobeBO.prototype);
                result.push(w);
            })
        } else {
            let w = wardrobes;
            Object.setPrototypeOf(w, WardrobeBO.prototype);
            result.push(w);
        }

        return result;
    }
}