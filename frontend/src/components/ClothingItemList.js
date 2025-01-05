import React, { useState, useEffect } from 'react';
import { Button, Grid } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import DigitalWardrobeAPI from "../api/DigitalWardrobeAPI";
import ClothingItemForm from './dialogs/ClothingItemForm'; // Formular für Kleidung
import ErrorMessage from './dialogs/ErrorMessage';
import LoadingSpinner from './dialogs/LoadingSpinner';
import ClothingItemBO from '../API/ClothingItemBO'; // Business Object für Kleidung
import { getAuth } from 'firebase/auth';
import ClothingItemCard from './layout/ClothingItemCard'; // Layout-Komponente für Kleidung

/** Übersicht aller Kleidungsstücke im digitalen Kleiderschrank */

const ClothingItemList = () => {
    const [clothingItems, setClothingItems] = useState([]);
    const [showAddForm, setShowAddForm] = useState(false);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [editItem, setEditItem] = useState(null);

    useEffect(() => {
        fetchClothingItems();
    }, []);

    // Läd alle Kleidungsstücke aus der DB
    const fetchClothingItems = async () => {
        const auth = getAuth();
        const user = auth.currentUser;
        const wardrobe_id = await DigitalWardrobeAPI.getAPI().getWardrobeIdByGoogleUserId(user.uid); // Holen der WardrobeID des Benutzers
        setLoading(true);
        try {
            const items = await DigitalWardrobeAPI.getAPI().getClothingItemsByWardrobeId(wardrobe_id.wardrobe_id); // Holen der Kleidungsstücke
            const clothingItemBOs = ClothingItemBO.fromJSON(items); // Konvertieren der Antwort in BOs
            setClothingItems(clothingItemBOs);
            setLoading(false);
        } catch (error) {
            console.error("Failed to fetch clothing items:", error);
            setError(error);
            setLoading(false);
        }
    };

    // Handle Add Clothing Button Click
    const handleAddButtonClick = () => {
        setShowAddForm(true);
        setEditItem(null);
    };

    // Form schließen und neues Kleidungsstück laden, falls hinzugefügt
    const handleFormClose = (newItem) => {
        if (newItem) {
            fetchClothingItems();
        }
        setShowAddForm(false);
    };

    // Handle Edit Button Click
    const handleEditButtonClick = (item) => {
        setShowAddForm(true);
        setEditItem(item);
    };

    // Handle Delete Button Click
    const handleDeleteButtonClick = async (designation) => {
        try {
            await DigitalWardrobeAPI.getAPI().deleteClothingItem(designation); // Löschen des Kleidungsstücks
            fetchClothingItems(); // Aktualisieren der Liste nach Löschung
        } catch (error) {
            console.error("Failed to delete clothing item:", error);
            setError(`Failed to delete item: ${designation}`);
        }
    };

    if (loading) {
        return <LoadingSpinner show={true} />;
    }

    if (error) {
        return <ErrorMessage error={error} contextErrorMsg="Failed to load clothing items." />;
    }

    return (
        <Grid container spacing={2} style={{ padding: 20 }}>
            <Grid item xs={12} style={{ textAlign: 'center' }}>
                <Button
                    variant="contained"
                    color="primary"
                    startIcon={<AddIcon />}
                    onClick={handleAddButtonClick}
                    sx={{ width: '200px', height: '50px' }}
                >
                    Add Clothing
                </Button>
            </Grid>
            {clothingItems.map((item) => (
                <Grid item xs={12} sm={6} md={4} key={item.getId()}>
                    <ClothingItemCard
                        item={item}
                        onEdit={handleEditButtonClick}
                        onDelete={handleDeleteButtonClick}
                    />
                </Grid>
            ))}
            {showAddForm && (
                <ClothingItemForm
                    show={showAddForm}
                    clothingItem={editItem}
                    onClose={handleFormClose}
                />
            )}
        </Grid>
    );
};

export default ClothingItemList;
