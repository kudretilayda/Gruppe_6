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
  #getClothingItemsURL = (userId, wardrobeId) => `${this.#serverBaseURL}/users/${userId}/wardrobe/${wardrobeId}/clothingitems`;
  #addClothingItemURL = (userId, wardrobeId) => `${this.#serverBaseURL}/users/${userId}/wardrobe/${wardrobeId}/clothingitems`;
  #deleteClothingItemURL = (userId, wardrobeId, clothingItemId) => `${this.#serverBaseURL}/users/${userId}/wardrobe/${wardrobeId}/clothingitems/${clothingItemId}`;
  #updateClothingItemURL = (userId, wardrobeId, clothingItemId) => `${this.#serverBaseURL}/users/${userId}/wardrobe/${wardrobeId}/clothingitems/${clothingItemId}`;

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
    #getBinaryConstraintsURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/binaryconstraints`;
    #addBinaryConstraintURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/binaryconstraints`;
    #updateBinaryConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/binaryconstraints/${constraintId}`;
    #deleteBinaryConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/binaryconstraints/${constraintId}`;

    // UnaryConstraint Endpoints
    #getUnaryConstraintsURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/unaryconstraints`;
    #addUnaryConstraintURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/unaryconstraints`;
    #updateUnaryConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/unaryconstraints/${constraintId}`;
    #deleteUnaryConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/unaryconstraints/${constraintId}`;

    // ImplicationConstraint Endpoints
    #getImplicationConstraintsURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/implicationconstraints`;
    #addImplicationConstraintURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/implicationconstraints`;
    #updateImplicationConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/implicationconstraints/${constraintId}`;
    #deleteImplicationConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/implicationconstraints/${constraintId}`;

    // MutexConstraint Endpoints
    #getMutexConstraintsURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/mutexconstraints`;
    #addMutexConstraintURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/mutexconstraints`;
    #updateMutexConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/mutexconstraints/${constraintId}`;
    #deleteMutexConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/mutexconstraints/${constraintId}`;

    // CardinalityConstraint Endpoints
    #getCardinalityConstraintsURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/cardinalityconstraints`;
    #addCardinalityConstraintURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/cardinalityconstraints`;
    #updateCardinalityConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/cardinalityconstraints/${constraintId}`;
    #deleteCardinalityConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/cardinalityconstraints/${constraintId}`;

    // ClothingEntry Endpoints
    #getClothingEntriesURL = (userId) => `${this.#serverBaseURL}/users/${userId}/clothingentries`;
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

    // User Endpoints
getUser = async (id) => {
    const url = this.#getUserURL(id);
    const response = await fetch(url);
    return response.json();
};

addUser = async (userData) => {
    const url = this.#addUserURL();
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
    });
    return response.json();
};

updateUser = async (id, userData) => {
    const url = this.#updateUserURL(id);
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
    });
    return response.json();
};

deleteUser = async (id) => {
    const url = this.#deleteUserURL(id);
    const response = await fetch(url, {
        method: 'DELETE',
    });
    return response.ok;
};

getUserByGoogleId = async (googleId) => {
    const url = this.#getUserByGoogleIdURL(googleId);
    const response = await fetch(url);
    return response.json();
};

// Wardrobe Endpoints
getWardrobe = async (userId) => {
    const url = this.#getWardrobeURL(userId);
    const response = await fetch(url);
    return response.json();
};

addWardrobe = async (userId, wardrobeData) => {
    const url = this.#addWardrobeURL(userId);
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(wardrobeData),
    });
    return response.json();
};

updateWardrobe = async (userId, wardrobeId, wardrobeData) => {
    const url = this.#updateWardrobeURL(userId, wardrobeId);
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(wardrobeData),
    });
    return response.json();
};

deleteWardrobe = async (userId, wardrobeId) => {
    const url = this.#deleteWardrobeURL(userId, wardrobeId);
    const response = await fetch(url, {
        method: 'DELETE',
    });
    return response.ok;
};

// ClothingItem Endpoints
getClothingItems = async (userId, wardrobeId) => {
    const url = this.#getClothingItemsURL(userId, wardrobeId);
    const response = await fetch(url);
    return response.json();
};

