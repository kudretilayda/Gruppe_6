import React, { useState, useEffect } from 'react';
import { Dialog, DialogActions, DialogContent, DialogTitle, Button, TextField, Grid } from '@mui/material';
import ClothingItemBO from '../API/ClothingItemBO';
import DigitalWardrobeAPI from "../../api/DigitalWardrobeAPI"; // Modell für Kleidungsstücke

function ClothingItemForm({ show, item, onClose, wardrobeId }) {
    const [designation, setDesignation] = useState('');
    const [size, setSize] = useState('');
    const [color, setColor] = useState('');
    const [quantity, setQuantity] = useState(1);

    useEffect(() => {
        if (item) {
            setDesignation(item.getDesignation());
            setSize(item.getSize());
            setColor(item.getColor());
            setQuantity(item.getQuantity());
        }
    }, [item]);

    const handleSave = async () => {
        try {
            if (item) {
                // Update existing clothing item
                await WardrobeAPI.getAPI().updateClothingItem(item.getId(), designation, size, color, quantity, wardrobeId);
            } else {
                // Add new clothing item
                await WardrobeAPI.getAPI().addClothingItem(designation, size, color, quantity, wardrobeId);
            }
            onClose(true); // Notify parent that the form is closed
        } catch (error) {
            console.error('Error saving clothing item:', error);
        }
    };

    const handleClose = () => {
        onClose(false); // Notify parent that the form is closed
    };

    return (
        <Dialog open={show} onClose={handleClose}>
            <DialogTitle>{item ? 'Edit Clothing Item' : 'Add Clothing Item'}</DialogTitle>
            <DialogContent>
                <Grid container spacing={2}>
                    <Grid item xs={12}>
                        <TextField
                            label="Designation (e.g. T-Shirt)"
                            fullWidth
                            value={designation}
                            onChange={(e) => setDesignation(e.target.value)}
                        />
                    </Grid>
                    <Grid item xs={12}>
                        <TextField
                            label="Size (e.g. M, L)"
                            fullWidth
                            value={size}
                            onChange={(e) => setSize(e.target.value)}
                        />
                    </Grid>
                    <Grid item xs={12}>
                        <TextField
                            label="Color"
                            fullWidth
                            value={color}
                            onChange={(e) => setColor(e.target.value)}
                        />
                    </Grid>
                    <Grid item xs={12}>
                        <TextField
                            label="Quantity"
                            type="number"
                            fullWidth
                            value={quantity}
                            onChange={(e) => setQuantity(e.target.value)}
                        />
                    </Grid>
                </Grid>
            </DialogContent>
            <DialogActions>
                <Button onClick={handleClose} color="secondary">Cancel</Button>
                <Button onClick={handleSave} color="primary">{item ? 'Save' : 'Add'}</Button>
            </DialogActions>
        </Dialog>
    );
}

export default ClothingItemForm;
