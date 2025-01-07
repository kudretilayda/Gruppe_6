import ConstraintBO from "./ConstraintBO.js";

export default class BinaryConstraintBO extends ConstraintBO {
  constructor(item1, item2) {
    super();
    this.item1 = item1;
    this.item2 = item2;
  }

  validate(style) {
    const isValid =
      style.getClothingTypes().includes(this.item1.clothingType) &&
      style.getClothingTypes().includes(this.item2.clothingType);

    if (!isValid) {
      console.error(
        `${this.item1.name} and ${this.item2.name} do not match the style.`
      );
    }
    return isValid;
  }
}