addClothingItem = async (userId, wardrobeId, clothingItemData) => {
    const url = this.#addClothingItemURL(userId, wardrobeId);
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(clothingItemData),
    });
    return response.json();
};

updateClothingItem = async (userId, wardrobeId, clothingItemId, clothingItemData) => {
    const url = this.#updateClothingItemURL(userId, wardrobeId, clothingItemId);
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(clothingItemData),
    });
    return response.json();
};

deleteClothingItem = async (userId, wardrobeId, clothingItemId) => {
    const url = this.#deleteClothingItemURL(userId, wardrobeId, clothingItemId);
    const response = await fetch(url, {
        method: 'DELETE',
    });
    return response.ok;
};

// Outfit Endpoints
getOutfits = async (userId) => {
    const url = this.#getOutfitsURL(userId);
    const response = await fetch(url);
    return response.json();
};

addOutfit = async (userId, outfitData) => {
    const url = this.#addOutfitURL(userId);
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(outfitData),
    });
    return response.json();
};

updateOutfit = async (userId, outfitId, outfitData) => {
    const url = this.#updateOutfitURL(userId, outfitId);
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(outfitData),
    });
    return response.json();
};

deleteOutfit = async (userId, outfitId) => {
    const url = this.#deleteOutfitURL(userId, outfitId);
    const response = await fetch(url, {
        method: 'DELETE',
    });
    return response.ok;
};

// Style Endpoints
getStyles = async () => {
    const url = this.#getStylesURL();
    const response = await fetch(url);
    return response.json();
};

addStyle = async (styleData) => {
    const url = this.#addStyleURL();
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(styleData),
    });
    return response.json();
};

updateStyle = async (styleId, styleData) => {
    const url = this.#updateStyleURL(styleId);
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(styleData),
    });
    return response.json();
};

deleteStyle = async (styleId) => {
    const url = this.#deleteStyleURL(styleId);
    const response = await fetch(url, {
        method: 'DELETE',
    });
    return response.ok;
};

getStyleById = async (styleId) => {
    const url = this.#getStyleByIdURL(styleId);
    const response = await fetch(url);
    return response.json();
};

// ClothingType Endpoints
getClothingTypes = async () => {
    const url = this.#getClothingTypesURL();
    const response = await fetch(url);
    return response.json();
};

addClothingType = async (clothingTypeData) => {
    const url = this.#addClothingTypeURL();
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(clothingTypeData),
    });
    return response.json();
};

   // Constraint Endpoints
getConstraints = async (styleId) => {
    const url = this.#getConstraintsURL(styleId);
    const response = await fetch(url);
    return response.json();
};

addConstraint = async (styleId, constraintData) => {
    const url = this.#addConstraintURL(styleId);
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(constraintData),
    });
    return response.json();
};

updateConstraint = async (styleId, constraintId, constraintData) => {
    const url = this.#updateConstraintURL(styleId, constraintId);
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(constraintData),
    });
    return response.json();
};

deleteConstraint = async (styleId, constraintId) => {
    const url = this.#deleteConstraintURL(styleId, constraintId);
    const response = await fetch(url, {
        method: 'DELETE',
    });
    return response.ok;
};

// WardrobeEntry Endpoints
getWardrobeEntries = async (userId, wardrobeId) => {
    const url = this.#getWardrobeEntriesURL(userId, wardrobeId);
    const response = await fetch(url);
    return response.json();
};

addWardrobeEntry = async (userId, wardrobeId, entryData) => {
    const url = this.#addWardrobeEntryURL(userId, wardrobeId);
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(entryData),
    });
    return response.json();
};

updateWardrobeEntry = async (userId, wardrobeId, entryId, entryData) => {
    const url = this.#updateWardrobeEntryURL(userId, wardrobeId, entryId);
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(entryData),
    });
    return response.json();
};

deleteWardrobeEntry = async (userId, wardrobeId, entryId) => {
    const url = this.#deleteWardrobeEntryURL(userId, wardrobeId, entryId);
    const response = await fetch(url, {
        method: 'DELETE',
    });
    return response.ok;
};

