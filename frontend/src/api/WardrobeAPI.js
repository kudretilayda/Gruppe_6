// src/API/WardrobeAPI.js

const getAllClothes = async () => {
    // Beispiel für eine API-Abfrage, dies muss je nach Backend angepasst werden.
    const response = await fetch('/api/clothes');
    return await response.json();
};

const WardrobeAPI = {
    getAllClothes,
};

export default WardrobeAPI;
