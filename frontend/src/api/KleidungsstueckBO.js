import BusinessObject from "./BusinessObject";

/**
 * Repräsentiert ein Kleidungsstück-Objekt.
 */
export default class KleidungsstueckBO extends BusinessObject {
  /**
   * Konstruiert ein KleidungsstueckBO-Objekt.
   *
   * @param {Number} aKleidungsstueckId - ID des Kleidungsstücks.
   * @param {Object|null} aKleidungstyp - Typ des Kleidungsstücks (z. B. Hemd, Hose).
   * @param {String} aKleidungsstueckName - Name des Kleidungsstücks.
   * @param {Number} aKleidungsstueckSize - Größe des Kleidungsstücks.
   * @param {String} aKleidungsstueckColor - Farbe des Kleidungsstücks.
   */
  constructor(
    aKleidungsstueckId = 0,
    aKleidungstyp = null,
    aKleidungsstueckName = "",
    aKleidungsstueckSize = 0,
    aKleidungsstueckColor = ""
  ) {
    super();
    this.kleidungsstueckId = aKleidungsstueckId;
    this.kleidungstyp = aKleidungstyp;
    this.kleidungsstueckName = aKleidungsstueckName;
    this.kleidungsstueckSize = aKleidungsstueckSize;
    this.kleidungsstueckColor = aKleidungsstueckColor;
  }

  // Getter und Setter für kleidungsstueckId
  getKleidungsstueckId() {
    return this.kleidungsstueckId;
  }

  setKleidungsstueckId(value) {
    this.kleidungsstueckId = value;
  }

  // Getter und Setter für kleidungstyp
  getKleidungstyp() {
    return this.kleidungstyp;
  }

  setKleidungstyp(value) {
    this.kleidungstyp = value;
  }

  // Getter und Setter für kleidungsstueckName
  getKleidungsstueckName() {
    return this.kleidungsstueckName;
  }

  setKleidungsstueckName(value) {
    this.kleidungsstueckName = value;
  }

  // Getter und Setter für kleidungsstueckSize
  getKleidungsstueckSize() {
    return this.kleidungsstueckSize;
  }

  setKleidungsstueckSize(value) {
    this.kleidungsstueckSize = value;
  }

  // Getter und Setter für kleidungsstueckColor
  getKleidungsstueckColor() {
    return this.kleidungsstueckColor;
  }

  setKleidungsstueckColor(value) {
    this.kleidungsstueckColor = value;
  }

  // String-Darstellung des Objekts
  toString() {
    return `Kleidungsstück ID: ${this.getKleidungsstueckId()}, Typ: ${this.getKleidungstyp()}, Name: ${this.getKleidungsstueckName()}, Größe: ${this.getKleidungsstueckSize()}, Farbe: ${this.getKleidungsstueckColor()}`;
  }

  /**
   * Wandelt eine JSON-Struktur in ein KleidungsstueckBO-Objekt um.
   * @param {Object} dictionary - Die JSON-Daten, die das KleidungsstueckBO beschreiben.
   * @returns {KleidungsstueckBO} - Ein neues KleidungsstueckBO-Objekt.
   */
  static fromJSON(dictionary = {}) {
    const kleidungsstueck = new KleidungsstueckBO();
    kleidungsstueck.setKleidungsstueckId(dictionary.kleidungsstueckId || 0);
    kleidungsstueck.setKleidungstyp(dictionary.kleidungstyp || null);
    kleidungsstueck.setKleidungsstueckName(dictionary.kleidungsstueckName || "");
    kleidungsstueck.setKleidungsstueckSize(dictionary.kleidungsstueckSize || 0);
    kleidungsstueck.setKleidungsstueckColor(dictionary.kleidungsstueckColor || "");
    return kleidungsstueck;
  }
}
