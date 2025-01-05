import BusinessObject from "./BusinessObject.js";

export default class ClothingTypeBO extends BusinessObject {
    constructor(name, usage) {
        super();
        this.name = name; // Bezeichnung (z.B. Hemd, Hose)
        this.usage = usage; // Verwendung (z.B. formal, casual)
    }

    // Getter und Setter für jedes Attribut
    getName() {
        return this.name;
    }

    setName(name) {
        this.name = name;
    }

    getUsage() {
        return this.usage;
    }

    setUsage(usage) {
        this.usage = usage;
    }

    static fromJSON(clothingTypes) {
        let result = [];
        if (Array.isArray(clothingTypes)) {
            clothingTypes.forEach((ct) => {
                Object.setPrototypeOf(ct, ClothingTypeBO.prototype);
                result.push(ct);
            });
        } else {
            let ct = clothingTypes;
            Object.setPrototypeOf(ct, ClothingTypeBO.prototype);
            result.push(ct);
        }
        return result;
    }
}
