import BusinessObject from "./BusinessObject";

/**
 * Represents a clothing type (e.g., shirt, pants, dress).
 */
export default class ClothingTypeBO extends BusinessObject {
  /**
   * Constructs a ClothingTypeBO object.
   *
   * @param {Number} aId - The ID of the clothing type.
   * @param {String} aName - The name of the clothing type.
   * @param {String} aUsage - Occasions or purposes for this clothing type.
   */
  constructor(aId = 0, aName = "", aUsage = "") {
    super();
    this.id = aId;
    this.name = aName;
    this.usage = aUsage;
  }

  // Getter and setter for name
  getName() {
    return this.name;
  }

  setName(value) {
    this.name = value;
  }

  // Getter and setter for usage
  getUsage() {
    return this.usage;
  }

  setUsage(value) {
    this.usage = value;
  }

  // String representation of the object
  toString() {
    return `Clothing Type: ${this.getId()}, Name: ${this.getName()}, Usage: ${this.getUsage()}`;
  }

  /**
   * Converts a JSON structure into a ClothingTypeBO object.
   * @param {Object} dictionary - The JSON data describing the ClothingTypeBO.
   * @returns {ClothingTypeBO} - A new ClothingTypeBO object.
   */
  static fromJSON(dictionary = {}) {
    const clothingType = new ClothingTypeBO();
    clothingType.setId(dictionary.id || 0); // Inherited from BusinessObject.
    clothingType.setName(dictionary.name || "");
    clothingType.setUsage(dictionary.usage || "");
    return clothingType;
  }
}