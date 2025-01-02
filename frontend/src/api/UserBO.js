import BusinessObject from './BusinessObject.js';

/** UserBO für den digitalen Kleiderschrank */

export default class UserBO extends BusinessObject {

    /** Konstruktion eines neuen Benutzers
     * @param {String} anickname - Der Nickname des Benutzers.
     * @param {String} afirstname - Der Vorname des Benutzers.
     * @param {String} alastname - Der Nachname des Benutzers.
     * @param {String} awardrobeid - Die ID des Kleiderschranks des Benutzers.
     * @param {String} agoogleuserid - Die Google User ID des Benutzers.
     */
    constructor(anickname, afirstname, alastname, awardrobeid, agoogleuserid) {
        super();
        this.nick_name = anickname;
        this.first_name = afirstname;
        this.last_name = alastname;
        this.wardrobe_id = awardrobeid; // Referenz zum Kleiderschrank
        this.google_user_id = agoogleuserid; // Google ID für die Authentifizierung
    }

    /**
     * Setzt den Vornamen des Benutzers.
     * @param {String} afirstname - Neuer Vorname des Benutzers.
     */
    setFirstName(afirstname) {
        this.first_name = afirstname;
    }

    getFirstName() {
        return this.first_name;
    }

    /**
     * Setzt den Nachnamen des Benutzers.
     * @param {String} alastname - Neuer Nachname des Benutzers.
     */
    setLastName(alastname) {
        this.last_name = alastname;
    }

    getLastName() {
        return this.last_name;
    }

    /**
     * Setzt den Nicknamen des Benutzers.
     * @param {String} anickname - Neuer Nickname des Benutzers.
     */
    setNickName(anickname) {
        this.nick_name = anickname;
    }

    getNickName() {
        return this.nick_name;
    }

    /**
     * Setzt die Google User ID des Benutzers.
     * @param {String} agoogleuserid - Neue Google User ID des Benutzers.
     */
    setGoogleUserId(agoogleuserid) {
        this.google_user_id = agoogleuserid;
    }

    getGoogleUserId() {
        return this.google_user_id;
    }

    /**
     * Setzt die ID des Kleiderschranks des Benutzers.
     * @param {String} awardrobeid - Neue Kleiderschrank-ID des Benutzers.
     */
    setWardrobeId(awardrobeid) {
        this.wardrobe_id = awardrobeid;
    }

    getWardrobeId() {
        return this.wardrobe_id;
    }

    /**
     * Erstellt ein Array von UserBO Objekten aus JSON.
     * @param {Array|Object} users - JSON-Daten von Benutzern.
     * @returns {Array} Array von UserBO Objekten.
     */
    static fromJSON(users) {
        let result = [];
        if (Array.isArray(users)) {
            users.forEach((u) => {
                Object.setPrototypeOf(u, UserBO.prototype);
                result.push(u);
            });
        } else {
            let u = users;
            Object.setPrototypeOf(u, UserBO.prototype);
            result.push(u);
        }
        return result;
    }
}
