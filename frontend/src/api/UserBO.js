import BusinessObject from "./BusinessObject";

/**
 * Repräsentiert ein Benutzerobjekt
 */
export default class UserBO extends BusinessObject {
   /**
   * Konstruiert ein UserBO-Objekt.
   *
   * @param {String} aUserId - Benutzer ID.
   * @param {String} aNachname - Nachname des Benutzers.
   * @param {String} aVorname - Vorname des Benutzers.
   * @param {String} aNickname - Nickname des Benutzers.
   * @param {String} aGoogleId - Google ID des Benutzers.
   * @param {String} aEmail - E-Mail-Adresse des Benutzers.
   */
  constructor(aUserId = "", aNachname = "", aVorname = "", aNickname = "", aGoogleId = "", aEmail = "") {
    super();
    this.userId = aUserId;
    this.nachname = aNachname;
    this.vorname = aVorname;
    this.nickname = aNickname;
    this.googleId = aGoogleId;
    this.email = aEmail;
  }

  // Getter und Setter für userId
  getUserId() {
    return this.userId;
  }

  setUserId(value) {
    this.userId = value;
  }

  // Getter und Setter für nachname
  getNachname() {
    return this.nachname;
  }

  setNachname(value) {
    this.nachname = value;
  }

  // Getter und Setter für vorname
  getVorname() {
    return this.vorname;
  }

  setVorname(value) {
    this.vorname = value;
  }

  // Getter und Setter für nickname
  getNickname() {
    return this.nickname;
  }

  setNickname(value) {
    this.nickname = value;
  }

  // Getter und Setter für googleId
  getGoogleId() {
    return this.googleId;
  }

  setGoogleId(value) {
    this.googleId = value;
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
    return `User: ${this.getUserId()}, ${this.getNachname()}, ${this.getEmail()}, ${this.getVorname()}`;
  }

  /**
   * Wandelt eine JSON-Struktur in ein UserBO-Objekt um.
   * @param {Object} dictionary - Die JSON-Daten, die das UserBO beschreiben.
   * @returns {UserBO} - Ein neues UserBO-Objekt.
   */
  static fromJSON(dictionary = {}) {
    const user = new UserBO();
    user.setUserId(dictionary.userId || "");
    user.setNachname(dictionary.nachname || "");
    user.setVorname(dictionary.vorname || "");
    user.setNickname(dictionary.nickname || "");
    user.setGoogleId(dictionary.googleId || "");
    user.setEmail(dictionary.email || "");
    return user;
  }
}
