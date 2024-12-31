import UserBO from '../../../Backup/UserBO';
import WardrobeBO from '../../../Backup/WardrobeBO';
import ClothingItemBO from '../../../Backup/ClothingItemBO';
import OutfitBO from '../../../Backup/OutfitBO';
import StyleBO from '../../../Backup/StyleBO';
import ClothingTypeBO from '../../../Backup/ClothingTypeBO';
import ConstraintBO from './ConstraintBO';

/**
 * Abstracts the REST interface of the Digital Wardrobe backend with convenient access methods.
 * The class is implemented as a singleton.
 *
 * @author [Your Name]
 */
export default class DigitalWardrobeAPI {

  // Singleton instance
  static #api = null;

  // Base URL for the API
  #serverBaseURL = '/api';

  // User endpoints
  #getUserURL = (id) => `${this.#serverBaseURL}/users/${id}`;
  #getUserByGoogleIdURL = (googleId) => `${this.#serverBaseURL}/user-by-google-id/${googleId}`;
  #addUserURL = () => `${this.#serverBaseURL}/users`;
  #updateUserURL = (id) => `${this.#serverBaseURL}/users/${id}`;
  #deleteUserURL = (id) => `${this.#serverBaseURL}/users/${id}`;

  // Wardrobe endpoints
  #getWardrobeURL = (userId) => `${this.#serverBaseURL}/users/${userId}/wardrobe`;
  #addClothingItemURL = (userId) => `${this.#serverBaseURL}/users/${userId}/wardrobe/clothingitems`;
  #deleteClothingItemURL = (userId, clothingItemId) => `${this.#serverBaseURL}/users/${userId}/wardrobe/clothingitems/${clothingItemId}`;
  #updateClothingItemURL = (userId, clothingItemId) => `${this.#serverBaseURL}/users/${userId}/wardrobe/clothingitems/${clothingItemId}`;

  // Outfit endpoints
  #getOutfitsURL = (userId) => `${this.#serverBaseURL}/users/${userId}/outfits`;
  #addOutfitURL = (userId) => `${this.#serverBaseURL}/users/${userId}/outfits`;
  #updateOutfitURL = (userId, outfitId) => `${this.#serverBaseURL}/users/${userId}/outfits/${outfitId}`;
  #deleteOutfitURL = (userId, outfitId) => `${this.#serverBaseURL}/users/${userId}/outfits/${outfitId}`;

  // Style endpoints
  #getStylesURL = () => `${this.#serverBaseURL}/styles`;
  #addStyleURL = () => `${this.#serverBaseURL}/styles`;
  #updateStyleURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}`;
  #deleteStyleURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}`;

  // ClothingType endpoints
  #getClothingTypesURL = () => `${this.#serverBaseURL}/clothingtypes`;
  #addClothingTypeURL = () => `${this.#serverBaseURL}/clothingtypes`;

  // Constraint endpoints
  #getConstraintsURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/constraints`;
  #addConstraintURL = (styleId) => `${this.#serverBaseURL}/styles/${styleId}/constraints`;
  #updateConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/constraints/${constraintId}`;
  #deleteConstraintURL = (styleId, constraintId) => `${this.#serverBaseURL}/styles/${styleId}/constraints/${constraintId}`;

  /**
   * Get the Singleton instance
   *
   * @public
   */
  static getAPI() {
    if (this.#api == null) {
      this.#api = new DigitalWardrobeAPI();
    }
    return this.#api;
  }

  /**
   * Fetch data with advanced error handling
   *
   * @private
   */
  #fetchAdvanced = (url, init) => fetch(url, init)
    .then(res => {
      if (!res.ok) {
        throw new Error(`${res.status} ${res.statusText}`);
      }
      return res.json();
    });

  // User Management

getUserByGoogleId(googleId) {
  return this.#fetchAdvanced(this.#getUserByGoogleIdURL(googleId))
    .then(responseJSON => UserBO.fromJSON(responseJSON)[0]);
}

