import BusinessObject from "./BusinessObject.js";

export default class OutfitEntryBO extends BusinessObject {
    constructor(clothingItemId, sizeId, outfitId) {
        super();
        this.clothingItemId = clothingItemId;  // ID des Kleidungsstücks
        this.sizeId = sizeId;  // ID der Größe
        this.outfitId = outfitId;  // ID des Outfits
    }

    // Getter und Setter für jedes Attribut
    getClothingItemId() {
        return this.clothingItemId;
    }

    setClothingItemId(clothingItemId) {
        this.clothingItemId = clothingItemId;
    }

    getSizeId() {
        return this.sizeId;
    }

    setSizeId(sizeId) {
        this.sizeId = sizeId;
    }

    getOutfitId() {
        return this.outfitId;
    }

    setOutfitId(outfitId) {
        this.outfitId = outfitId;
    }

    static fromJSON(outfitEntries) {
        let result = [];
        if (Array.isArray(outfitEntries)) {
            outfitEntries.forEach((oe) => {
                Object.setPrototypeOf(oe, OutfitEntryBO.prototype);
                result.push(oe);
            });
        } else {
            let oe = outfitEntries;
            Object.setPrototypeOf(oe, OutfitEntryBO.prototype);
            result.push(oe);
        }
        return result;
    }
}
