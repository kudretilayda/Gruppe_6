import React, { useEffect, useState } from 'react';
import { Button, Grid } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import { useNavigate } from 'react-router-dom';
import WardrobeAPI from '../API/DigitalWardrobeAPIAPI';
import ContextErrorMessage from './dialogs/ContextErrorMessage';
import LoadingProgress from './dialogs/LoadingProgress';
import OutfitBO from '../API/OutfitBO';
import OutfitForm from './dialogs/OutfitForm';
import OutfitCard from './layout/OutfitCard';
import { getAuth } from 'firebase/auth';

function OutfitList() {
    const [outfits, setOutfits] = useState([]);
    const [showAddForm, setShowAddForm] = useState(false);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [editOutfit, setEditOutfit] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        fetchOutfits();
    }, []);

    const fetchOutfits = async () => {
        setLoading(true);
        const auth = getAuth();
        const currentUser = auth.currentUser;
        try {
            const wardrobe_id = await WardrobeAPI.getAPI().getWardrobeIdByGoogleUserId(currentUser.uid);
            const outfits = await WardrobeAPI.getAPI().getOutfitsByWardrobeId(wardrobe_id.wardrobe_id);
            const outfitBOs = OutfitBO.fromJSON(outfits);
            setOutfits(outfitBOs);
            setLoading(false);
        } catch (error) {
            setError(error);
            setLoading(false);
        }
    };

    const handleAddButtonClick = () => {
        setShowAddForm(true);
        setEditOutfit(null);
    };

    const handleFormClose = (newOutfit) => {
        if (newOutfit) {
            fetchOutfits();
        }
        setShowAddForm(false);
    };

    const handleEditButtonClick = (outfit) => {
        const auth = getAuth();
        const currentUser = auth.currentUser;
        const creator = outfit.getCreator();
        if (currentUser.uid !== creator) {
            alert('You are not the creator of this outfit. You cannot edit it.');
            return;
        } else {
            setShowAddForm(true);
            setEditOutfit(outfit);
        }
    };

    const handleDeleteButtonClick = async (outfit) => {
        const auth = getAuth();
        const currentUser = auth.currentUser;
        const creator = outfit.getCreator();
        if (currentUser.uid !== creator) {
            alert('You are not the creator of this outfit. You cannot delete it.');
            return;
        } else {
            try {
                await WardrobeAPI.getAPI().deleteOutfit(outfit.getId());
                fetchOutfits();
            } catch (error) {
                setError(error);
            }
        }
    };

    const handleViewItemsButtonClick = (outfitId) => {
        navigate(`/outfits/items/${outfitId}`);
    };

    if (loading) {
        return <LoadingProgress show={true} />;
    }

    if (error) {
        return <ContextErrorMessage error={error} contextErrorMsg="Failed to load outfits." />;
    }

    return (
        <Grid container spacing={2} style={{ padding: 20, justifyContent: "center", alignItems: "center" }}>
            <Grid item xs={12} style={{ textAlign: 'center' }}>
                <Button
                    variant="contained"
                    color="primary"
                    startIcon={<AddIcon />}
                    onClick={handleAddButtonClick}
                    sx={{ width: '250px', height: '50px', p:1 }}
                >
                    Create new outfit
                </Button>
            </Grid>
            {outfits.map((outfit) => (
                <Grid 
                    item 
                    xs={12} 
                    sm={8} 
                    md={8} 
                    key={outfit.getId()}
                >
                    <OutfitCard
                        outfit={outfit}
                        onEdit={handleEditButtonClick}
                        onDelete={handleDeleteButtonClick}
                        onViewItems={handleViewItemsButtonClick}
                    />
                </Grid>
            ))}
            {showAddForm && (
                <OutfitForm
                    show={showAddForm}
                    outfit={editOutfit}
                    onClose={handleFormClose}
                />
            )}
        </Grid>
    );
}

export default OutfitList;
