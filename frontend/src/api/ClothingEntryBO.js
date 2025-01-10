import BusinessObject from "./BusinessObject.js";

// Die Klasse ClothingEntry erbt von der BusinessObject-Klasse.
// Diese Klasse repräsentiert einen Eintrag für Kleidung mit Bezeichnung, Menge, Einheit, Farbe, Größe und Marke.
export default class ClothingEntryBO extends BusinessObject {
    // Der Konstruktor initialisiert eine neue Instanz der ClothingEntry-Klasse mit den übergebenen Parametern.
    constructor(designation, quantity, unit, color, size, brand) {
        super(); // Ruft den Konstruktor der übergeordneten Klasse (BusinessObject) auf.
        this.designation = designation; // Bezeichnung der Kleidung (z.B. T-Shirt, Hose).
        this.quantity = quantity; // Menge der Kleidungsstücke.
        this.unit = unit; // Einheit der Menge (z.B. Stück, Paar).
        this.color = color; // Farbe der Kleidung.
        this.size = size; // Größe der Kleidung (z.B. S, M, L, XL).
        this.brand = brand; // Marke der Kleidung.
    }

    // Methode zum Setzen der Bezeichnung der Kleidung.
    setDesignation(designation) {
        this.designation = designation;
    }

    // Methode zum Abrufen der Bezeichnung der Kleidung.
    getDesignation() {
        return this.designation;
    }

    // Methode zum Setzen der Menge der Kleidung.
    setQuantity(quantity) {
        this.quantity = quantity;
    }

    // Methode zum Abrufen der Menge der Kleidung.
    getQuantity() {
        return this.quantity;
    }

    // Methode zum Setzen der Einheit der Menge.
    setUnit(unit) {
        this.unit = unit;
    }

    // Methode zum Abrufen der Einheit der Menge.
    getUnit() {
        return this.unit;
    }

    // Methode zum Setzen der Farbe der Kleidung.
    setColor(color) {
        this.color = color;
    }

    // Methode zum Abrufen der Farbe der Kleidung.
    getColor() {
        return this.color;
    }

    // Methode zum Setzen der Größe der Kleidung.
    setSize(size) {
        this.size = size;
    }

    // Methode zum Abrufen der Größe der Kleidung.
    getSize() {
        return this.size;
    }

    // Methode zum Setzen der Marke der Kleidung.
    setBrand(brand) {
        this.brand = brand;
    }

    // Methode zum Abrufen der Marke der Kleidung.
    getBrand() {
        return this.brand;
    }

    // Statische Methode zum Erzeugen von ClothingEntry-Instanzen aus einem JSON-Array.
    static fromJSON(clothingEntries) {
        return clothingEntries.map(f => {
            // Erzeugt eine neue Instanz von ClothingEntry basierend auf den JSON-Daten.
            let clothingEntry = new clothingEntries(
                f.designation,
                f.quantity,
                f.unit,
                f.color,
                f.size,
                f.brand
            );
            clothingEntry.setId(f.id);  // ID direkt setzen
            return clothingEntry;
        });
    }
}
