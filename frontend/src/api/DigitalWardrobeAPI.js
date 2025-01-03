import UserBO from './UserBO';
import ClothingEntry from "./ClothingEntry";
import ClothingItemEntryBO from "./ClothingItemEntryBO";
import Size from "../api/Size";
import StyleBO from './StyleBO';
import OutfitBO from './OutfitBO';
import ClothingTypeBO from './ClothingTypeBO';
import ClothingItemBO from './ClothingItemBO';
import WardrobeBO from './WardrobeBO';
import WardrobeEntryBO from "./WardrobeEntryBO";
import BinaryConstraintBO from './BinaryConstraintBO';
import UnaryConstraintBO from './UnaryConstraintBO';
import ImplicationConstraintBO from './ImplicationConstraintBO';
import MutexConstraintBO from './MutexConstraintBO';
import CardinalityConstraintBO from './CardinalityConstraintBO';
import ConstraintBO from './ConstraintBO';

class DigitalWardrobeAPI {
    // Basis-URL des Servers
    #serverBaseURL = '/api';

  //Schrank API 
  // User endpoints
  #getUserURL = (id) => `${this.#serverBaseURL}/users/${id}`;
  #deleteUserURL = (id) => `${this.#serverBaseURL}/users/${id}`;
  #getUserByGoogleIdURL = (google_id) => `${this.#serverBaseURL}/user-by-google-id/${google_id}`;
  #updateUserURL = (id) => `${this.#serverBaseURL}/users/${id}`;
  #addUserURL = () => `${this.#serverBaseURL}/users`;

  // Wardrobe Endpoints
  #getWardrobeURL = (userId) => `${this.#serverBaseURL}/users/${userId}/wardrobe`;
  #addWardrobeURL = (userId) => `${this.#serverBaseURL}/users/${userId}/wardrobe`;
  #updateWardrobeURL = (userId, wardrobeId) => `${this.#serverBaseURL}/users/${userId}/wardrobe/${wardrobeId}`;
  #deleteWardrobeURL = (userId, wardrobeId) => `${this.#serverBaseURL}/users/${userId}/wardrobe/${wardrobeId}`;

  // ClothingItem Endpoints
  #getClothingItemsURL = (userId, wardrobeId) => `${this.#serverBaseURL}/users/${userId}/wardrobe/${wardrobeId}/ClothingTtems`;
  #addClothingItemURL = (userId, wardrobeId) => `${this.#serverBaseURL}/users/${userId}/wardrobe/${wardrobeId}/ClothingItems`;
  #deleteClothingItemURL = (userId, wardrobeId, clothingItemId) => `${this.#serverBaseURL}/users/${userId}/wardrobe/${wardrobeId}/ClothingItems/${clothingItemId}`;
  #updateClothingItemURL = (userId, wardrobeId, clothingItemId) => `${this.#serverBaseURL}/users/${userId}/wardrobe/${wardrobeId}/ClothingItems/${clothingItemId}`;

  // Outfit endpoints
  #getOutfitsURL = (userId) => `${this.#serverBaseURL}/users/${userId}/outfits`;
  #addOutfitURL = (userId) => `${this.#serverBaseURL}/users/${userId}/outfits`;
  #deleteOutfitURL = (userId, outfitId) => `${this.#serverBaseURL}/users/${userId}/outfits/${outfitId}`;
  #updateOutfitURL = (userId, outfitId) => `${this.#serverBaseURL}/users/${userId}/outfits/${outfitId}`;
  // Style endpoints
  #getStylesURL = () => `${this.#serverBaseURL}/styles`;
  #addStyleURL = () => `${this.#serverBaseURL}/styles`;
  #updateStyleURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}`;
  #deleteStyleURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}`;
  #getStyleByIdURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}`;

  // ClothingType endpoints
  #getClothingTypesURL = () => `${this.#serverBaseURL}/ClothingTypes`;
  #addClothingTypeURL = () => `${this.#serverBaseURL}/ClothingTypes`;


  // Constraint Endpoints
    #getConstraintsURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/constraints`;
    #addConstraintURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/constraints`;
    #updateConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/constraints/${constraintId}`;
    #deleteConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/constraints/${constraintId}`;

    // WardrobeEntry Endpoints
    #getWardrobeEntriesURL = (userId, wardrobeId) => `${this.#serverBaseURL}/users/${userId}/wardrobe/${wardrobeId}/entries`;
    #addWardrobeEntryURL = (userId, wardrobeId) => `${this.#serverBaseURL}/users/${userId}/wardrobe/${wardrobeId}/entries`;
    #deleteWardrobeEntryURL = (userId, wardrobeId, entryId) => `${this.#serverBaseURL}/users/${userId}/wardrobe/${wardrobeId}/entries/${entryId}`;
    #updateWardrobeEntryURL = (userId, wardrobeId, entryId) => `${this.#serverBaseURL}/users/${userId}/wardrobe/${wardrobeId}/entries/${entryId}`;