// BinaryConstraint Endpoints
getBinaryConstraints = async (styleId) => {
    const url = this.#getBinaryConstraintsURL(styleId);
    const response = await fetch(url);
    return response.json();
};

addBinaryConstraint = async (styleId, binaryConstraintData) => {
    const url = this.#addBinaryConstraintURL(styleId);
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(binaryConstraintData),
    });
    return response.json();
};

updateBinaryConstraint = async (styleId, constraintId, binaryConstraintData) => {
    const url = this.#updateBinaryConstraintURL(styleId, constraintId);
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(binaryConstraintData),
    });
    return response.json();
};

deleteBinaryConstraint = async (styleId, constraintId) => {
    const url = this.#deleteBinaryConstraintURL(styleId, constraintId);
    const response = await fetch(url, {
        method: 'DELETE',
    });
    return response.ok;
};

// UnaryConstraint Endpoints
getUnaryConstraints = async (styleId) => {
    const url = this.#getUnaryConstraintsURL(styleId);
    const response = await fetch(url);
    return response.json();
};

addUnaryConstraint = async (styleId, unaryConstraintData) => {
    const url = this.#addUnaryConstraintURL(styleId);
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(unaryConstraintData),
    });
    return response.json();
};

updateUnaryConstraint = async (styleId, constraintId, unaryConstraintData) => {
    const url = this.#updateUnaryConstraintURL(styleId, constraintId);
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(unaryConstraintData),
    });
    return response.json();
};

deleteUnaryConstraint = async (styleId, constraintId) => {
    const url = this.#deleteUnaryConstraintURL(styleId, constraintId);
    const response = await fetch(url, {
        method: 'DELETE',
    });
    return response.ok;
};

// ImplicationConstraint Endpoints
getImplicationConstraints = async (styleId) => {
    const url = this.#getImplicationConstraintsURL(styleId);
    const response = await fetch(url);
    return response.json();
};

addImplicationConstraint = async (styleId, implicationConstraintData) => {
    const url = this.#addImplicationConstraintURL(styleId);
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(implicationConstraintData),
    });
    return response.json();
};

updateImplicationConstraint = async (styleId, constraintId, implicationConstraintData) => {
    const url = this.#updateImplicationConstraintURL(styleId, constraintId);
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(implicationConstraintData),
    });
    return response.json();
};

deleteImplicationConstraint = async (styleId, constraintId) => {
    const url = this.#deleteImplicationConstraintURL(styleId, constraintId);
    const response = await fetch(url, {
        method: 'DELETE',
    });
    return response.ok;
};

// MutexConstraint Endpoints
getMutexConstraints = async (styleId) => {
    const url = this.#getMutexConstraintsURL(styleId);
    const response = await fetch(url);
    return response.json();
};

addMutexConstraint = async (styleId, mutexConstraintData) => {
    const url = this.#addMutexConstraintURL(styleId);
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(mutexConstraintData),
    });
    return response.json();
};

updateMutexConstraint = async (styleId, constraintId, mutexConstraintData) => {
    const url = this.#updateMutexConstraintURL(styleId, constraintId);
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(mutexConstraintData),
    });
    return response.json();
};

deleteMutexConstraint = async (styleId, constraintId) => {
    const url = this.#deleteMutexConstraintURL(styleId, constraintId);
    const response = await fetch(url, {
        method: 'DELETE',
    });
    return response.ok;
};

// CardinalityConstraint Endpoints
getCardinalityConstraints = async (styleId) => {
    const url = this.#getCardinalityConstraintsURL(styleId);
    const response = await fetch(url);
    return response.json();
};

addCardinalityConstraint = async (styleId, cardinalityConstraintData) => {
    const url = this.#addCardinalityConstraintURL(styleId);
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(cardinalityConstraintData),
    });
    return response.json();
};

updateCardinalityConstraint = async (styleId, constraintId, cardinalityConstraintData) => {
    const url = this.#updateCardinalityConstraintURL(styleId, constraintId);
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(cardinalityConstraintData),
    });
    return response.json();
};

deleteCardinalityConstraint = async (styleId, constraintId) => {
    const url = this.#deleteCardinalityConstraintURL(styleId, constraintId);
    const response = await fetch(url, {
        method: 'DELETE',
    });
    return response.ok;
};