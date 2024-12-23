import BusinessObject from "./BusinessObject";

/**
 * Represents a clothing item object.
 */
export default class ClothingItemBO extends BusinessObject {
  /**
   * Constructs a ClothingItemBO object.
   *
   * @param {Number} aClothingItemId - The ID of the clothing item.
   * @param {Object|null} aClothingType - The type of the clothing item (e.g., shirt, pants).
   * @param {String} aClothingItemName - The name of the clothing item.
   * @param {Number} aClothingItemSize - The size of the clothing item.
   * @param {String} aClothingItemColor - The color of the clothing item.
   */
  constructor(
    aClothingItemId = 0,
    aClothingType = null,
    aClothingItemName = "",
    aClothingItemSize = 0,
    aClothingItemColor = ""
  ) {
    super();
    this.clothingItemId = aClothingItemId;
    this.clothingType = aClothingType;
    this.clothingItemName = aClothingItemName;
    this.clothingItemSize = aClothingItemSize;
    this.clothingItemColor = aClothingItemColor;
  }

  // Getter and setter for clothingItemId
  getClothingItemId() {
    return this.clothingItemId;
  }

  setClothingItemId(value) {
    this.clothingItemId = value;
  }

  // Getter and setter for clothingType
  getClothingType() {
    return this.clothingType;
  }

  setClothingType(value) {
    this.clothingType = value;
  }

  // Getter and setter for clothingItemName
  getClothingItemName() {
    return this.clothingItemName;
  }

  setClothingItemName(value) {
    this.clothingItemName = value;
  }

  // Getter and setter for clothingItemSize
  getClothingItemSize() {
    return this.clothingItemSize;
  }

  setClothingItemSize(value) {
    this.clothingItemSize = value;
  }

  // Getter and setter for clothingItemColor
  getClothingItemColor() {
    return this.clothingItemColor;
  }

  setClothingItemColor(value) {
    this.clothingItemColor = value;
  }

  // String representation of the object
  toString() {
    return `Clothing Item ID: ${this.getClothingItemId()}, Type: ${this.getClothingType()}, Name: ${this.getClothingItemName()}, Size: ${this.getClothingItemSize()}, Color: ${this.getClothingItemColor()}`;
  }

  /**
   * Converts a JSON structure into a ClothingItemBO object.
   * @param {Object} dictionary - The JSON data describing the ClothingItemBO.
   * @returns {ClothingItemBO} - A new ClothingItemBO object.
   */
  static fromJSON(dictionary = {}) {
    const clothingItem = new ClothingItemBO();
    clothingItem.setClothingItemId(dictionary.clothingItemId || 0);
    clothingItem.setClothingType(dictionary.clothingType || null);
    clothingItem.setClothingItemName(dictionary.clothingItemName || "");
    clothingItem.setClothingItemSize(dictionary.clothingItemSize || 0);
    clothingItem.setClothingItemColor(dictionary.clothingItemColor || "");
    return clothingItem;
  }
}
