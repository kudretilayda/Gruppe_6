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


  