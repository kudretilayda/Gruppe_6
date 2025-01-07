import BusinessObject from "./BusinessObject.js";

export default class ClothingItemBO extends BusinessObject {

  /**
   * Constructs a ClothingItemBO object.
   *
   * @param {Number} aClothingItemId - The ID of the clothing item.
   * @param {Object|null} aClothingType - The type of the clothing item (e.g., shirt, pants).
   * @param {String} aClothingItemName - The name of the clothing item.
   * @param {Number} aWardrobeId - Associated Wardrobe
   */
  constructor(
    aClothingItemId = 0,
    aWardrobeId = 0,
    aClothingType = null,
    aClothingItemName = ""
  ) {
    super();
    this.clothingItemId = aClothingItemId;
    this.clothingType = aClothingType;
    this.clothingItemName = aClothingItemName;
    this.wardrobeId = aWardrobeId
  }

  // Getter and setter for clothingItemId
  getClothingItemId() {
    return this.clothingItemId;
  }

  setClothingItemId(itemId) {
    this.clothingItemId = itemId;
  }

  getWardrobeId() {
    return this.wardrobeId
  }

  setWardrobeId(wardrobeId) {
    this.wardrobeId = wardrobeId
  }

  // Getter and setter for clothingType
  getClothingType() {
    return this.clothingType;
  }

  setClothingType(ctype) {
    this.clothingType = ctype;
  }

  // Getter and setter for clothingItemName
  getClothingItemName() {
    return this.clothingItemName;
  }

  setClothingItemName(name) {
    this.clothingItemName = name;
  }

  // String representation of the object
  toString() {
    return `Clothing Item ID: ${this.getClothingItemId()}, 
    Name: ${this.getClothingItemName()},
    Type: ${this.getClothingType()}, 
    Wardrobe: ${this.getWardrobeId()}
    }`;
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
    clothingItem.setWardrobeId(dictionary.wardrobeId || 0);
    return clothingItem;
  }
}
