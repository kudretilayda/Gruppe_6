export default class BusinessObject {
    constructor() {
        this.id = 0
    }

    /**
     * Sets the ID of this BusinessObject.
     * @param {*} aId - the new ID of this BusinessObject
     */

    setID(aId) {
        this.id = aId
    }

    getID() {
        return this.id
    }

    toString() {
        let result = '';
        for (let prop in this) {
            result += prop + ': ' + this[prop] + ' ';
        }
        return result;
    }
}