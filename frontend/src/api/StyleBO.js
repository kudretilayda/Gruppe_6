import BusinessObject from "./BusinessObject";

/**
 * Repräsentiert ein Style-Objekt
 */
export default class StyleBO extends BusinessObject {
  /**
   * Konstruiert ein StyleBO-Objekt.
   *
   * @param {Number} aStyleId - ID des Styles.
   * @param {String} aFeatures - Features des Styles.
   * @param {Array} aConstraints - Einschränkungen des Styles.
   * @param {Array} aKleidungstypen - Kleidungstypen des Styles.
   */
  constructor(aStyleId = 0, aFeatures = "", aConstraints = [], aKleidungstypen = []) {
    super();
    this.styleId = aStyleId;
    this.features = aFeatures;
    this.constraints = aConstraints;
    this.kleidungstypen = aKleidungstypen;
  }

  // Getter und Setter für styleId
  getStyleId() {
    return this.styleId;
  }

  setStyleId(value) {
    this.styleId = value;
  }

  // Getter und Setter für features
  getFeatures() {
    return this.features;
  }

  setFeatures(value) {
    this.features = value;
  }

  // Getter und Setter für constraints
  getConstraints() {
    return this.constraints;
  }

  setConstraints(value) {
    this.constraints = value;
  }

  // Getter und Setter für kleidungstypen
  getKleidungstypen() {
    return this.kleidungstypen;
  }

  setKleidungstypen(value) {
    this.kleidungstypen = value;
  }

  // String-Darstellung des Objekts
  toString() {
    return `Style: ${this.getStyleId()}, ${this.getFeatures()}, ${JSON.stringify(this.getConstraints())}, ${JSON.stringify(this.getKleidungstypen())}`;
  }

  /**
   * Wandelt eine JSON-Struktur in ein StyleBO-Objekt um.
   * @param {Object} dictionary - Die JSON-Daten, die das StyleBO beschreiben.
   * @returns {StyleBO} - Ein neues StyleBO-Objekt.
   */
  static fromJSON(dictionary = {}) {
    const style = new StyleBO();
    style.setStyleId(dictionary.styleId || 0);
    style.setFeatures(dictionary.features || "");
    style.setConstraints(dictionary.constraints || []);
    style.setKleidungstypen(dictionary.kleidungstypen || []);
    return style;
  }
}
