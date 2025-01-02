import React, { useState, useEffect } from 'react';
import { Button, Grid } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import WardrobeEntryForm from './dialogs/WardrobeEntryForm'; // Form zum Hinzufügen/Bearbeiten von Kleidungsstücken
import ErrorMessage from './dialogs/ErrorMessage'; // Fehlermeldung
import LoadingSpinner from './dialogs/LoadingSpinner'; // Ladeindikator
import WardrobeEntryBO from '../API/WardrobeEntryBO'; // Business-Objekt für Kleiderschrank-Einträge
import { getAuth } from 'firebase/auth';
import WardrobeEntryCard from './layout/WardrobeEntryCard';
import DigitalWardrobeAPI from "../api/DigitalWardrobeAPI"; // Layout für die Anzeige von Kleidungsstücken

/**Übersicht aller Kleiderschrank-Einträge */

const WardrobeEntryList = () => {
    const [wardrobeEntries, setWardrobeEntries] = useState([]);
    const [showAddForm, setShowAddForm] = useState(false);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [editEntry, setEditEntry] = useState(null);

    useEffect(() => {
        fetchWardrobeEntries();
    }, []);

    //Läd alle Kleiderschrank-Einträge aus der DB
    const fetchWardrobeEntries = async () => {
        const auth = getAuth();
        const user = auth.currentUser;
        const wardrobe_id = await DigitalWardrobeAPI.getAPI().getWardrobeIdByGoogleUserId(user.uid);
        setLoading(true);
        try {
            const entries = await DigitalWardrobeAPI.getAPI().getWardrobeEntriesByWardrobeId(wardrobe_id.wardrobe_id);
            const wardrobeEntryBOs = WardrobeEntryBO.fromJSON(entries);
            setWardrobeEntries(wardrobeEntryBOs);
            setLoading(false);
        } catch (error) {
            console.error("Failed to fetch wardrobe entries:", error);
            setError(error);
            setLoading(false);
        }
    };

    const handleAddButtonClick = () => {
        setShowAddForm(true);
        setEditEntry(null);
    };

    const handleFormClose = (newEntry) => {
        if (newEntry) {
            fetchWardrobeEntries();
        }
        setShowAddForm(false);
    };

    const handleEditButtonClick = (entry) => {
        setShowAddForm(true);
        setEditEntry(entry);
    };

    const handleDeleteButtonClick = async (itemName) => {
        try {
            await DigitalWardrobeAPI.getAPI().deleteWardrobeEntry(itemName);
            fetchWardrobeEntries();
        } catch (error) {
            console.error("Failed to delete wardrobe entry:", error);
            setError(`Failed to delete entry: ${itemName}`);
        }
    };

    if (loading) {
        return <LoadingSpinner show={true} />;
    }

    if (error) {
        return <ErrorMessage error={error} contextErrorMsg="Failed to load wardrobe entries." />;
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
            {wardrobeEntries.map((entry) => (
                <Grid item xs={12} sm={6} md={4} key={entry.getId()}>
                    <WardrobeEntryCard
                        entry={entry}
                        onEdit={handleEditButtonClick}
                        onDelete={handleDeleteButtonClick}
                    />
                </Grid>
            ))}
            {showAddForm && (
                <WardrobeEntryForm
                    show={showAddForm}
                    wardrobeentry={editEntry}
                    onClose={handleFormClose}
                />
            )}
        </Grid>
    );
};

export default WardrobeEntryList;
