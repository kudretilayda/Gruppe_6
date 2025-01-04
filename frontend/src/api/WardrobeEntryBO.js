import ClothingEntry from "./ClothingEntryBO";  // Falls es eine grundlegende Klasse für Kleidung gibt

// Die Klasse WardrobeEntryBO erbt von der ClothingEntry-Klasse.
// Diese Klasse repräsentiert einen Eintrag im Kleiderschrank und erweitert ClothingEntry um die Eigenschaft wardrobeId.
export default class WardrobeEntryBO extends ClothingEntry {
    // Der Konstruktor initialisiert eine neue Instanz der WardrobeEntryBO-Klasse mit den übergebenen Parametern.
    constructor(designation, quantity, unit, wardrobeId, color, size, brand) {
        super(designation, quantity, unit); // Ruft den Konstruktor der übergeordneten Klasse (ClothingEntry) auf.
        this.wardrobeId = wardrobeId; // ID des Kleiderschranks.
        this.color = color; // Farbe des Kleidungsstücks.
        this.size = size; // Größe des Kleidungsstücks.
        this.brand = brand; // Marke des Kleidungsstücks.
    }

    // Methode zum Abrufen der Kleiderschrank-ID.
    getWardrobeId() {
        return this.wardrobeId;
    }

    // Methode zum Setzen der Kleiderschrank-ID.
    setWardrobeId(wardrobeId) {
        this.wardrobeId = wardrobeId;
    }

    // Zusätzliche Getter und Setter für Farbe, Größe und Marke
    getColor() {
        return this.color;
    }

    setColor(color) {
        this.color = color;
    }

    getSize() {
        return this.size;
    }

    setSize(size) {
        this.size = size;
    }

    getBrand() {
        return this.brand;
    }

    setBrand(brand) {
        this.brand = brand;
    }

    // Statische Methode zum Erzeugen von WardrobeEntryBO-Instanzen aus JSON-Daten.
    static fromJSON(wardrobeEntries) {
        // Überprüft, ob wardrobeEntries ein Array ist. Wenn nicht, wird es in ein Array umgewandelt.
        if (!Array.isArray(wardrobeEntries)) {
            wardrobeEntries = [wardrobeEntries];
        }
        // Erzeugt eine neue Instanz von WardrobeEntryBO für jedes Element im Array.
        return wardrobeEntries.map(f => {
            let wardrobeEntry = new WardrobeEntryBO(
                f.designation,
                f.quantity,
                f.unit,
                f.wardrobe_id,
                f.color,
                f.size,
                f.brand
            );
            wardrobeEntry.setId(f.id);  // Setzt die ID direkt
            return wardrobeEntry;
        });
    }
}
