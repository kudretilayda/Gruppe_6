import BusinessObject from "./BusinessObject";

/**
 * Repräsentiert ein Outfit-Objekt
 */
export default class OutfitBO extends BusinessObject {
  /**
   * Konstruiert ein OutfitBO-Objekt.
   *
   * @param {Number} aOutfitId - ID des Outfits.
   * @param {Array} aKleidungsstuecke - Kleidungsstücke des Outfits.
   * @param {Object} aStyle - Style des Outfits.
   */
  constructor(aOutfitId = 0, aKleidungsstuecke = [], aStyle = null) {
    super();
    this.outfitId = aOutfitId;
    this.kleidungsstuecke = aKleidungsstuecke;
    this.style = aStyle;
  }

  // Getter und Setter für outfitId
  getOutfitId() {
    return this.outfitId;
  }

  setOutfitId(value) {
    this.outfitId = value;
  }

  // Getter und Setter für kleidungsstuecke
  getKleidungsstuecke() {
    return this.kleidungsstuecke;
  }

  setKleidungsstuecke(value) {
    this.kleidungsstuecke = value;
  }

  // Getter und Setter für style
  getStyle() {
    return this.style;
  }

  setStyle(value) {
    this.style = value;
  }

  // String-Darstellung des Objekts
  toString() {
    return `Outfit: ${this.getOutfitId()}, ${JSON.stringify(this.getKleidungsstuecke())}, ${this.getStyle()}`;
  }

  /**
   * Wandelt eine JSON-Struktur in ein OutfitBO-Objekt um.
   * @param {Object} dictionary - Die JSON-Daten, die das OutfitBO beschreiben.
   * @param {Object|null} styleInstance - Eine optionale Style-Instanz, die mit dem Outfit verbunden ist.
   * @returns {OutfitBO} - Ein neues OutfitBO-Objekt.
   */
  static fromJSON(dictionary = {}, styleInstance = null) {
    const outfit = new OutfitBO();
    outfit.setOutfitId(dictionary.outfitId || 0);
    outfit.setKleidungsstuecke(dictionary.kleidungsstuecke || []);
    outfit.setStyle(styleInstance);
    return outfit;
  }
}
