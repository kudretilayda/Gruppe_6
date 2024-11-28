import BusinessObject from "./BusinessObject";

/**
 * Repräsentiert einen Kleiderschrank mit Kleidungsstücken und Outfits.
 */
export default class KleiderschrankBO extends BusinessObject {
  /**
   * Konstruiert ein KleiderschrankBO-Objekt.
   *
   * @param {Array} aInhalt - Die Liste der Kleidungsstücke im Kleiderschrank.
   * @param {Array} aOutfits - Die Liste der Outfits im Kleiderschrank.
   */
  constructor(aInhalt = [], aOutfits = []) {
    super();
    this.inhalt = aInhalt; // Liste der Kleidungsstücke.
    this.outfits = aOutfits; // Liste der Outfits.
  }

  // Getter und Setter für inhalt
  getInhalt() {
    return this.inhalt;
  }

  setInhalt(value) {
    this.inhalt = value;
  }

  // Getter und Setter für outfits
  getOutfits() {
    return this.outfits;
  }

  setOutfits(value) {
    this.outfits = value;
  }

  // String-Darstellung des Objekts
  toString() {
    return `Kleiderschrank: Inhalt = ${JSON.stringify(this.getInhalt())}, Outfits = ${JSON.stringify(this.getOutfits())}`;
  }

  /**
   * Wandelt eine JSON-Struktur in ein KleiderschrankBO-Objekt um.
   * @param {Object} dictionary - Die JSON-Daten, die das KleiderschrankBO beschreiben.
   * @returns {KleiderschrankBO} - Ein neues KleiderschrankBO-Objekt.
   */
  static fromJSON(dictionary = {}) {
    const kleiderschrank = new KleiderschrankBO();
    kleiderschrank.setInhalt(dictionary.inhalt || []);
    kleiderschrank.setOutfits(dictionary.outfits || []);
    return kleiderschrank;
  }
}
