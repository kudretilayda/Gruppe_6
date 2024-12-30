import BusinessObject from './BusinessObject.js';

/**
 * Repräsentiert ein Benutzer-Objekt
 */
export default class UserBO extends BusinessObject {
  /**
   * Erstellt ein neues UserBO Objekt.
   * 
   * @param {String} aUserId - Benutzer ID
   * @param {String} aGoogleId - Google ID des Benutzers
   * @param {String} aFirstName - Vorname des Benutzers
   * @param {String} aLastName - Nachname des Benutzers
   * @param {String} aNickname - Spitzname des Benutzers
   * @param {String} anEmail - E-Mail-Adresse des Benutzers
   */
  constructor(aUserId = "", aGoogleId = "", aFirstName = "", aLastName = "", aNickname = "", anEmail = "") {
    super();
    this.userId = aUserId;
    this.googleId = aGoogleId;
    this.firstName = aFirstName;
    this.lastName = aLastName;
    this.nickname = aNickname;
    this.email = anEmail;
  }

  // Getter und Setter für userId
  getUserId() {
    return this.userId;
  }

  setUserId(value) {
    this.userId = value;
  }

  // Getter und Setter für googleId
  getGoogleId() {
    return this.googleId;
  }

  setGoogleId(value) {
    this.googleId = value;
  }

  // Getter und Setter für firstName
  getFirstName() {
    return this.firstName;
  }

  setFirstName(value) {
    this.firstName = value;
  }

  // Getter und Setter für lastName
  getLastName() {
    return this.lastName;
  }

  setLastName(value) {
    this.lastName = value;
  }

  // Getter und Setter für nickname
  getNickname() {
    return this.nickname;
  }

  setNickname(value) {
    this.nickname = value;
  }

  // Getter und Setter für email
  getEmail() {
    return this.email;
  }

  setEmail(value) {
    this.email = value;
  }

  // String-Darstellung des Objekts
  toString() {
    return `Benutzer: ${this.getUserId()}, ${this.getLastName()}, ${this.getEmail()}, ${this.getFirstName()}`;
  }

  /**
   * Erstellt ein Array von UserBO Objekten aus einer JSON-Struktur.
   * 
   * @param {Object|Array} users - JSON-Daten von einem oder mehreren Benutzern
   * @returns {Array} Array von UserBO Objekten
   */
  static fromJSON(users) {
    let result = [];

    if (Array.isArray(users)) {
      users.forEach((u) => {
        let user = new UserBO(
          u.userId,
          u.googleId,
          u.firstName,
          u.lastName,
          u.nickname,
          u.email
        );
        result.push(user);
      });
    } else {
      let user = new UserBO(
        users.userId,
        users.googleId,
        users.firstName,
        users.lastName,
        users.nickname,
        users.email
      );
      result.push(user);
    }

    return result;
  }
}