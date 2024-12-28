import BusinessObject from "./BusinessObject";

/**
 * Represents a User object
 */
export default class UserBO extends BusinessObject {
   /**
   * Constructs a UserBO object.
   *
   * @param {String} aUserId - User ID.
   * @param {String} aLastName - Last name of the user.
   * @param {String} aFirstName - First name of the user.
   * @param {String} aNickname - Nickname of the user.
   * @param {String} aGoogleId - Google ID of the user.
   * @param {String} anEmail - Email address of the user.
   */
  constructor(aUserId = "", aLastName = "", aFirstName = "", aNickname = "", aGoogleId = "", anEmail = "") {
    super();
    this.userId = aUserId;
    this.lastName = aLastName;
    this.firstName = aFirstName;
    this.nickname = aNickname;
    this.googleId = aGoogleId;
    this.email = anEmail;
  }

  // Getter and Setter for userId
  getUserId() {
    return this.userId;
  }

  setUserId(value) {
    this.userId = value;
  }

  // Getter and Setter for lastName
  getLastName() {
    return this.lastName;
  }

  setLastName(value) {
    this.lastName = value;
  }

  // Getter and Setter for firstName
  getFirstName() {
    return this.firstName;
  }

  setFirstName(value) {
    this.firstName = value;
  }

  // Getter and Setter for nickname
  getNickname() {
    return this.nickname;
  }

  setNickname(value) {
    this.nickname = value;
  }

  // Getter and Setter for googleId
  getGoogleId() {
    return this.googleId;
  }

  setGoogleId(value) {
    this.googleId = value;
  }

  // Getter and Setter for email
  getEmail() {
    return this.email;
  }

  setEmail(value) {
    this.email = value;
  }

  // String representation of the object
  toString() {
    return `User: ${this.getUserId()}, ${this.getLastName()}, ${this.getEmail()}, ${this.getFirstName()}`;
  }

  /**
   * Converts a JSON structure into a UserBO object.
   * @param {Object} dictionary - The JSON data describing the UserBO.
   * @returns {UserBO} - A new UserBO object.
   */
  static fromJSON(dictionary = {}) {
    const user = new UserBO();
    user.setUserId(dictionary.userId || "");
    user.setLastName(dictionary.lastName || "");
    user.setFirstName(dictionary.firstName || "");
    user.setNickname(dictionary.nickname || "");
    user.setGoogleId(dictionary.googleId || "");
    user.setEmail(dictionary.email || "");
    return user;
  }
}