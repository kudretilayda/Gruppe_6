// src/api/ClothingAPI.js
class ClothingAPI {
  static async getWardrobe(userId) {
    const response = await fetch(`/api/wardrobe/${userId}`);
    return response.json();
  }

  static async addClothingItem(userId, item) {
    const response = await fetch(`/api/wardrobe/${userId}/items`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(item),
    });
    return response.json();
  }

  static async getStyles(userId) {
    const response = await fetch(`/api/styles/${userId}`);
    return response.json();
  }

  static async createOutfit(userId, styleId) {
    const response = await fetch(`/api/outfits/${userId}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ styleId }),
    });
    return response.json();
  }
}

export default ClothingAPI;