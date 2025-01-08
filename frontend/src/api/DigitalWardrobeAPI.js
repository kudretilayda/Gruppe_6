import UserBO from './UserBO.js';
import StyleBO from './StyleBO.js';
import OutfitBO from './OutfitBO.js';
import ClothingTypeBO from './ClothingTypeBO.js';
import ClothingItemBO from './ClothingItemBO.js';
import WardrobeBO from './WardrobeBO.js';

import UnaryConstraintBO from './ConstraintAPI/UnaryConstraintBO.js';
import BinaryConstraintBO from './ConstraintAPI/BinaryConstraintBO.js';
import ImplicationConstraintBO from './ConstraintAPI/ImplicationConstraintBO.js';
import MutexConstraintBO from './ConstraintAPI/MutexConstraintBO.js';
import CardinalityConstraintBO from './ConstraintAPI/CardinalityConstraintBO.js';
import ConstraintBO from './ConstraintAPI/ConstraintBO.js';

/*
import ClothingEntryBO from "./ClothingEntryBO";
import ClothingItemEntryBO from "./ClothingItemEntryBO";
import UnitBO from "./UnitBO";
import WardrobeEntryBO from "./WardrobeEntryBO";
 */

class DigitalWardrobeAPI {

    // Singelton instance
    static #api = null;

    // Local Python backend
    #wardrobeServerBaseURL = 'http://127.0.0.1:5000/';

    //Schrank API
    // User endpoints
    #getUserURL = (id) => `${this.#wardrobeServerBaseURL}/users/${id}`;
    #deleteUserURL = (id) => `${this.#wardrobeServerBaseURL}/users/${id}`;
    #getUserByGoogleIdURL = (google_id) => `${this.#wardrobeServerBaseURL}/user-by-google-id/${google_id}`;
    #updateUserURL = (id) => `${this.#wardrobeServerBaseURL}/users/${id}`;
    #addUserURL = () => `${this.#wardrobeServerBaseURL}/users`;

    // Wardrobe Endpoints
    #getWardrobeURL = (userId) => `${this.#wardrobeServerBaseURL}/users/${userId}/wardrobe`;
    #getWardrobeByGoogleIdURL = (google_id) => `${this.#wardrobeServerBaseURL}/user-by-google-id/${google_id}/wardrobe`;
    #addWardrobeURL = (userId) => `${this.#wardrobeServerBaseURL}/users/${userId}/wardrobe`;
    #updateWardrobeURL = (userId, wardrobeId) => `${this.#wardrobeServerBaseURL}/users/${userId}/wardrobe/${wardrobeId}`;
    #deleteWardrobeURL = (userId, wardrobeId) => `${this.#wardrobeServerBaseURL}/users/${userId}/wardrobe/${wardrobeId}`;

    // ClothingItem Endpoints
    #getClothingItemsURL = (userId, wardrobeId) => `${this.#wardrobeServerBaseURL}/users/${userId}/wardrobe/${wardrobeId}/ClothingItems`;
    #addClothingItemURL = (userId, wardrobeId) => `${this.#wardrobeServerBaseURL}/users/${userId}/wardrobe/${wardrobeId}/ClothingItems`;
    #deleteClothingItemURL = (userId, wardrobeId, clothingItemId) => `${this.#wardrobeServerBaseURL}/users/${userId}/wardrobe/${wardrobeId}/ClothingItems/${clothingItemId}`;
    #updateClothingItemURL = (userId, wardrobeId, clothingItemId) => `${this.#wardrobeServerBaseURL}/users/${userId}/wardrobe/${wardrobeId}/ClothingItems/${clothingItemId}`;

    // Outfit endpoints
    #getOutfitsURL = (userId) => `${this.#wardrobeServerBaseURL}/users/${userId}/outfits`;
    #addOutfitURL = (userId) => `${this.#wardrobeServerBaseURL}/users/${userId}/outfits`;
    #deleteOutfitURL = (userId, outfitId) => `${this.#wardrobeServerBaseURL}/users/${userId}/outfits/${outfitId}`;
    #updateOutfitURL = (userId, outfitId) => `${this.#wardrobeServerBaseURL}/users/${userId}/outfits/${outfitId}`;

