import BusinessObject from './BusinessObject.js'

/**
 * Repräsentiert ein Outfit-Objekt
 */
export default class OutfitBO extends BusinessObject {
    
    /** 
     * Konstruktor für ein Outfit-Objekt
     * 
     * @param {String} aoutfit_name - Name des Outfits
     * @param {Number} astyle_id - ID des zugehörigen Styles
     * @param {Array} aclothing_items - Zugehörige Kleidungsstücke
     */
    constructor(aoutfit_name, astyle_id, aclothing_items) {
        super();
        this.outfit_name = aoutfit_name;
        this.style_id = astyle_id;
        this.clothing_items = aclothing_items;
    }

    setOutfitName(aoutfit_name) {
        this.outfit_name = aoutfit_name;
    }

    getOutfitName() {
        return this.outfit_name;
    }

    setStyleId(astyle_id) {
        this.style_id = astyle_id;
    }

    getStyleId() {
        return this.style_id;
    }

    setClothingItems(aclothing_items) {
        this.clothing_items = aclothing_items;
    }

    getClothingItems() {
        return this.clothing_items;
    }

    static fromJSON(outfits) {
        let result = [];

        if (Array.isArray(outfits)) {
            outfits.forEach((o) => {
                Object.setPrototypeOf(o, OutfitBO.prototype);
                result.push(o);
            })
        } else {
            let o = outfits;
            Object.setPrototypeOf(o, OutfitBO.prototype);
            result.push(o);
        }

        return result;
    }
}