import BusinessObject from "./BusinessObject.js";

// Die Klasse WardrobeBO erbt von der BusinessObject-Klasse.
// Diese Klasse repräsentiert einen digitalen Kleiderschrank.
export default class WardrobeBO extends BusinessObject {
    constructor(ownerId, clothingItems = []) {
        super();
        this.owner = ownerId; // Der Besitzer des Kleiderschranks
        this.content = clothingItems; // Inhalt des Kleiderschranks (Kleidungsstücke)
    }

    // Getter und Setter für ownerId
    getOwnerId() {
        return this.owner;
    }

    setOwnerId(ownerId) {
        this.owner = ownerId;
    }

    // Getter und Setter für Content
    getContent() {
        return this.content;
    }

    setContent(clothingItems) {
        this.content = clothingItems; // Korrigiert, damit content richtig gesetzt wird
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
