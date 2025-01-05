import BusinessObject from './BusinessObject.js'

/**UserBO fürs Frontend */

export default class UserBO extends BusinessObject {
    googleuserid;

    /** Konstruktion eines neuen Users
     * @param anick_name
     * @param {String} afirstname - der Vorname von diesem  CustomerBO.
     * @param {String} alastname - der Nachname von diesem  CustomerBO.
     * @param {String} ahouseholdid - die Haushalts ID von diesem CustomerBO.
     * @param {String} agoogleuserid - die Google User ID von diesem CustomerBO.
     */
    constructor(anick_name, afirstname, alastname,  ahouseholdid, agoogleuserid,) {
        super();
        this.nick_name = anick_name;
        this.first_name = afirstname;
        this.last_name = alastname;
        this.google_user_id = agoogleuserid;
    }


    /**
   * Setzen eines neuen Vornamen.
   *
   * @param {String} afirstname - neuer Vorname von diesem CustomerBO.
   */
    setfirstname(afirstname) {
        this.first_name = afirstname;
    }

    getfirsname() {
        return this.first_name;
    }


    /**
     * Setzen eines neuen Nachnamen.
     *
     * @param alastname
     */
    setlastname(alastname) {
        this.last_name = alastname;
    }

    getlastname(){
        return this.last_name;
    }


    /**
     * Setzen eines neuen Nicknamen.
     *
     * @param anick_name
     */
    setnickname(anick_name) {
        this.nick_name = anick_name;
    }

    getnickname() {
        return this.nick_name;
    }


    /**
   * Setzen einer neuen Google User ID.
   *
   * @param {String} agoogleuserid - neue Google User ID von diesem CustomerBO.
   */
    setgoogleuserid(agoogleuserid) {
        this.google_user_id = agoogleuserid;
    }

    getgoogleuserid() {
        return this.googleuserid;
    }




    static fromJSON(users) {
        let result = [];
        /**
         * Wir erstellen aus jedem Objekt von User eine Json.
         *
         */

        if (Array.isArray(users)) {
          users.forEach((u) => {
            Object.setPrototypeOf(u, UserBO.prototype);
            result.push(u);
          })
        } else {
          // Sollte es ein Singelton Objekt sein
          let u = users;
          Object.setPrototypeOf(u, UserBO.prototype);
          result.push(u);
        }

        return result;
      }
}