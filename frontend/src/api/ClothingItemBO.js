import BusinessObject from "./BusinessObject.js";

/**
 * Repräsentiert ein Kleidungsstück, das sowohl als Einzelstück als auch als Sammlung verwaltet werden kann.
 */
export default class ClothingItemBO extends BusinessObject {
    /**
     * Konstruktor für ein Kleidungsstück
     *
     * @param {String} itemName - Name des Kleidungsstücks (z. B. "T-Shirt").
     * @param {Number} quantity - Anzahl der Kleidungsstücke.
     * @param {String} unit - Einheit der Menge (z. B. "Stück", "Paar").
     * @param {String} color - Farbe des Kleidungsstücks.
     * @param {String} size - Größe des Kleidungsstücks (z. B. "M", "L", "XL").
     * @param {String} brand - Marke des Kleidungsstücks.
     * @param {String} wardrobeId - ID des zugehörigen Kleiderschranks.
     * @param {String} typeId - ID des Kleidungstyps (z. B. "Hose", "Jacke").
     * @param {String} season - Saison, für die das Kleidungsstück gedacht ist (z. B. "Sommer").
     */
    constructor(itemName, quantity, unit, color, size, brand, wardrobeId, typeId, season) {
        super();
        this.itemName = itemName; // Name des Kleidungsstücks
        this.quantity = quantity || 0; // Menge der Kleidungsstücke (Standard: 0)
        this.unit = unit || "Stück"; // Einheit (Standard: "Stück")
        this.color = color; // Farbe des Kleidungsstücks
        this.size = size; // Größe des Kleidungsstücks
        this.brand = brand; // Marke des Kleidungsstücks
        this.wardrobeId = wardrobeId; // ID des zugehörigen Kleiderschranks
        this.typeId = typeId; // Typ-ID des Kleidungsstücks
        this.season = season; // Saison des Kleidungsstücks
    }

    // Getter und Setter für jedes Attribut
    setItemName(itemName) {
        this.itemName = itemName;
    }

    getItemName() {
        return this.itemName;
    }

    setQuantity(quantity) {
        this.quantity = quantity;
    }

    getQuantity() {
        return this.quantity;
    }

    setUnit(unit) {
        this.unit = unit;
    }

    getUnit() {
        return this.unit;
    }

    setColor(color) {
        this.color = color;
    }

    getColor() {
        return this.color;
    }

    setSize(size) {
        this.size = size;
    }

    getSize() {
        return this.size;
    }

    setBrand(brand) {
        this.brand = brand;
    }

    getBrand() {
        return this.brand;
    }

    setWardrobeId(wardrobeId) {
        this.wardrobeId = wardrobeId;
    }

    getWardrobeId() {
        return this.wardrobeId;
    }

    setTypeId(typeId) {
        this.typeId = typeId;
    }

    getTypeId() {
        return this.typeId;
    }

    setSeason(season) {
        this.season = season;
    }

    getSeason() {
        return this.season;
    }

    /**
     * Erstellt eine oder mehrere Instanzen von ClothingItemBO aus JSON-Daten.
     *
     * @param {Array|Object} items - JSON-Daten, die Kleidungsstücke repräsentieren.
     * @returns {Array} - Liste von ClothingItemBO-Instanzen.
     */
    static fromJSON(items) {
        let result = [];

        if (Array.isArray(items)) {
            items.forEach((i) => {
                result.push(
                    new ClothingItemBO(
                        i.itemName,
                        i.quantity,
                        i.unit,
                        i.color,
                        i.size,
                        i.brand,
                        i.wardrobeId,
                        i.typeId,
                        i.season
                    )
                );
            });
        } else {
            let i = items;
            result.push(
                new ClothingItemBO(
                    i.itemName,
                    i.quantity,
                    i.unit,
                    i.color,
                    i.size,
                    i.brand,
                    i.wardrobeId,
                    i.typeId,
                    i.season
                )
            );
        }

        return result;
    }
}
