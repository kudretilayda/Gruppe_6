import UserBO from './UserBO';
import UnitBO from "./UnitBO";
import StyleBO from './StyleBO';
import OutfitBO from './OutfitBO';
import ClothingTypeBO from './ClothingTypeBO';
import ClothingItemBO from './ClothingItemBO';
import WardrobeBO from './WardrobeBO';
import BinaryConstraintBO from './BinaryConstraintBO';
import UnaryConstraintBO from './UnaryConstraintBO';
import ImplicationConstraintBO from './ImplicationConstraintBO';
import MutexConstraintBO from './MutexConstraintBO';
import CardinalityConstraintBO from './CardinalityConstraintBO';
import ConstraintBO from './ConstraintBO';

class DigitalWardrobeAPI {

  // Singelton instance
  static #api = null;

  // Local Python backend
  #wardrobeServerBaseURL = 'http://localhost:5000/wardrobe';

  //Schrank API 
  // User endpoints
  #getUsersURL = () => `${this.#wardrobeServerBaseURL}/Users/`;
  #addUsersURL = () => `${this.#wardrobeServerBaseURL}/Users`;
  #getUsersByGoogleIdURL = (google_id) => `${this.#wardrobeServerBaseURL}/User-by-google-id/${google_id}`;
  #updateUsersURL = (user_id) => `${this.#wardrobeServerBaseURL}/Users/${user_id}`;
  #deleteUsersURL = (user_id) => `${this.#wardrobeServerBaseURL}/Users/${user_id}`;


  // Wardrobe Endpoints
  #getWardrobesURL = () => `${this.#wardrobeServerBaseURL}/Wardrobe`;
  #getWardrobeIdByGoogleUserId = (google_id) => `${this.#wardrobeServerBaseURL}/Wardrobe/${google_id}`;
  #addWardrobeURL = () => `${this.#wardrobeServerBaseURL}/Wardrobe`;
  #updateWardrobeURL = (wardrobeId) => `${this.#wardrobeServerBaseURL}/Wardrobe/${wardrobeId}`;
  #deleteWardrobeURL = (wardrobeId) => `${this.#wardrobeServerBaseURL}/Wardrobe/${wardrobeId}`;

  // ClothingItem Endpoints
  #getClothingItemsURL = () => `${this.#wardrobeServerBaseURL}/ClothingItems`;
  #addClothingItemURL = () => `${this.#wardrobeServerBaseURL}/ClothingItems`;
  #getClothingItemsByType = (type_id) => `${this.#wardrobeServerBaseURL}/ClothingItems/ByType/${type_id}`;
  #getClothingItemByID = (item_id) => `${this.#wardrobeServerBaseURL}/ClothingItems/${item_id}`;
  #deleteClothingItemURL = (item_id) => `${this.#wardrobeServerBaseURL}/ClothingItems/${item_id}`;
  #updateClothingItemURL = (item_id) => `${this.#wardrobeServerBaseURL}/ClothingItems/${item_id}`;

  // ClothingType Endpoints
  #getClothingTypesURL = () => `${this.#wardrobeServerBaseURL}/ClothingTypes`;
  #addClothingTypesURL = () => `${this.#wardrobeServerBaseURL}/ClothingTypes`;
  #getClothingTypesByIDURL = (type_id) => `${this.#wardrobeServerBaseURL}/ClothingTypes/${type_id}`;
  #deleteClothingTypeURL = (type_id) => `${this.#wardrobeServerBaseURL}/ClothingTypes/${type_id}`;
  #updateClothingTypeURL = (type_id) => `${this.#wardrobeServerBaseURL}/ClothingTypes/${type_id}`;


  // Outfit endpoints
  #getOutfitsURL = () => `${this.#wardrobeServerBaseURL}/Outfits/`;
  #getOutfitByIDURL = (outfit_id) => `${this.#wardrobeServerBaseURL}/Outfits/${outfit_id}/`;
  #addOutfitURL = () => `${this.#wardrobeServerBaseURL}/Outfits/`;
  #deleteOutfitURL = (outfit_id) => `${this.#wardrobeServerBaseURL}/Outfits/${outfit_id}`;
  #updateOutfitURL = (outfit_id) => `${this.#wardrobeServerBaseURL}/Outfits/${outfit_id}`;
  #getCompatibleOutfitsURL = (wardrobe_id) => `${this.#wardrobeServerBaseURL}/Outfits/${wardrobe_id}`;

