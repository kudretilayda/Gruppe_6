import ConstraintBO from "./ConstraintBO.js";

export default class MutexConstraintBO extends ConstraintBO {
  constructor(mutexPairs) {
    super();
    this.mutexPairs = mutexPairs; // Array of pairs [item1, item2]
  }

  validate(outfit) {
    for (const [item1, item2] of this.mutexPairs) {
      if (outfit.items.includes(item1) && outfit.items.includes(item2)) {
        console.error(
          `Conflict: ${item1.name} and ${item2.name} cannot coexist in the same outfit.`
        );
        return false;
      }
    }
    return true;
  }
}