    // BinaryConstraint Endpoints
    #getBinaryConstraintsURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/BinaryConstraints`;
    #addBinaryConstraintURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/BinaryConstraints`;
    #updateBinaryConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/BinaryConstraints/${constraintId}`;
    #deleteBinaryConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/BinaryConstraints/${constraintId}`;

    // UnaryConstraint Endpoints
    #getUnaryConstraintsURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/UnaryConstraints`;
    #addUnaryConstraintURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/UnaryConstraints`;
    #updateUnaryConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/UnaryConstraints/${constraintId}`;
    #deleteUnaryConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/UnaryConstraints/${constraintId}`;

    // ImplicationConstraint Endpoints
    #getImplicationConstraintsURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/ImplicationConstraints`;
    #addImplicationConstraintURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/ImplicationConstraints`;
    #updateImplicationConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/ImplicationConstraints/${constraintId}`;
    #deleteImplicationConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/ImplicationConstraints/${constraintId}`;

    // MutexConstraint Endpoints
    #getMutexConstraintsURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/MutexConstraints`;
    #addMutexConstraintURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/MutexConstraints`;
    #updateMutexConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/MutexConstraints/${constraintId}`;
    #deleteMutexConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/MutexConstraints/${constraintId}`;

    // CardinalityConstraint Endpoints
    #getCardinalityConstraintsURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/CardinalityConstraints`;
    #addCardinalityConstraintURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/CardinalityConstraints`;
    #updateCardinalityConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/CardinalityConstraints/${constraintId}`;
    #deleteCardinalityConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/CardinalityConstraints/${constraintId}`;

    // ClothingEntry Endpoints
    #getClothingEntriesURL = (userId) => `${this.#serverBaseURL}/users/${userId}/Clothingentries`;
    #addClothingEntryURL = (userId) => `${this.#serverBaseURL}/users/${userId}/clothingentries`;
    #deleteClothingEntryURL = (userId, entryId) => `${this.#serverBaseURL}/users/${userId}/clothingentries/${entryId}`;
    #updateClothingEntryURL = (userId, entryId) => `${this.#serverBaseURL}/users/${userId}/clothingentries/${entryId}`;

    // ClothingItemEntry Endpoints
    #getClothingItemEntriesURL = (userId) => `${this.#serverBaseURL}/users/${userId}/clothingitementries`;
    #addClothingItemEntryURL = (userId) => `${this.#serverBaseURL}/users/${userId}/clothingitementries`;
    #deleteClothingItemEntryURL = (userId, entryId) => `${this.#serverBaseURL}/users/${userId}/clothingitementries/${entryId}`;
    #updateClothingItemEntryURL = (userId, entryId) => `${this.#serverBaseURL}/users/${userId}/clothingitementries/${entryId}`;

    // Size Endpoints
    #getSizesURL = () => `${this.#serverBaseURL}/sizes`;
    #addSizeURL = () => `${this.#serverBaseURL}/sizes`;
    #updateSizeURL = (sizeId) => `${this.#serverBaseURL}/sizes/${sizeId}`;
    #deleteSizeURL = (sizeId) => `${this.#serverBaseURL}/sizes/${sizeId}`;


  // Fetch-Helper-Methode
    #fetchAdvanced = (url, init) => fetch(url, init)
        .then(res => {
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
        return new Promise(function(resolve) {
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
        return new Promise(function(resolve) {
            resolve(clothingType);
        });
    });
}

/ Constraint Endpoints
getConstraints(styleId) {
    return this.#fetchAdvanced(this.#getConstraintsURL(styleId)).then((responseJSON) => {
        let constraints = ConstraintBO.fromJSON(responseJSON);
        return new Promise(function(resolve) {
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
        return new Promise(function(resolve) {
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
        return new Promise(function(resolve) {
            resolve(updatedConstraint);
        });
    });
}

deleteConstraint(styleId, constraintId) {
    return this.#fetchAdvanced(this.#deleteConstraintURL(styleId, constraintId), {
        method: 'DELETE',
    }).then((responseJSON) => {
        let deletedConstraint = ConstraintBO.fromJSON(responseJSON);
        return new Promise(function(resolve) {
            resolve(deletedConstraint);
        });
    });
}

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

// BinaryConstraint Endpoints
getBinaryConstraints(styleId) {
    return this.#fetchAdvanced(this.#getBinaryConstraintsURL(styleId)).then((responseJSON) => {
        let binaryConstraints = BinaryConstraintBO.fromJSON(responseJSON);
        return new Promise(function(resolve) {
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
        return new Promise(function(resolve) {
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
        return new Promise(function(resolve) {
            resolve(updatedBinaryConstraint);
        });
    });
}

deleteBinaryConstraint(styleId, constraintId) {
    return this.#fetchAdvanced(this.#deleteBinaryConstraintURL(styleId, constraintId), {
        method: 'DELETE',
    }).then((responseJSON) => {
        let deletedBinaryConstraint = BinaryConstraintBO.fromJSON(responseJSON);
        return new Promise(function(resolve) {
            resolve(deletedBinaryConstraint);
        });
    });
}