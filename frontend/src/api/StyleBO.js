import BusinessObject from "./BusinessObject";

/**
 * Represents a Style object.
 */
export default class StyleBO extends BusinessObject {
  /**
   * Constructs a StyleBO object.
   *
   * @param {Number} aStyleId - ID of the style.
   * @param {String} aFeatures - Features of the style.
   * @param {Array} aConstraints - Constraints of the style.
   * @param {Array} aClothingTypes - Clothing types of the style.
   */
  constructor(aStyleId = 0, aFeatures = "", aConstraints = [], aClothingTypes = []) {
    super();
    this.styleId = aStyleId;
    this.features = aFeatures;
    this.constraints = aConstraints;
    this.clothingTypes = aClothingTypes;
  }

  // Getter and setter for styleId
  getStyleId() {
    return this.styleId;
  }

  setStyleId(value) {
    this.styleId = value;
  }

  // Getter and setter for features
  getFeatures() {
    return this.features;
  }

  setFeatures(value) {
    this.features = value;
  }

  // Getter and setter for constraints
  getConstraints() {
    return this.constraints;
  }

  setConstraints(value) {
    this.constraints = value;
  }

  // Getter and setter for clothingTypes
  getClothingTypes() {
    return this.clothingTypes;
  }

  setClothingTypes(value) {
    this.clothingTypes = value;
  }

  // String representation of the object
  toString() {
    return `Style: ${this.getStyleId()}, ${this.getFeatures()}, ${JSON.stringify(this.getConstraints())}, ${JSON.stringify(this.getClothingTypes())}`;
  }

  /**
   * Converts a JSON structure into a StyleBO object.
   * @param {Object} dictionary - The JSON data describing the StyleBO.
   * @returns {StyleBO} - A new StyleBO object.
   */
  static fromJSON(dictionary = {}) {
    const style = new StyleBO();
    style.setStyleId(dictionary.styleId || 0);
    style.setFeatures(dictionary.features || "");
    style.setConstraints(dictionary.constraints || []);
    style.setClothingTypes(dictionary.clothingTypes || []);
    return style;
  }
}
