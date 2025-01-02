import BusinessObject from "./BusinessObject.js";

export default class ClothingItemEntryBO extends BusinessObject {
    constructor(clothingItem) {
        super();
        this.clothingItem = clothingItem;
    }

    // Methode, die das Kleidungsstück zur Sammlung hinzufügt
    addClothingItem(newClothingItem) {
        this.clothingItem.push(newClothingItem);
    }

    // Methode zur Darstellung des Eintrags als String
    toString() {
        return `Clothing Item Entry: ${this.clothingItem.toString()}`;
    }
}