  // Style endpoints
  #getStylesURL = () => `${this.#wardrobeServerBaseURL}/Styles`;
  #getStyleByIdURL = (style_id) => `${this.#wardrobeServerBaseURL}/styles/${style_id}`;
  #addStyleURL = () => `${this.#wardrobeServerBaseURL}/Styles`;
  #updateStyleURL = (style_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}`;
  #deleteStyleURL = (style_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}`;

 // Constraint Endpoints
  #getConstraintsURL = (style_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/constraints`;
  #addConstraintURL = (style_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/constraints`;
  #updateConstraintURL = (style_id, constraint_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/constraints/${constraint_id}`;
  #deleteConstraintURL = (style_id, constraint_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/constraints/${constraint_id}`;


  // BinaryConstraint URLs
  #getBinaryConstraintsURL = (style_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/BinaryConstraints`;
  #addBinaryConstraintURL = (style_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/BinaryConstraints`;
  #updateBinaryConstraintURL = (style_id, constraint_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/BinaryConstraints/${constraint_id}`;
  #deleteBinaryConstraintURL = (style_id, constraint_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/BinaryConstraints/${constraint_id}`;

// UnaryConstraint URLs
  #getUnaryConstraintsURL = (style_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/UnaryConstraints`;
  #addUnaryConstraintURL = (style_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/UnaryConstraints`;
  #updateUnaryConstraintURL = (style_id, constraint_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/UnaryConstraints/${constraint_id}`;
  #deleteUnaryConstraintURL = (style_id, constraint_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/UnaryConstraints/${constraint_id}`;

// ImplicationConstraint URLs
  #getImplicationConstraintsURL = (style_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/ImplicationConstraints`;
  #addImplicationConstraintURL = (style_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/ImplicationConstraints`;
  #updateImplicationConstraintURL = (style_id, constraint_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/ImplicationConstraints/${constraint_id}`;
  #deleteImplicationConstraintURL = (style_id, constraint_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/ImplicationConstraints/${constraint_id}`;

// MutexConstraint URLs
  #getMutexConstraintsURL = (style_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/MutexConstraints`;
  #addMutexConstraintURL = (style_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/MutexConstraints`;
  #updateMutexConstraintURL = (style_id, constraint_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/MutexConstraints/${constraint_id}`;
  #deleteMutexConstraintURL = (style_id, constraint_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/MutexConstraints/${constraint_id}`;

// CardinalityConstraint URLs
  #getCardinalityConstraintsURL = (style_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/CardinalityConstraints`;
  #addCardinalityConstraintURL = (style_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/CardinalityConstraints`;
  #updateCardinalityConstraintURL = (style_id, constraint_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/CardinalityConstraints/${constraint_id}`;
  #deleteCardinalityConstraintURL = (style_id, constraint_id) => `${this.#wardrobeServerBaseURL}/Styles/${style_id}/CardinalityConstraints/${constraint_id}`;




    static getAPI() {
    if (this.#api == null) {
      this.#api = new DigitalWardrobeAPI();
    }
    return this.#api;
  }
  // Fetch-Helper-Methode
    #fetchAdvanced = (url, init) => fetch(url, init)
        .then(res => {
            if (!res.ok) {
                throw Error(`${res.status} ${res.statusText}`);
            }
            return res.json();
        });

// User Endpoints
// Methode nach der man einen User anhand der ID aus der Datenbank holt

    getUsers() {
        return this.#fetchAdvanced(this.#getUsersURL()).then((responseJSON) => {
            let userBO = UserBO.fromJSON(responseJSON);
            return new Promise(function(resolve) {
                resolve(userBO)
            })
        }
    )
    }


// Delete a user

    deleteUser(user_id) {
        return this.#fetchAdvanced(this.#deleteUsersURL(user_id), {
            method:'DELETE'

        }).then((responseJSON) => {

            let responseUserBO = UserBO.fromJSON(responseJSON)[0];

            return new Promise(function(resolve){
                resolve(responseUserBO);
            })
        })
    }

// Get user by Google ID

    getUserByGoogleId(user_id) {
    return this.#fetchAdvanced(this.#getUsersByGoogleIdURL(user_id)).then((responseJSON) => {
        let userBO = UserBO.fromJSON(responseJSON);
        return new Promise(function(resolve) {
                resolve(userBO)
            })
        }
    )
    }