    // Style endpoints
    #getStylesURL = () => `${this.#wardrobeServerBaseURL}/styles`;
    #addStyleURL = () => `${this.#wardrobeServerBaseURL}/styles`;
    #updateStyleURL = (styleId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}`;
    #deleteStyleURL = (styleId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}`;
    #getStyleByIdURL = (styleId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}`;

    // ClothingType endpoints
    #getClothingTypesURL = () => `${this.#wardrobeServerBaseURL}/ClothingTypes`;
    #addClothingTypeURL = () => `${this.#wardrobeServerBaseURL}/ClothingTypes`;

    // Constraint Endpoints
    #getConstraintsURL = (styleId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/constraints`;
    #addConstraintURL = (styleId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/constraints`;
    #updateConstraintURL = (styleId, constraintId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/constraints/${constraintId}`;
    #deleteConstraintURL = (styleId, constraintId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/constraints/${constraintId}`;

    // WardrobeEntry Endpoints
    #getWardrobeEntriesURL = (userId, wardrobeId) => `${this.#wardrobeServerBaseURL}/users/${userId}/wardrobe/${wardrobeId}/entries`;
    #addWardrobeEntryURL = (userId, wardrobeId) => `${this.#wardrobeServerBaseURL}/users/${userId}/wardrobe/${wardrobeId}/entries`;
    #deleteWardrobeEntryURL = (userId, wardrobeId, entryId) => `${this.#wardrobeServerBaseURL}/users/${userId}/wardrobe/${wardrobeId}/entries/${entryId}`;
    #updateWardrobeEntryURL = (userId, wardrobeId, entryId) => `${this.#wardrobeServerBaseURL}/users/${userId}/wardrobe/${wardrobeId}/entries/${entryId}`;

    // UnaryConstraint Endpoints
    #getUnaryConstraintsURL = (styleId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/UnaryConstraints`;
    #addUnaryConstraintURL = (styleId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/UnaryConstraints`;
    #updateUnaryConstraintURL = (styleId, constraintId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/UnaryConstraints/${constraintId}`;
    #deleteUnaryConstraintURL = (styleId, constraintId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/UnaryConstraints/${constraintId}`;

    // BinaryConstraint Endpoints
    #getBinaryConstraintsURL = (styleId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/BinaryConstraints`;
    #addBinaryConstraintURL = (styleId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/BinaryConstraints`;
    #updateBinaryConstraintURL = (styleId, constraintId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/BinaryConstraints/${constraintId}`;
    #deleteBinaryConstraintURL = (styleId, constraintId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/BinaryConstraints/${constraintId}`;

    // ImplicationConstraint Endpoints
    #getImplicationConstraintsURL = (styleId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/ImplicationConstraints`;
    #addImplicationConstraintURL = (styleId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/ImplicationConstraints`;
    #updateImplicationConstraintURL = (styleId, constraintId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/ImplicationConstraints/${constraintId}`;
    #deleteImplicationConstraintURL = (styleId, constraintId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/ImplicationConstraints/${constraintId}`;

    // MutexConstraint Endpoints
    #getMutexConstraintsURL = (styleId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/MutexConstraints`;
    #addMutexConstraintURL = (styleId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/MutexConstraints`;
    #updateMutexConstraintURL = (styleId, constraintId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/MutexConstraints/${constraintId}`;
    #deleteMutexConstraintURL = (styleId, constraintId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/MutexConstraints/${constraintId}`;

    // CardinalityConstraint Endpoints
    #getCardinalityConstraintsURL = (styleId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/CardinalityConstraints`;
    #addCardinalityConstraintURL = (styleId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/CardinalityConstraints`;
    #updateCardinalityConstraintURL = (styleId, constraintId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/CardinalityConstraints/${constraintId}`;
    #deleteCardinalityConstraintURL = (styleId, constraintId) => `${this.#wardrobeServerBaseURL}/styles/${styleId}/CardinalityConstraints/${constraintId}`;

