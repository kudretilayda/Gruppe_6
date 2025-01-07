/*import UserBO from './UserBO';
import StyleBO from './StyleBO';
import OutfitBO from './OutfitBO';
import ClothingTypeBO from './ClothingTypeBO';
import ClothingItemBO from './ClothingItemBO';
import WardrobeBO from './WardrobeBO';
import BinaryConstraintBO from './ConstraintAPI/BinaryConstraintBO';
import UnaryConstraintBO from './ConstraintAPI/UnaryConstraintBO';
import ImplicationConstraintBO from './ConstraintAPI/ImplicationConstraintBO';
import MutexConstraintBO from './ConstraintAPI/MutexConstraintBO';
import CardinalityConstraintBO from './ConstraintAPI/CardinalityConstraintBO';
import ConstraintBO from './ConstraintAPI/ConstraintBO';

export default class WardrobeAPI {
  static #api = null;
  #serverBaseURL = '/api';

  // User endpoints
  #getUserURL = (id) => `${this.#serverBaseURL}/users/${id}`;
  #updateUserURL = (id) => `${this.#serverBaseURL}/users/${id}`;
  #addUserURL = () => `${this.#serverBaseURL}/users`;

  // Wardrobe endpoints
  #getWardrobeURL = (userId) => `${this.#serverBaseURL}/users/${userId}/wardrobe`;
  #addClothingItemURL = (userId) => `${this.#serverBaseURL}/users/${userId}/wardrobe/clothingitems`;
  #deleteClothingItemURL = (userId, clothingItemId) => 
    `${this.#serverBaseURL}/users/${userId}/wardrobe/clothingitems/${clothingItemId}`;

  // Outfit endpoints
  #getOutfitsURL = (userId) => `${this.#serverBaseURL}/users/${userId}/outfits`;
  #addOutfitURL = (userId) => `${this.#serverBaseURL}/users/${userId}/outfits`;
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

  static getAPI() {
    if (this.#api == null) {
      this.#api = new WardrobeAPI();
    }
    return this.#api;
  }

  #fetchAdvanced = (url, init) => fetch(url, init)
    .then(res => {
      if (!res.ok) {
        throw Error(`${res.status} ${res.statusText}`);
      }
      return res.json();
    })

  // User management
  getUser(userId) {
    return this.#fetchAdvanced(this.#getUserURL(userId))
      .then(responseJSON => {
        let userBO = UserBO.fromJSON(responseJSON)[0];
        return new Promise(resolve => resolve(userBO));
      })
  }

  updateUser(userBO) {
    return this.#fetchAdvanced(this.#updateUserURL(userBO.getUserId()), {
      method: 'PUT',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(userBO)
    }).then(responseJSON => {
      let responseUserBO = UserBO.fromJSON(responseJSON)[0];
      return new Promise(resolve => resolve(responseUserBO));
    })
  }

  addUser(userBO) {
    return this.#fetchAdvanced(this.#addUserURL(), {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(userBO)
    }).then(responseJSON => {
      let responseUserBO = UserBO.fromJSON(responseJSON)[0];
      return new Promise(resolve => resolve(responseUserBO));
    })
  }

  // Wardrobe management
  getWardrobe(userId) {
    return this.#fetchAdvanced(this.#getWardrobeURL(userId))
      .then(responseJSON => {
        let wardrobeBO = WardrobeBO.fromJSON(responseJSON);
        return new Promise(resolve => resolve(wardrobeBO));
      })
  }

  addClothingItem(userId, clothingItemBO) {
    return this.#fetchAdvanced(this.#addClothingItemURL(userId), {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(clothingItemBO)
    }).then(responseJSON => {
      let responseClothingItemBO = ClothingItemBO.fromJSON(responseJSON)[0];
      return new Promise(resolve => resolve(responseClothingItemBO));
    })
  }

  deleteClothingItem(userId, clothingItemId) {
    return this.#fetchAdvanced(this.#deleteClothingItemURL(userId, clothingItemId), {
      method: 'DELETE'
    }).then(responseJSON => {
      let responseClothingItemBO = ClothingItemBO.fromJSON(responseJSON)[0];
      return new Promise(resolve => resolve(responseClothingItemBO));
    })
  }

  // Outfit management
  getOutfits(userId) {
    return this.#fetchAdvanced(this.#getOutfitsURL(userId))
      .then(responseJSON => {
        let outfitBOs = OutfitBO.fromJSON(responseJSON);
        return new Promise(resolve => resolve(outfitBOs));
      })
  }

  addOutfit(userId, outfitBO) {
    return this.#fetchAdvanced(this.#addOutfitURL(userId), {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(outfitBO)
    }).then(responseJSON => {
      let responseOutfitBO = OutfitBO.fromJSON(responseJSON)[0];
      return new Promise(resolve => resolve(responseOutfitBO));
    })
  }

  deleteOutfit(userId, outfitId) {
    return this.#fetchAdvanced(this.#deleteOutfitURL(userId, outfitId), {
      method: 'DELETE'
    }).then(responseJSON => {
      let responseOutfitBO = OutfitBO.fromJSON(responseJSON)[0];
      return new Promise(resolve => resolve(responseOutfitBO));
    })
  }

  // Style management
  getStyles() {
    return this.#fetchAdvanced(this.#getStylesURL())
      .then(responseJSON => {
        let styleBOs = StyleBO.fromJSON(responseJSON);
        return new Promise(resolve => resolve(styleBOs));
      })
  }

  addStyle(styleBO) {
    return this.#fetchAdvanced(this.#addStyleURL(), {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(styleBO)
    }).then(responseJSON => {
      let responseStyleBO = StyleBO.fromJSON(responseJSON)[0];
      return new Promise(resolve => resolve(responseStyleBO));
    })
  }

  updateStyle(styleBO) {
    return this.#fetchAdvanced(this.#updateStyleURL(styleBO.getStyleId()), {
      method: 'PUT',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(styleBO)
    }).then(responseJSON => {
      let responseStyleBO = StyleBO.fromJSON(responseJSON)[0];
      return new Promise(resolve => resolve(responseStyleBO));
    })
  }

  deleteStyle(styleId) {
    return this.#fetchAdvanced(this.#deleteStyleURL(styleId), {
      method: 'DELETE'
    }).then(responseJSON => {
      let responseStyleBO = StyleBO.fromJSON(responseJSON)[0];
      return new Promise(resolve => resolve(responseStyleBO));
    })
  }

  // ClothingType management
  getClothingTypes() {
    return this.#fetchAdvanced(this.#getClothingTypesURL())
      .then(responseJSON => {
        let clothingTypeBOs = ClothingTypeBO.fromJSON(responseJSON);
        return new Promise(resolve => resolve(clothingTypeBOs));
      })
  }

  addClothingType(clothingTypeBO) {
    return this.#fetchAdvanced(this.#addClothingTypeURL(), {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(clothingTypeBO)
    }).then(responseJSON => {
      let responseClothingTypeBO = ClothingTypeBO.fromJSON(responseJSON)[0];
      return new Promise(resolve => resolve(responseClothingTypeBO));
    })
  }

  // Constraint management
  getConstraints(styleId) {
    return this.#fetchAdvanced(this.#getConstraintsURL(styleId))
      .then(responseJSON => {
        let constraints = responseJSON.map(constraint => {
          switch(constraint.type) {
            case 'binary':
              return BinaryConstraintBO.fromJSON(constraint);
            case 'unary':
              return UnaryConstraintBO.fromJSON(constraint);
            case 'implication':
              return ImplicationConstraintBO.fromJSON(constraint);
            case 'mutex':
              return MutexConstraintBO.fromJSON(constraint);
            case 'cardinality':
              return CardinalityConstraintBO.fromJSON(constraint);
            default:
              return ConstraintBO.fromJSON(constraint);
          }
        });
        return new Promise(resolve => resolve(constraints));
      })
  }

  addConstraint(styleId, constraintBO) {
    return this.#fetchAdvanced(this.#addConstraintURL(styleId), {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(constraintBO)
    }).then(responseJSON => {
      let responseConstraintBO = this.#createConstraintFromJSON(responseJSON[0]);
      return new Promise(resolve => resolve(responseConstraintBO));
    })
  }

  updateConstraint(styleId, constraintBO) {
    return this.#fetchAdvanced(this.#updateConstraintURL(styleId, constraintBO.getId()), {
      method: 'PUT',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(constraintBO)
    }).then(responseJSON => {
      let responseConstraintBO = this.#createConstraintFromJSON(responseJSON[0]);
      return new Promise(resolve => resolve(responseConstraintBO));
    })
  }

  deleteConstraint(styleId, constraintId) {
    return this.#fetchAdvanced(this.#deleteConstraintURL(styleId, constraintId), {
      method: 'DELETE'
    }).then(responseJSON => {
      let responseConstraintBO = this.#createConstraintFromJSON(responseJSON[0]);
      return new Promise(resolve => resolve(responseConstraintBO));
    })
  }

  #createConstraintFromJSON(json) {
    switch(json.type) {
      case 'binary':
        return BinaryConstraintBO.fromJSON(json);
      case 'unary':
        return UnaryConstraintBO.fromJSON(json);
      case 'implication':
        return ImplicationConstraintBO.fromJSON(json);
      case 'mutex':
        return MutexConstraintBO.fromJSON(json);
      case 'cardinality':
        return CardinalityConstraintBO.fromJSON(json);
      default:
        return ConstraintBO.fromJSON(json);
    }
  }
}
*/