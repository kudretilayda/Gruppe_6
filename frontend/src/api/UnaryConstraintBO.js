import ConstraintBO from "./ConstraintBO";

export default class UnaryConstraintBO extends ConstraintBO {
  constructor() {
    super();
    this.style = null;
  }

  // Getter and Setter for style
  getStyle() {
    return this.style;
  }

  setStyle(value) {
    this.style = value;
  }

  validate(outfit) {
    return outfit.items.every(item =>
      this.style.getClothingTypes().includes(item.clothingType)
    );
  }
}