    /*    // ClothingEntry Endpoints
        #getClothingEntriesURL = (userId) => `${this.#wardrobeServerBaseURL}/users/${userId}/ClothingEntry`;
        #addClothingEntryURL = (userId) => `${this.#wardrobeServerBaseURL}/users/${userId}/ClothingEntry`;
        #deleteClothingEntryURL = (userId, entryId) => `${this.#wardrobeServerBaseURL}/users/${userId}/ClothingEntry/${entryId}`;
        #updateClothingEntryURL = (userId, entryId) => `${this.#wardrobeServerBaseURL}/users/${userId}/ClothingEntry/${entryId}`;

        // ClothingItemEntry Endpoints
        #getClothingItemEntriesURL = (userId) => `${this.#wardrobeServerBaseURL}/users/${userId}/ClothingItemEntry`;
        #addClothingItemEntryURL = (userId) => `${this.#wardrobeServerBaseURL}/users/${userId}/ClothingItemEntry`;
        #deleteClothingItemEntryURL = (userId, entryId) => `${this.#wardrobeServerBaseURL}/users/${userId}/ClothingItemEntry/${entryId}`;
        #updateClothingItemEntryURL = (userId, entryId) => `${this.#wardrobeServerBaseURL}/users/${userId}/ClothingItemEntry/${entryId}`;

        // Size Endpoints
        #getSizesURL = () => `${this.#wardrobeServerBaseURL}/Unit`;
        #getSizesByWardrobeIdURL = (wardrobeId) => `${this.#wardrobeServerBaseURL}/wardrobe/${wardrobeId}/sizes`;
        #addSizeURL = () => `${this.#wardrobeServerBaseURL}/Unit`;
        #updateSizeURL = (sizeId) => `${this.#wardrobeServerBaseURL}/Unit/${sizeId}`;
        #deleteSizeURL = (sizeId) => `${this.#wardrobeServerBaseURL}/Unit/${sizeId}`;
     */


    static getAPI() {
        if (this.#api == null) {
            this.#api = new DigitalWardrobeAPI();
        }
        return this.#api;
    }

    // Fetch-Helper-Methode
    #fetchAdvanced = (url, init) =>
        fetch(url, init).then((res) => {
            if (!res.ok) {
                throw Error(`${res.status} ${res.statusText}`);
            }
            return res.json();
        });

