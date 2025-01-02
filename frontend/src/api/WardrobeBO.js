import BusinessObject from "./BusinessObject.js"

// Die Klasse DigitalWardrobeBO erbt von der BusinessObject-Klasse.
// Diese Klasse repräsentiert ein digitales Kleiderschrank-Objekt.
export default class DigitalWardrobeBO extends BusinessObject {
    // Konstruktor, der den Konstruktor der übergeordneten Klasse (BusinessObject) aufruft.
    constructor() {
        super();
        this.clothes = [];  // Ein Array, das die Kleidung im digitalen Kleiderschrank speichert.
    }

    // Methode, um Kleidungsstücke hinzuzufügen.
    addClothing(clothingItem) {
        this.clothes.push(clothingItem);
    }

    // Methode, um ein Kleidungsstück zu entfernen.
    removeClothing(clothingItem) {
        this.clothes = this.clothes.filter(item => item !== clothingItem);
    }

    // Statische Methode zum Erzeugen von DigitalWardrobeBO-Instanzen aus JSON-Daten.
    static fromJSON(wardrobes) {
        let result = [];
        // Überprüft, ob wardrobes ein Array ist.
        if (Array.isArray(wardrobes)) {
            // Wenn wardrobes ein Array ist, iteriert durch jedes Element.
            wardrobes.forEach((w) => {
                // Setzt das Prototyp-Objekt des Elements auf DigitalWardrobeBO.
                Object.setPrototypeOf(w, DigitalWardrobeBO.prototype);
                result.push(w); // Fügt das Element zum Ergebnisarray hinzu.
            })
        } else {
            // Wenn wardrobes kein Array ist, behandelt es als singuläres Objekt.
            let w = wardrobes;
            // Setzt das Prototyp-Objekt des Objekts auf DigitalWardrobeBO.
            Object.setPrototypeOf(w, DigitalWardrobeBO.prototype);
            result.push(w); // Fügt das Objekt zum Ergebnisarray hinzu.
        }
        // Gibt das Ergebnisarray zurück.
        return result;
    }

    // Methode zum Filtern von Kleidung nach Kategorie (z.B. 'jackets', 'shirts').
    filterByCategory(category) {
        return this.clothes.filter(item => item.category === category);
    }
}