// Update user by ID

    updateUser(userBO) {
    return this.#fetchAdvanced(this.#updateUsersURL(userBO.id), {
      method: 'PUT',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(userBO)
    }).then((responseJSON) => {
      // We always get an array of CustomerBOs.fromJSON
      let responseUserBO = UserBO.fromJSON(responseJSON)[0];
      // console.info(accountBOs);
      return new Promise(function (resolve) {
        resolve(responseUserBO);
      })
    })
  }

// Add a new user

    addUser(userBO) {
    return this.#fetchAdvanced(this.#addUsersURL(), {
        method: 'POST',
        credentials: 'include',
        headers: {
            'Accept': 'application/json, text/plain',
            'Content-type': 'application/json',
        },
        body: JSON.stringify(userBO)
    }).then((responseJSON) => {
        let responseUserBO = UserBO.fromJSON(responseJSON)[0];
        return new Promise(function (resolve) {
            resolve(responseUserBO);
        })
    })
}

// Wardrobe Endpoints
// Get wardrobe by userId

    getWardrobe() {
    return this.#fetchAdvanced(this.#getWardrobesURL()).then((responseJSON) => {
        let wardrobeBO = WardrobeBO.fromJSON(responseJSON);
        return new Promise (function (resolve) {
            resolve (wardrobeBO);
        })
    })
}

// Methode für das Abrufen der WardrobeId für die Google User ID
  getWardrobeIdByGoogleUserId(google_id) {
    return this.#fetchAdvanced(this.#getWardrobeIdByGoogleUserId(google_id))
      .then((responseJSON) => {
        // Hier anpassen, je nachdem wie die Daten strukturiert sind, aber
        // wir gehen davon aus, dass die `wardrobeId` vom Server zurückgegeben wird.
        return responseJSON.wardrobeId; // Beispiel, wie du die ID extrahierst
      });
  }

// Add a new wardrobe

    addWardrobe(wardrobeBO) {
    return this.#fetchAdvanced(this.#addWardrobeURL(), {
        method: 'POST',
        headers: {
            'Accept': 'application/json, text/plain',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(wardrobeBO)
    }).then(responseJSON => {
            return WardrobeBO.fromJSON(responseJSON)[0];
        });
    }

// Update wardrobe by ID

    updateWardrobe(wardrobeBO) {
        return this.#fetchAdvanced(this.#updateWardrobeURL(wardrobeBO.getId), {
            method: 'PUT',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(wardrobeBO)
        }).then(responseJSON => WardrobeBO.fromJSON(responseJSON)[0]);
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

    getClothingItems() {
    return this.#fetchAdvanced(this.#getClothingItemsURL()).then((responseJSON) => {
        let clothingItemsBO = ClothingItemBO.fromJSON(responseJSON);
        return Promise.resolve(clothingItemsBO);
    });
}

// Get clothing items by type (e.g., shirts, pants)

    getClothingItemsByType(type_id) {
    return this.#fetchAdvanced(this.#getClothingItemsByType(type_id)).then((responseJSON) => {
        let clothingItemsBO = ClothingItemBO.fromJSON(responseJSON);
        return Promise.resolve(clothingItemsBO);
    });
}

// Get a specific clothing item by its ID

    getClothingItemByID(item_id) {
    return this.#fetchAdvanced(this.#getClothingItemByID(item_id)).then((responseJSON) => {
        let clothingItemBO = ClothingItemBO.fromJSON(responseJSON);
        return Promise.resolve(clothingItemBO);
    });
}

// Add a new clothing item

    addClothingItem() {
    return this.#fetchAdvanced(this.#addClothingItemURL(), 'POST').then((responseJSON) => {
        let clothingItemBO = ClothingItemBO.fromJSON(responseJSON);
        return Promise.resolve(clothingItemBO);
    });
}

// Update a clothing item

    updateClothingItem(item_id) {
    return this.#fetchAdvanced(this.#updateClothingItemURL(item_id), 'PUT').then((responseJSON) => {
        let clothingItemBO = ClothingItemBO.fromJSON(responseJSON);
        return Promise.resolve(clothingItemBO);
    });
}