    // Get a single user by ID
    getUser(id) {
        return this.#fetchAdvanced(this.#getUserURL(id)).then((responseJSON) => {
            let userBO = UserBO.fromJSON(responseJSON);
            return Promise.resolve(userBO);
        });
    }

    // Delete a user
    deleteUser(id) {
        return this.#fetchAdvanced(this.#deleteUserURL(id)).then((responseJSON) => {
            // Es gibt möglicherweise keine Rückgabe bei DELETE, daher könnte hier einfach `null` zurückgegeben werden
            return Promise.resolve(null);
        });
    }

    // Get user by Google ID
    getUserByGoogleId(google_id) {
        return this.#fetchAdvanced(this.#getUserByGoogleIdURL(google_id)).then((responseJSON) => {
            let userBO = UserBO.fromJSON(responseJSON);
            return Promise.resolve(userBO);
        });
    }

    // Update user by ID
    updateUser(id, userData) {
        return this.#fetchAdvanced(this.#updateUserURL(id), 'PUT', userData).then((responseJSON) => {
            let userBO = UserBO.fromJSON(responseJSON);
            return Promise.resolve(userBO);
        });
    }

    // Add a new user
    addUser(userData) {
        return this.#fetchAdvanced(this.#addUserURL(), 'POST', userData).then((responseJSON) => {
            let userBO = UserBO.fromJSON(responseJSON);
            return Promise.resolve(userBO);
        });
    }

    // Get wardrobe by userId
    getWardrobe(userId) {
        return this.#fetchAdvanced(this.#getWardrobeURL(userId)).then((responseJSON) => {
            let wardrobeBO = WardrobeBO.fromJSON(responseJSON);
            return Promise.resolve(wardrobeBO);
        });
    }

    // Methode für das Abrufen der WardrobeId für die Google User ID
    getWardrobeIdByGoogleUserId(google_id) {
        return this.#fetchAdvanced(this.#getWardrobeByGoogleIdURL(google_id))
            .then((responseJSON) => {
                // Hier anpassen, je nachdem wie die Daten strukturiert sind, aber
                // wir gehen davon aus, dass die `wardrobeId` vom Server zurückgegeben wird.
                return responseJSON.wardrobeId; // Beispiel, wie du die ID extrahierst
            });
    }

    // Add a new wardrobe
    addWardrobe(userId, wardrobeData) {
        return this.#fetchAdvanced(this.#addWardrobeURL(userId), 'POST', wardrobeData).then((responseJSON) => {
            let wardrobeBO = WardrobeBO.fromJSON(responseJSON);
            return Promise.resolve(wardrobeBO);
        });
    }

    // Update wardrobe by ID
    updateWardrobe(userId, wardrobeId, wardrobeData) {
        return this.#fetchAdvanced(this.#updateWardrobeURL(userId, wardrobeId), 'PUT', wardrobeData).then((responseJSON) => {
            let wardrobeBO = WardrobeBO.fromJSON(responseJSON);
            return Promise.resolve(wardrobeBO);
        });
    }

    // Delete wardrobe by ID
    deleteWardrobe(userId, wardrobeId) {
        return this.#fetchAdvanced(this.#deleteWardrobeURL(userId, wardrobeId)).then((responseJSON) => {
            // Rückgabe null, da DELETE keine Daten zurückgibt
            return Promise.resolve(null);
        });
    }


    // ClothingItem Endpoints
    // Get clothing items in a wardrobe
    getClothingItems(userId, wardrobeId) {
        return this.#fetchAdvanced(this.#getClothingItemsURL(userId, wardrobeId)).then((responseJSON) => {
            let clothingItemsBOs = ClothingItemBO.fromJSON(responseJSON);
            return Promise.resolve(clothingItemsBOs);
        });
    }

    // Add a new clothing item
    addClothingItem(userId, wardrobeId, clothingItemData) {
        return this.#fetchAdvanced(this.#addClothingItemURL(userId, wardrobeId), 'POST', clothingItemData).then((responseJSON) => {
            let clothingItemBO = ClothingItemBO.fromJSON(responseJSON);
            return Promise.resolve(clothingItemBO);
        });
    }

    // Update a clothing item
    updateClothingItem(userId, wardrobeId, clothingItemId, clothingItemData) {
        return this.#fetchAdvanced(this.#updateClothingItemURL(userId, wardrobeId, clothingItemId), 'PUT', clothingItemData).then((responseJSON) => {
            let clothingItemBO = ClothingItemBO.fromJSON(responseJSON);
            return Promise.resolve(clothingItemBO);
        });
    }

    // Delete a clothing item
    deleteClothingItem(userId, wardrobeId, clothingItemId) {
        return this.#fetchAdvanced(this.#deleteClothingItemURL(userId, wardrobeId, clothingItemId)).then((responseJSON) => {
            // Rückgabe null, da DELETE keine Daten zurückgibt
            return Promise.resolve(null);
        });
    }


    // Outfit Endpoints
    // Get outfits for a user
    getOutfits(userId) {
        return this.#fetchAdvanced(this.#getOutfitsURL(userId)).then((responseJSON) => {
            let outfitsBOs = OutfitBO.fromJSON(responseJSON);
            return Promise.resolve(outfitsBOs);
        });
    }

    // Add an outfit for a user
    addOutfit(userId, outfitData) {
        return this.#fetchAdvanced(this.#addOutfitURL(userId), 'POST', outfitData).then((responseJSON) => {
            let outfitBO = OutfitBO.fromJSON(responseJSON);
            return Promise.resolve(outfitBO);
        });
    }

    // Update an outfit
    updateOutfit(userId, outfitId, outfitData) {
        return this.#fetchAdvanced(this.#updateOutfitURL(userId, outfitId), 'PUT', outfitData).then((responseJSON) => {
            let outfitBO = OutfitBO.fromJSON(responseJSON);
            return Promise.resolve(outfitBO);
        });
    }

    // Delete an outfit
    deleteOutfit(userId, outfitId) {
        return this.#fetchAdvanced(this.#deleteOutfitURL(userId, outfitId)).then((responseJSON) => {
            // Rückgabe null, da DELETE keine Daten zurückgibt
            return Promise.resolve(null);
        });
    }

    // Get all styles
    getStyles() {
        return this.#fetchAdvanced(this.#getStylesURL()).then((responseJSON) => {
            let styleBOs = StyleBO.fromJSON(responseJSON);
            return Promise.resolve(styleBOs);
        });
    }

    // Add a new style
    addStyle(styleData) {
        return this.#fetchAdvanced(this.#addStyleURL(), 'POST', styleData).then((responseJSON) => {
            let styleBO = StyleBO.fromJSON(responseJSON);
            return Promise.resolve(styleBO);
        });
    }

    // Update a style
    updateStyle(styleId, styleData) {
        return this.#fetchAdvanced(this.#updateStyleURL(styleId), 'PUT', styleData).then((responseJSON) => {
            let styleBO = StyleBO.fromJSON(responseJSON);
            return Promise.resolve(styleBO);
        });
    }

    // Delete a style
    deleteStyle(styleId) {
        return this.#fetchAdvanced(this.#deleteStyleURL(styleId)).then((responseJSON) => {
            // Rückgabe null, da DELETE keine Daten zurückgibt
            return Promise.resolve(null);
        });
    }

    // Get a style by ID
    getStyleById(styleId) {
        return this.#fetchAdvanced(this.#getStyleByIdURL(styleId)).then((responseJSON) => {
            let styleBO = StyleBO.fromJSON(responseJSON);
            return Promise.resolve(styleBO);
        });
    }

    // ClothingType endpoints
    getClothingTypes() {
        return this.#fetchAdvanced(this.#getClothingTypesURL()).then((responseJSON) => {
            let clothingTypes = ClothingTypeBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(clothingTypes);
            });
        });
    }

    addClothingType(clothingTypeData) {
        return this.#fetchAdvanced(this.#addClothingTypeURL(), {
            method: 'POST',
            body: JSON.stringify(clothingTypeData),
        }).then((responseJSON) => {
            let clothingType = ClothingTypeBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(clothingType);
            });
        });
    }

    // Constraint Endpoints
    getConstraints(styleId) {
        return this.#fetchAdvanced(this.#getConstraintsURL(styleId)).then((responseJSON) => {
            let constraints = ConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(constraints);
            });
        });
    }

    addConstraint(styleId, constraintData) {
        return this.#fetchAdvanced(this.#addConstraintURL(styleId), {
            method: 'POST',
            body: JSON.stringify(constraintData),
        }).then((responseJSON) => {
            let constraint = ConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(constraint);
            });
        });
    }

    updateConstraint(styleId, constraintId, constraintData) {
        return this.#fetchAdvanced(this.#updateConstraintURL(styleId, constraintId), {
            method: 'PUT',
            body: JSON.stringify(constraintData),
        }).then((responseJSON) => {
            let updatedConstraint = ConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(updatedConstraint);
            });
        });
    }

    deleteConstraint(styleId, constraintId) {
        return this.#fetchAdvanced(this.#deleteConstraintURL(styleId, constraintId), {
            method: 'DELETE',
        }).then((responseJSON) => {
            let deletedConstraint = ConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(deletedConstraint);
            });
        });
    }

    // UnaryConstraint Endpoints
    getUnaryConstraints(styleId) {
        return this.#fetchAdvanced(this.#getUnaryConstraintsURL(styleId)).then((responseJSON) => {
            let unaryConstraints = UnaryConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(unaryConstraints);
            });
        });
    }

    addUnaryConstraint(styleId, unaryConstraintData) {
        return this.#fetchAdvanced(this.#addUnaryConstraintURL(styleId), {
            method: 'POST',
            body: JSON.stringify(unaryConstraintData),
        }).then((responseJSON) => {
            let unaryConstraint = UnaryConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(unaryConstraint);
            });
        });
    }

    updateUnaryConstraint(styleId, constraintId, unaryConstraintData) {
        return this.#fetchAdvanced(this.#updateUnaryConstraintURL(styleId, constraintId), {
            method: 'PUT',
            body: JSON.stringify(unaryConstraintData),
        }).then((responseJSON) => {
            let updatedUnaryConstraint = UnaryConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(updatedUnaryConstraint);
            });
        });
    }

    deleteUnaryConstraint(styleId, constraintId) {
        return this.#fetchAdvanced(this.#deleteUnaryConstraintURL(styleId, constraintId), {
            method: 'DELETE',
        }).then((responseJSON) => {
            let deletedUnaryConstraint = UnaryConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(deletedUnaryConstraint);
            });
        });
    }

    // BinaryConstraint Endpoints
    getBinaryConstraints(styleId) {
        return this.#fetchAdvanced(this.#getBinaryConstraintsURL(styleId)).then((responseJSON) => {
            let binaryConstraints = BinaryConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(binaryConstraints);
            });
        });
    }

    addBinaryConstraint(styleId, binaryConstraintData) {
        return this.#fetchAdvanced(this.#addBinaryConstraintURL(styleId), {
            method: 'POST',
            body: JSON.stringify(binaryConstraintData),
        }).then((responseJSON) => {
            let binaryConstraint = BinaryConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(binaryConstraint);
            });
        });
    }

    updateBinaryConstraint(styleId, constraintId, binaryConstraintData) {
        return this.#fetchAdvanced(this.#updateBinaryConstraintURL(styleId, constraintId), {
            method: 'PUT',
            body: JSON.stringify(binaryConstraintData),
        }).then((responseJSON) => {
            let updatedBinaryConstraint = BinaryConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(updatedBinaryConstraint);
            });
        });
    }

    deleteBinaryConstraint(styleId, constraintId) {
        return this.#fetchAdvanced(this.#deleteBinaryConstraintURL(styleId, constraintId), {
            method: 'DELETE',
        }).then((responseJSON) => {
            let deletedBinaryConstraint = BinaryConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(deletedBinaryConstraint);
            });
        });
    }

    // ImplicationConstraint Endpoints
    getImplicationConstraints(styleId) {
        return this.#fetchAdvanced(this.#getImplicationConstraintsURL(styleId)).then((responseJSON) => {
            let implicationConstraints = ImplicationConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(implicationConstraints);
            });
        });
    }

    addImplicationConstraint(styleId, implicationConstraintData) {
        return this.#fetchAdvanced(this.#addImplicationConstraintURL(styleId), {
            method: 'POST',
            body: JSON.stringify(implicationConstraintData),
        }).then((responseJSON) => {
            let implicationConstraint = ImplicationConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(implicationConstraint);
            });
        });
    }

    updateImplicationConstraint(styleId, constraintId, implicationConstraintData) {
        return this.#fetchAdvanced(this.#updateImplicationConstraintURL(styleId, constraintId), {
            method: 'PUT',
            body: JSON.stringify(implicationConstraintData),
        }).then((responseJSON) => {
            let updatedImplicationConstraint = ImplicationConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(updatedImplicationConstraint);
            });
        });
    }

    deleteImplicationConstraint(styleId, constraintId) {
        return this.#fetchAdvanced(this.#deleteImplicationConstraintURL(styleId, constraintId), {
            method: 'DELETE',
        }).then((responseJSON) => {
            let deletedImplicationConstraint = ImplicationConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(deletedImplicationConstraint);
            });
        });
    }

    // MutexConstraint Endpoints
    getMutexConstraints(styleId) {
        return this.#fetchAdvanced(this.#getMutexConstraintsURL(styleId)).then((responseJSON) => {
            let mutexConstraints = MutexConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(mutexConstraints);
            });
        });
    }

    addMutexConstraint(styleId, mutexConstraintData) {
        return this.#fetchAdvanced(this.#addMutexConstraintURL(styleId), {
            method: 'POST',
            body: JSON.stringify(mutexConstraintData),
        }).then((responseJSON) => {
            let mutexConstraint = MutexConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(mutexConstraint);
            });
        });
    }

    updateMutexConstraint(styleId, constraintId, mutexConstraintData) {
        return this.#fetchAdvanced(this.#updateMutexConstraintURL(styleId, constraintId), {
            method: 'PUT',
            body: JSON.stringify(mutexConstraintData),
        }).then((responseJSON) => {
            let updatedMutexConstraint = MutexConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(updatedMutexConstraint);
            });
        });
    }

    deleteMutexConstraint(styleId, constraintId) {
        return this.#fetchAdvanced(this.#deleteMutexConstraintURL(styleId, constraintId), {
            method: 'DELETE',
        }).then((responseJSON) => {
            let deletedMutexConstraint = MutexConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(deletedMutexConstraint);
            });
        });
    }

    // CardinalityConstraint Endpoints
    getCardinalityConstraints(styleId) {
        return this.#fetchAdvanced(this.#getCardinalityConstraintsURL(styleId)).then((responseJSON) => {
            let cardinalityConstraints = CardinalityConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(cardinalityConstraints);
            });
        });
    }

    addCardinalityConstraint(styleId, cardinalityConstraintData) {
        return this.#fetchAdvanced(this.#addCardinalityConstraintURL(styleId), {
            method: 'POST',
            body: JSON.stringify(cardinalityConstraintData),
        }).then((responseJSON) => {
            let cardinalityConstraint = CardinalityConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(cardinalityConstraint);
            });
        });
    }

    updateCardinalityConstraint(styleId, constraintId, cardinalityConstraintData) {
        return this.#fetchAdvanced(this.#updateCardinalityConstraintURL(styleId, constraintId), {
            method: 'PUT',
            body: JSON.stringify(cardinalityConstraintData),
        }).then((responseJSON) => {
            let updatedCardinalityConstraint = CardinalityConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(updatedCardinalityConstraint);
            });
        });
    }

    deleteCardinalityConstraint(styleId, constraintId) {
        return this.#fetchAdvanced(this.#deleteCardinalityConstraintURL(styleId, constraintId), {
            method: 'DELETE',
        }).then((responseJSON) => {
            let deletedCardinalityConstraint = CardinalityConstraintBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(deletedCardinalityConstraint);
            });
        });
    }
}

