import ConstraintBO from "./ConstraintBO";

export default class ImplicationConstraintBO extends ConstraintBO {
 constructor(ifType, thenType) {
   super();
   this.ifType = ifType;
   this.thenType = thenType;
 }

 validate(outfit) {
   const hasIfType = outfit.items.some(item => item.clothingType === this.ifType);
   const hasThenType = outfit.items.some(item => item.clothingType === this.thenType);

   if (hasIfType && !hasThenType) {
     console.error(
       `Rule violated: If ${this.ifType} is present, ${this.thenType} must also be present.`
     );
     return false;
   }
   return true;
 }
}