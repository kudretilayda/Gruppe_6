import BusinessObject from "./BusinessObject.js";

// Die Klasse WardrobeBO erbt von der BusinessObject-Klasse.
// Diese Klasse repräsentiert einen digitalen Kleiderschrank.
export default class WardrobeBO extends BusinessObject {
    constructor(ownerId, clothingItems = []) {
        super();
        this.ownerId = ownerId; // Der Besitzer des Kleiderschranks
        this.clothingItems = clothingItems; // Liste der Kleidungsstücke
    }

    // Getter und Setter für ownerId
    getOwnerId() {
        return this.ownerId;
    }

    setOwnerId(ownerId) {
        this.ownerId = ownerId;
    }

    // Getter und Setter für clothingItems
    getClothingItems() {
        return this.clothingItems;
    }

    setClothingItems(clothingItems) {
        this.clothingItems = clothingItems;
    }

    // Statische Methode zur Konvertierung von JSON-Daten in WardrobeBO-Objekte
    static fromJSON(wardrobes) {
        let result = [];
        if (Array.isArray(wardrobes)) {
            wardrobes.forEach((w) => {
                Object.setPrototypeOf(w, WardrobeBO.prototype);
                result.push(w);
            });
        } else {
            let w = wardrobes;
            Object.setPrototypeOf(w, WardrobeBO.prototype);
            result.push(w);
        }
        return result;
    }
}
