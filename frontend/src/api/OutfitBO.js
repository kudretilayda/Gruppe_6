import BusinessObject from "./BusinessObject.js";

/**
 * Represents an Outfit object.
 */
export default class OutfitBO extends BusinessObject {
  /**
   * Constructs an OutfitBO object.
   *
   * @param {Number} aOutfitId - ID of the outfit.
   * @param {String} aName - Name of the Outfit
   * @param {Array} aClothingItems - Clothing items of the outfit.
   * @param {Object} aStyle - Style of the outfit.
   */
  constructor(aOutfitId = 0, aName = '', aClothingItems = [], aStyle = null) {
    super();
    this.outfitId = aOutfitId;
    this.name = aName
    this.clothingItems = aClothingItems;
    this.style = aStyle;
  }

  // Getter and setter for outfitId
  getOutfitId() {
    return this.outfitId;
  }

  setOutfitId(value) {
    this.outfitId = value;
  }

  getOutfitName() {
  return this.name
  }

  setName(name) {
    this.name = name
  }

  // Getter and setter for clothingItems
  getClothingItems() {
    return this.clothingItems;
  }

  setClothingItems(item) {
    this.clothingItems.push(item);
  }

  // Getter and setter for style
  getStyle() {
    return this.style;
  }

  setStyle(style) {
    this.style = style;
  }

  // String representation of the object
  toString() {
    return `Outfit: ${this.getOutfitId()}, ${this.getOutfitName()}, ${JSON.stringify(this.getClothingItems())}, 
    ${this.getStyle()}`;
  }

  /**
   * Converts a JSON structure into an OutfitBO object.
   * @param {Object} dictionary - The JSON data describing the OutfitBO.
   * @param {Object|null} styleInstance - An optional style instance associated with the outfit.
   * @returns {OutfitBO} - A new OutfitBO object.
   */
  static fromJSON(dictionary = {}, styleInstance = null) {
    const outfit = new OutfitBO();
    outfit.setOutfitId(dictionary.outfitId || 0);
    outfit.setName(dictionary.name || '')
    outfit.setClothingItems(dictionary.clothingItems || []);
    outfit.setStyle(styleInstance);
    return outfit;
  }
}
