import BusinessObject from "./BusinessObject";

/**
 * Repräsentiert einen Kleidungstyp (z. B. Hemd, Hose, Kleid).
 */
export default class KleidungstypBO extends BusinessObject {
  /**
   * Konstruiert ein KleidungstypBO-Objekt.
   *
   * @param {Number} aId - ID des Kleidungstyps.
   * @param {String} aName - Der Name des Kleidungstyps.
   * @param {String} aVerwendung - Anlässe oder Zwecke für diesen Kleidungstyp.
   */
  constructor(aId = 0, aName = "", aVerwendung = "") {
    super();
    this.id = aId;
    this.name = aName;
    this.verwendung = aVerwendung;
  }

  // Getter und Setter für name
  getName() {
    return this.name;
  }

  setName(value) {
    this.name = value;
  }

  // Getter und Setter für verwendung
  getVerwendung() {
    return this.verwendung;
  }

  setVerwendung(value) {
    this.verwendung = value;
  }

  // String-Darstellung des Objekts
  toString() {
    return `Kleidungstyp: ${this.getId()}, Name: ${this.getName()}, Verwendung: ${this.getVerwendung()}`;
  }

  /**
   * Wandelt eine JSON-Struktur in ein KleidungstypBO-Objekt um.
   * @param {Object} dictionary - Die JSON-Daten, die das KleidungstypBO beschreiben.
   * @returns {KleidungstypBO} - Ein neues KleidungstypBO-Objekt.
   */
  static fromJSON(dictionary = {}) {
    const kleidungstyp = new KleidungstypBO();
    kleidungstyp.setId(dictionary.id || 0); // Von BusinessObject geerbt.
    kleidungstyp.setName(dictionary.name || "");
    kleidungstyp.setVerwendung(dictionary.verwendung || "");
    return kleidungstyp;
  }
}