// Delete a clothing item

    deleteClothingItem(item_id) {
    return this.#fetchAdvanced(this.#deleteClothingItemURL(item_id)).then((responseJSON) => {
        // Rückgabe null, da DELETE keine Daten zurückgibt
        return Promise.resolve(null);
    });
}

// ClothingType Endpoints
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



//Outfit Endpoints
// Add an outfit for a user

    addOutfit(userId, outfitData) {
    return this.#fetchAdvanced(this.#addOutfitURL(userId), 'POST', outfitData).then((responseJSON) => {
        let outfitBO = OutfitBO.fromJSON(responseJSON);
        return Promise.resolve(outfitBO);
    });
}

// Get outfits for a user

    getOutfits(userId) {
    return this.#fetchAdvanced(this.#getOutfitsURL(userId)).then((responseJSON) => {
        let outfitsBOs = OutfitBO.fromJSON(responseJSON);
        return Promise.resolve(outfitsBOs);
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

// Styles Endpoints
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


// Constraint Endpoints

    getConstraints(style_id, type) {
    return this.#fetchAdvanced(this.#getConstraintsURL(style_id, type)).then((responseJSON) => {
        let constraints = ConstraintBO.fromJSON(responseJSON);
        return new Promise(function(resolve) {
            resolve(constraints);
        });
    });
}

    addConstraint(style_id, type, constraintData) {
    return this.#fetchAdvanced(this.#addConstraintURL(style_id, type), {
        method: 'POST',
        body: JSON.stringify(constraintData),
    }).then((responseJSON) => {
        let constraint = ConstraintBO.fromJSON(responseJSON);
        return new Promise(function(resolve) {
            resolve(constraint);
        });
    });
}



    updateConstraint(style_id, constraintId, type, constraintData) {
    return this.#fetchAdvanced(this.#updateConstraintURL(style_id, constraintId, type), {
        method: 'PUT',
        body: JSON.stringify(constraintData),
    }).then((responseJSON) => {
        let updatedConstraint = ConstraintBO.fromJSON(responseJSON);
        return new Promise(function(resolve) {
            resolve(updatedConstraint);
        });
    });
}

    deleteConstraint(styleId, constraintId, type) {
    return this.#fetchAdvanced(this.#deleteConstraintURL(styleId, constraintId, type), {
        method: 'DELETE',
    }).then((responseJSON) => {
        let deletedConstraint = ConstraintBO.fromJSON(responseJSON);
        return new Promise(function(resolve) {
            resolve(deletedConstraint);
        });
    });
}


// BinaryConstraint Endpoints

    getBinaryConstraints(styleId) {
    return this.#fetchAdvanced(this.#getBinaryConstraintsURL(styleId))
        .then(responseJSON => BinaryConstraintBO.fromJSON(responseJSON));
}


    addBinaryConstraint(styleId, binaryConstraintData) {
    return this.#fetchAdvanced(this.#addBinaryConstraintURL(styleId), {
        method: 'POST',
        body: JSON.stringify(binaryConstraintData),
    }).then(responseJSON => BinaryConstraintBO.fromJSON(responseJSON));
}


    updateBinaryConstraint(styleId, constraintId, binaryConstraintData) {
    return this.#fetchAdvanced(this.#updateBinaryConstraintURL(styleId, constraintId), {
        method: 'PUT',
        body: JSON.stringify(binaryConstraintData),
    }).then(responseJSON => BinaryConstraintBO.fromJSON(responseJSON));
}


    deleteBinaryConstraint(styleId, constraintId) {
    return this.#fetchAdvanced(this.#deleteBinaryConstraintURL(styleId, constraintId), {
        method: 'DELETE',
    }).then(responseJSON => BinaryConstraintBO.fromJSON(responseJSON));
}

// UnaryConstraint Endpoints

    getUnaryConstraints(styleId) {
    return this.#fetchAdvanced(this.#getUnaryConstraintsURL(styleId))
        .then(responseJSON => UnaryConstraintBO.fromJSON(responseJSON));
}


    addUnaryConstraint(styleId, unaryConstraintData) {
    return this.#fetchAdvanced(this.#addUnaryConstraintURL(styleId), {
        method: 'POST',
        body: JSON.stringify(unaryConstraintData),
    }).then(responseJSON => UnaryConstraintBO.fromJSON(responseJSON));
}


    updateUnaryConstraint(styleId, constraintId, unaryConstraintData) {
    return this.#fetchAdvanced(this.#updateUnaryConstraintURL(styleId, constraintId), {
        method: 'PUT',
        body: JSON.stringify(unaryConstraintData),
    }).then(responseJSON => UnaryConstraintBO.fromJSON(responseJSON));
}


    deleteUnaryConstraint(styleId, constraintId) {
    return this.#fetchAdvanced(this.#deleteUnaryConstraintURL(styleId, constraintId), {
        method: 'DELETE',
    }).then(responseJSON => UnaryConstraintBO.fromJSON(responseJSON));
}

