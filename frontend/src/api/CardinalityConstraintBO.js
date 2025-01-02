import ConstraintBO from "./ConstraintBO";

export default class CardinalityConstraintBO extends ConstraintBO {
  constructor(objects, minCount, maxCount) {
    super();
    this.objects = objects;
    this.minCount = minCount;
    this.maxCount = maxCount;
  }

  validate() {
    const selectedCount = this.objects.filter(obj => obj.isSelected()).length;

    if (selectedCount < this.minCount || selectedCount > this.maxCount) {
      console.error(
        `Error: ${selectedCount} selected items, allowed range: ${this.minCount} - ${this.maxCount}.`
      );
      return false;
    }
    return true;
  }
}
