import BusinessObject from './BusinessObject.js'

/**
 * Repräsentiert ein Kleidungsstück
 */
export default class ClothingItemBO extends BusinessObject {
    
    /** 
     * Konstruktor für ein Kleidungsstück
     * 
     * @param {String} aitem_name - Name des Kleidungsstücks
     * @param {String} awardrobe_id - ID des zugehörigen Kleiderschranks
     * @param {String} atype_id - ID des Kleidungstyps
     * @param {String} acolor - Farbe des Kleidungsstücks
     * @param {String} aseason - Saison des Kleidungsstücks
     */
    constructor(aitem_name, awardrobe_id, atype_id, acolor, aseason) {
        super();
        this.item_name = aitem_name;
        this.wardrobe_id = awardrobe_id;
        this.type_id = atype_id;
        this.color = acolor;
        this.season = aseason;
    }

    setItemName(aitem_name) {
        this.item_name = aitem_name;
    }

    getItemName() {
        return this.item_name;
    }

    setWardrobeId(awardrobe_id) {
        this.wardrobe_id = awardrobe_id;
    }

    getWardrobeId() {
        return this.wardrobe_id;
    }

    setTypeId(atype_id) {
        this.type_id = atype_id;
    }

    getTypeId() {
        return this.type_id;
    }

    setColor(acolor) {
        this.color = acolor;
    }

    getColor() {
        return this.color;
    }

    setSeason(aseason) {
        this.season = aseason;
    }

    getSeason() {
        return this.season;
    }

    static fromJSON(items) {
        let result = [];

        if (Array.isArray(items)) {
            items.forEach((i) => {
                Object.setPrototypeOf(i, ClothingItemBO.prototype);
                result.push(i);
            })
        } else {
            let i = items;
            Object.setPrototypeOf(i, ClothingItemBO.prototype);
            result.push(i);
        }

        return result;
    }
}