// ImplicationConstraint Endpoints

    getImplicationConstraints(styleId) {
    return this.#fetchAdvanced(this.#getImplicationConstraintsURL(styleId))
        .then(responseJSON => ImplicationConstraintBO.fromJSON(responseJSON));
}


    addImplicationConstraint(styleId, implicationConstraintData) {
    return this.#fetchAdvanced(this.#addImplicationConstraintURL(styleId), {
        method: 'POST',
        body: JSON.stringify(implicationConstraintData),
    }).then(responseJSON => ImplicationConstraintBO.fromJSON(responseJSON));
}


    updateImplicationConstraint(styleId, constraintId, implicationConstraintData) {
    return this.#fetchAdvanced(this.#updateImplicationConstraintURL(styleId, constraintId), {
        method: 'PUT',
        body: JSON.stringify(implicationConstraintData),
    }).then(responseJSON => ImplicationConstraintBO.fromJSON(responseJSON));
}




    deleteImplicationConstraint(styleId, constraintId) {
    return this.#fetchAdvanced(this.#deleteImplicationConstraintURL(styleId, constraintId), {
        method: 'DELETE',
    }).then(responseJSON => ImplicationConstraintBO.fromJSON(responseJSON));
}

// MutexConstraint Endpoints

    getMutexConstraints(styleId) {
    return this.#fetchAdvanced(this.#getMutexConstraintsURL(styleId))
        .then(responseJSON => MutexConstraintBO.fromJSON(responseJSON));
}


    addMutexConstraint(styleId, mutexConstraintData) {
    return this.#fetchAdvanced(this.#addMutexConstraintURL(styleId), {
        method: 'POST',
        body: JSON.stringify(mutexConstraintData),
    }).then(responseJSON => MutexConstraintBO.fromJSON(responseJSON));
}


    updateMutexConstraint(styleId, constraintId, mutexConstraintData) {
    return this.#fetchAdvanced(this.#updateMutexConstraintURL(styleId, constraintId), {
        method: 'PUT',
        body: JSON.stringify(mutexConstraintData),
    }).then(responseJSON => MutexConstraintBO.fromJSON(responseJSON));
}


    deleteMutexConstraint(styleId, constraintId) {
    return this.#fetchAdvanced(this.#deleteMutexConstraintURL(styleId, constraintId), {
        method: 'DELETE',
    }).then(responseJSON => MutexConstraintBO.fromJSON(responseJSON));
}

// CardinalityConstraint Endpoints

    getCardinalityConstraints(styleId) {
    return this.#fetchAdvanced(this.#getCardinalityConstraintsURL(styleId))
        .then(responseJSON => CardinalityConstraintBO.fromJSON(responseJSON));
}


    addCardinalityConstraint(styleId, cardinalityConstraintData) {
    return this.#fetchAdvanced(this.#addCardinalityConstraintURL(styleId), {
        method: 'POST',
        body: JSON.stringify(cardinalityConstraintData),
    }).then(responseJSON => CardinalityConstraintBO.fromJSON(responseJSON));
}


    updateCardinalityConstraint(styleId, constraintId, cardinalityConstraintData) {
    return this.#fetchAdvanced(this.#updateCardinalityConstraintURL(styleId, constraintId), {
        method: 'PUT',
        body: JSON.stringify(cardinalityConstraintData),
    }).then(responseJSON => CardinalityConstraintBO.fromJSON(responseJSON));
}


    deleteCardinalityConstraint(styleId, constraintId) {
    return this.#fetchAdvanced(this.#deleteCardinalityConstraintURL(styleId, constraintId), {
        method: 'DELETE',
    }).then(responseJSON => CardinalityConstraintBO.fromJSON(responseJSON));
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
    }

}
export default DigitalWardrobeAPI

//API TESTEN