  addUser(userBO) {
    return this.#fetchAdvanced(this.#addUserURL(), {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(userBO),
    }).then(responseJSON => UserBO.fromJSON(responseJSON)[0]);
  }

  updateUser(userBO) {
    return this.#fetchAdvanced(this.#updateUserURL(userBO.getUserId()), {
      method: 'PUT',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(userBO),
    }).then(responseJSON => UserBO.fromJSON(responseJSON)[0]);
  }

  deleteUser(userId) {
    return this.#fetchAdvanced(this.#deleteUserURL(userId), { method: 'DELETE' })
      .then(responseJSON => UserBO.fromJSON(responseJSON)[0]);
  }

  // Wardrobe Management

  getWardrobe(userId) {
    return this.#fetchAdvanced(this.#getWardrobeURL(userId))
      .then(responseJSON => WardrobeBO.fromJSON(responseJSON));
  }

  addClothingItem(userId, clothingItemBO) {
    return this.#fetchAdvanced(this.#addClothingItemURL(userId), {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(clothingItemBO),
    }).then(responseJSON => ClothingItemBO.fromJSON(responseJSON)[0]);
  }

  updateClothingItem(userId, clothingItemBO) {
    return this.#fetchAdvanced(this.#updateClothingItemURL(userId, clothingItemBO.getId()), {
      method: 'PUT',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(clothingItemBO),
    }).then(responseJSON => ClothingItemBO.fromJSON(responseJSON)[0]);
  }

  deleteClothingItem(userId, clothingItemId) {
    return this.#fetchAdvanced(this.#deleteClothingItemURL(userId, clothingItemId), {
      method: 'DELETE',
    }).then(responseJSON => ClothingItemBO.fromJSON(responseJSON)[0]);
  }

  // Outfit Management

  getOutfits(userId) {
    return this.#fetchAdvanced(this.#getOutfitsURL(userId))
      .then(responseJSON => OutfitBO.fromJSON(responseJSON));
  }

  addOutfit(userId, outfitBO) {
    return this.#fetchAdvanced(this.#addOutfitURL(userId), {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(outfitBO),
    }).then(responseJSON => OutfitBO.fromJSON(responseJSON)[0]);
  }

  updateOutfit(userId, outfitBO) {
    return this.#fetchAdvanced(this.#updateOutfitURL(userId, outfitBO.getId()), {
      method: 'PUT',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(outfitBO),
    }).then(responseJSON => OutfitBO.fromJSON(responseJSON)[0]);
  }

  deleteOutfit(userId, outfitId) {
    return this.#fetchAdvanced(this.#deleteOutfitURL(userId, outfitId), {
      method: 'DELETE',
    }).then(responseJSON => OutfitBO.fromJSON(responseJSON)[0]);
  }

  // Style Management

  getStyles() {
    return this.#fetchAdvanced(this.#getStylesURL())
      .then(responseJSON => StyleBO.fromJSON(responseJSON));
  }

  addStyle(styleBO) {
    return this.#fetchAdvanced(this.#addStyleURL(), {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(styleBO),
    }).then(responseJSON => StyleBO.fromJSON(responseJSON)[0]);
  }

  updateStyle(styleBO) {
    return this.#fetchAdvanced(this.#updateStyleURL(styleBO.getStyleId()), {
      method: 'PUT',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(styleBO),
    }).then(responseJSON => StyleBO.fromJSON(responseJSON)[0]);
  }

  deleteStyle(styleId) {
    return this.#fetchAdvanced(this.#deleteStyleURL(styleId), {
      method: 'DELETE',
    }).then(responseJSON => StyleBO.fromJSON(responseJSON)[0]);
  }

  // ClothingType Management

  getClothingTypes() {
    return this.#fetchAdvanced(this.#getClothingTypesURL())
      .then(responseJSON => ClothingTypeBO.fromJSON(responseJSON));
  }

  addClothingType(clothingTypeBO) {
    return this.#fetchAdvanced(this.#addClothingTypeURL(), {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(clothingTypeBO),
    }).then(responseJSON => ClothingTypeBO.fromJSON(responseJSON)[0]);
  }

  // Constraint Management

  getConstraints(styleId) {
    return this.#fetchAdvanced(this.#getConstraintsURL(styleId))
      .then(responseJSON => ConstraintBO.fromJSON(responseJSON));
  }

  addConstraint(styleId, constraintBO) {
    return this.#fetchAdvanced(this.#addConstraintURL(styleId), {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(constraintBO),
    }).then(responseJSON => ConstraintBO.fromJSON(responseJSON)[0]);
  }

  updateConstraint(styleId, constraintBO) {
    return this.#fetchAdvanced(this.#updateConstraintURL(styleId, constraintBO.getId()), {
      method: 'PUT',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(constraintBO),
    }).then(responseJSON => ConstraintBO.fromJSON(responseJSON)[0]);
  }

  deleteConstraint(styleId, constraintId) {
    return this.#fetchAdvanced(this.#deleteConstraintURL(styleId, constraintId), {
      method: 'DELETE',
    }).then(responseJSON => ConstraintBO.fromJSON(responseJSON)[0]);
  }
}
