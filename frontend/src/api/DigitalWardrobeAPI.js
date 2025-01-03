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
        const response = await fetch(this.#getUserURL(id));
        return await response.json();
    };

    addUser = async (userData) => {
        const response = await fetch(this.#addUserURL(), {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(userData),
        });
        return await response.json();
    };

    updateUser = async (id, userData) => {
        const response = await fetch(this.#updateUserURL(id), {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(userData),
        });
        return await response.json();
    };

    deleteUser = async (id) => {
        await fetch(this.#deleteUserURL(id), {
            method: 'DELETE',
        });
    };

    // Wardrobe Endpoints
    getWardrobe = async (userId) => {
        const response = await fetch(this.#getWardrobeURL(userId));
        return await response.json();
    };

    addWardrobe = async (userId, wardrobeData) => {
        const response = await fetch(this.#addWardrobeURL(userId), {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(wardrobeData),
        });
        return await response.json();
    };

    updateWardrobe = async (userId, wardrobeId, wardrobeData) => {
        const response = await fetch(this.#updateWardrobeURL(userId, wardrobeId), {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(wardrobeData),
        });
        return await response.json();
    };

    deleteWardrobe = async (userId, wardrobeId) => {
        await fetch(this.#deleteWardrobeURL(userId, wardrobeId), {
            method: 'DELETE',
        });
    };

    // ClothingItem Endpoints
    getClothingItems = async (userId, wardrobeId) => {
        const response = await fetch(this.#getClothingItemsURL(userId, wardrobeId));
        return await response.json();
    };

    addClothingItem = async (userId, wardrobeId, clothingItemData) => {
        const response = await fetch(this.#addClothingItemURL(userId, wardrobeId), {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(clothingItemData),
        });
        return await response.json();
    };

    updateClothingItem = async (userId, wardrobeId, clothingItemId, clothingItemData) => {
        const response = await fetch(this.#updateClothingItemURL(userId, wardrobeId, clothingItemId), {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(clothingItemData),
        });
        return await response.json();
    };

    deleteClothingItem = async (userId, wardrobeId, clothingItemId) => {
        await fetch(this.#deleteClothingItemURL(userId, wardrobeId, clothingItemId), {
            method: 'DELETE',
        });
    };

    // Outfit Endpoints
    getOutfits = async (userId) => {
        const response = await fetch(this.#getOutfitsURL(userId));
        return await response.json();
    };

    addOutfit = async (userId, outfitData) => {
        const response = await fetch(this.#addOutfitURL(userId), {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(outfitData),
        });
        return await response.json();
    };

    updateOutfit = async (userId, outfitId, outfitData) => {
        const response = await fetch(this.#updateOutfitURL(userId, outfitId), {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(outfitData),
        });
        return await response.json();
    };

    deleteOutfit = async (userId, outfitId) => {
        await fetch(this.#deleteOutfitURL(userId, outfitId), {
            method: 'DELETE',
        });
    };

    // Style Endpoints
    getStyles = async () => {
        const response = await fetch(this.#getStylesURL());
        return await response.json();
    };

    addStyle = async (styleData) => {
        const response = await fetch(this.#addStyleURL(), {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(styleData),
        });
        return await response.json();
    };

    updateStyle = async (styleId, styleData) => {
        const response = await fetch(this.#updateStyleURL(styleId), {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(styleData),
        });
        return await response.json();
    };

    deleteStyle = async (styleId) => {
        await fetch(this.#deleteStyleURL(styleId), {
            method: 'DELETE',
        });
    };

    // ClothingType Endpoints
    getClothingTypes = async () => {
        const response = await fetch(this.#getClothingTypesURL());
        return await response.json();
    };

    addClothingType = async (clothingTypeData) => {
        const response = await fetch(this.#addClothingTypeURL(), {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(clothingTypeData),
        });
        return await response.json();
    };

    // Constraint Endpoints
    getConstraints = async (styleId) => {
        const response = await fetch(this.#getConstraintsURL(styleId));
        return await response.json();
    };

    addConstraint = async (styleId, constraintData) => {
        const response = await fetch(this.#addConstraintURL(styleId), {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(constraintData),
        });
        return await response.json();
    };

    updateConstraint = async (styleId, constraintId, constraintData) => {
        const response = await fetch(this.#updateConstraintURL(styleId, constraintId), {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(constraintData),
        });
        return await response.json();
    };

    deleteConstraint = async (styleId, constraintId) => {
        await fetch(this.#deleteConstraintURL(styleId, constraintId), {
            method: 'DELETE',
        });
    };

    // WardrobeEntry Endpoints
    getWardrobeEntries = async (userId, wardrobeId) => {
        const response = await fetch(this.#getWardrobeEntriesURL(userId, wardrobeId));
        return await response.json();
    };

    addWardrobeEntry = async (userId, wardrobeId, wardrobeEntryData) => {
        const response = await fetch(this.#addWardrobeEntryURL(userId, wardrobeId), {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(wardrobeEntryData),
        });
        return await response.json();
    };

    updateWardrobeEntry = async (userId, wardrobeId, entryId, wardrobeEntryData) => {
        const response = await fetch(this.#updateWardrobeEntryURL(userId, wardrobeId, entryId), {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(wardrobeEntryData),
        });
        return await response.json();
    };

    deleteWardrobeEntry = async (userId, wardrobeId, entryId) => {
        await fetch(this.#deleteWardrobeEntryURL(userId, wardrobeId, entryId), {
            method: 'DELETE',
        });
    };