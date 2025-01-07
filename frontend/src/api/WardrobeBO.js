import BusinessObject from "./BusinessObject.js";

/**
 * Represents a wardrobe with clothing items and outfits.
 */
export default class WardrobeBO extends BusinessObject {
  /**
   * Constructs a WardrobeBO object.
   *
   * @param {Array} aContents - The list of clothing items in the wardrobe.
   * @param {Array} aOutfits - The list of outfits in the wardrobe.
   */
  constructor(aContents = [], aOutfits = []) {
    super();
    this.contents = aContents; // List of clothing items.
    this.outfits = aOutfits; // List of outfits.
  }

  // Getter and setter for contents
  getContents() {
    return this.contents;
  }

  setContents(value) {
    this.contents = value;
  }

  // Getter and setter for outfits
  getOutfits() {
    return this.outfits;
  }

  setOutfits(value) {
    this.outfits = value;
  }

  // String representation of the object
  toString() {
    return `Wardrobe: Contents = ${JSON.stringify(this.getContents())}, Outfits = ${JSON.stringify(this.getOutfits())}`;
  }

  /**
   * Converts a JSON structure into a WardrobeBO object.
   * @param {Object} dictionary - The JSON data describing the WardrobeBO.
   * @returns {WardrobeBO} - A new WardrobeBO object.
   */
  static fromJSON(dictionary = {}) {
    const wardrobe = new WardrobeBO();
    wardrobe.setContents(dictionary.contents || []);
    wardrobe.setOutfits(dictionary.outfits || []);
    return wardrobe;
  }
}
