import BusinessObject from "frontend/src/api/BusinessObject.js";



export default class ConstraintBO extends BusinessObject {
   

constructor() {
  super();
  this.constraintID = 0}

  getConstraintID() {
    return this.constraintID
  }

  setConstraintID(c_id) {
    this.constraintID = c_id
  }

validate(...args) {
  throw new Error("Validate method must be implemented in a subclass.");}


static fromJSON(dictionary = {}) {
  const constraint = new ConstraintBO();
  constraint.setConstraintID(dictionary.constraintID || 0);
  return constraint;}
}