// Frontend API Service
import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:5000';

export const wardrobeService = {
    // Kleidungsstücke abrufen
    getItems: async (wardrobeId) => {
        try {
            const response = await axios.get(`${API_BASE_URL}/wardrobe/${wardrobeId}/items`);
            return response.data;
        } catch (error) {
            console.error('Fehler beim Abrufen der Kleidungsstücke:', error);
            throw error;
        }
    },

    // Kleidungsstück hinzufügen
    addItem: async (wardrobeId, itemData) => {
        try {
            const response = await axios.post(
                `${API_BASE_URL}/wardrobe/${wardrobeId}/items`,
                itemData
            );
            return response.data;
        } catch (error) {
            console.error('Fehler beim Hinzufügen des Kleidungsstücks:', error);
            throw error;
        }
    },

    // Style abrufen
    getStyle: async (styleId) => {
        try {
            const response = await axios.get(`${API_BASE_URL}/styles/${styleId}`);
            return response.data;
        } catch (error) {
            console.error('Fehler beim Abrufen des Styles:', error);
            throw error;
        }
    },

    // Outfit-Vorschläge erhalten
    getSuggestions: async (wardrobeId, styleId) => {
        try {
            const response = await axios.post(`${API_BASE_URL}/outfits/suggest`, {
                wardrobe_id: wardrobeId,
                style_id: styleId
            });
            return response.data;
        } catch (error) {
            console.error('Fehler beim Abrufen der Vorschläge:', error);
            throw error;
        }
    }
};