/*
    // WardrobeEntry Endpoints
    getWardrobeEntries(userId, wardrobeId) {
        return this.#fetchAdvanced(this.#getWardrobeEntriesURL(userId, wardrobeId)).then((responseJSON) => {
            let wardrobeEntries = WardrobeEntryBO.fromJSON(responseJSON);
            return new Promise(function(resolve) {
                resolve(wardrobeEntries);
            });
        });
    }

    addWardrobeEntry(userId, wardrobeId, entryData) {
        return this.#fetchAdvanced(this.#addWardrobeEntryURL(userId, wardrobeId), {
            method: 'POST',
            body: JSON.stringify(entryData),
        }).then((responseJSON) => {
            let wardrobeEntry = WardrobeEntryBO.fromJSON(responseJSON);
            return new Promise(function(resolve) {
                resolve(wardrobeEntry);
            });
        });
    }

    deleteWardrobeEntry(userId, wardrobeId, entryId) {
        return this.#fetchAdvanced(this.#deleteWardrobeEntryURL(userId, wardrobeId, entryId), {
            method: 'DELETE',
        }).then((responseJSON) => {
            let deletedEntry = WardrobeEntryBO.fromJSON(responseJSON);
            return new Promise(function(resolve) {
                resolve(deletedEntry);
            });
        });
    }

    updateWardrobeEntry(userId, wardrobeId, entryId, entryData) {
        return this.#fetchAdvanced(this.#updateWardrobeEntryURL(userId, wardrobeId, entryId), {
            method: 'PUT',
            body: JSON.stringify(entryData),
        }).then((responseJSON) => {
            let updatedEntry = WardrobeEntryBO.fromJSON(responseJSON);
            return new Promise(function(resolve) {
                resolve(updatedEntry);
            });
        });
    }


    // ClothingEntry Endpoints
    getClothingEntries(userId) {
        return this.#fetchAdvanced(this.#getClothingEntriesURL(userId)).then((responseJSON) => {
            let clothingEntries = ClothingEntryBO.fromJSON(responseJSON);
            return new Promise(function(resolve) {
                resolve(clothingEntries);
            });
        });
    }

    addClothingEntry(userId, clothingEntryData) {
        return this.#fetchAdvanced(this.#addClothingEntryURL(userId), {
            method: 'POST',
            body: JSON.stringify(clothingEntryData),
        }).then((responseJSON) => {
            let clothingEntry = ClothingEntryBO.fromJSON(responseJSON);
            return new Promise(function(resolve) {
                resolve(clothingEntry);
            });
        });
    }

    deleteClothingEntry(userId, entryId) {
        return this.#fetchAdvanced(this.#deleteClothingEntryURL(userId, entryId), {
            method: 'DELETE',
        }).then((responseJSON) => {
            let deletedClothingEntry = ClothingEntryBO.fromJSON(responseJSON);
            return new Promise(function(resolve) {
                resolve(deletedClothingEntry);
            });
        });
    }

    updateClothingEntry(userId, entryId, clothingEntryData) {
        return this.#fetchAdvanced(this.#updateClothingEntryURL(userId, entryId), {
            method: 'PUT',
            body: JSON.stringify(clothingEntryData),
        }).then((responseJSON) => {
            let updatedClothingEntry = ClothingEntryBO.fromJSON(responseJSON);
            return new Promise(function(resolve) {
                resolve(updatedClothingEntry);
            });
        });
    }

    // ClothingItemEntry Endpoints
    getClothingItemEntries(userId) {
        return this.#fetchAdvanced(this.#getClothingItemEntriesURL(userId)).then((responseJSON) => {
            let clothingItemEntries = ClothingItemEntryBO.fromJSON(responseJSON);
            return new Promise(function(resolve) {
                resolve(clothingItemEntries);
            });
        });
    }

    addClothingItemEntry(userId, clothingItemEntryData) {
        return this.#fetchAdvanced(this.#addClothingItemEntryURL(userId), {
            method: 'POST',
            body: JSON.stringify(clothingItemEntryData),
        }).then((responseJSON) => {
            let clothingItemEntry = ClothingItemEntryBO.fromJSON(responseJSON);
            return new Promise(function(resolve) {
                resolve(clothingItemEntry);
            });
        });
    }

    deleteClothingItemEntry(userId, entryId) {
        return this.#fetchAdvanced(this.#deleteClothingItemEntryURL(userId, entryId), {
            method: 'DELETE',
        }).then((responseJSON) => {
            let deletedClothingItemEntry = ClothingItemEntryBO.fromJSON(responseJSON);
            return new Promise(function(resolve) {
                resolve(deletedClothingItemEntry);
            });
        });
    }

    updateClothingItemEntry(userId, entryId, clothingItemEntryData) {
        return this.#fetchAdvanced(this.#updateClothingItemEntryURL(userId, entryId), {
            method: 'PUT',
            body: JSON.stringify(clothingItemEntryData),
        }).then((responseJSON) => {
            let updatedClothingItemEntry = ClothingItemEntryBO.fromJSON(responseJSON);
            return new Promise(function(resolve) {
                resolve(updatedClothingItemEntry);
            });
        });
    }

    // Size Endpoints
    getSizes() {
        return this.#fetchAdvanced(this.#getSizesURL()).then((responseJSON) => {
            let sizes = UnitBO.fromJSON(responseJSON);
            return new Promise(function(resolve) {
                resolve(sizes);
            });
        });
    }

    // Methode für das Abrufen der Größen für ein bestimmtes Wardrobe
      getSizeByWardrobeId(wardrobeId) {
        return this.#fetchAdvanced(this.#getSizesByWardrobeIdURL(wardrobeId))
          .then((sizes) => {
            // Hier gehst du davon aus, dass die API die Größen als Array zurückgibt.
            return sizes; // Die tatsächlichen Größen-Daten
          });
      }

    addSize(sizeData) {
        return this.#fetchAdvanced(this.#addSizeURL(), {
            method: 'POST',
            body: JSON.stringify(sizeData),
        }).then((responseJSON) => {
            let size = UnitBO.fromJSON(responseJSON);
            return new Promise(function(resolve) {
                resolve(size);
            });
        });
    }

    updateSize(sizeId, sizeData) {
        return this.#fetchAdvanced(this.#updateSizeURL(sizeId), {
            method: 'PUT',
            body: JSON.stringify(sizeData),
        }).then((responseJSON) => {
            let updatedSize = UnitBO.fromJSON(responseJSON);
            return new Promise(function(resolve) {
                resolve(updatedSize);
            });
        });
    }

    deleteSize(sizeId) {
        return this.#fetchAdvanced(this.#deleteSizeURL(sizeId), {
            method: 'DELETE',
        }).then((responseJSON) => {
            let deletedSize = UnitBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(deletedSize);
            });
        });
        */

export default DigitalWardrobeAPI;
//API TESTEN
