import React from 'react';
import { Card, CardContent, CardActions, Typography, Button } from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import PropTypes from 'prop-types';

/**Optische Anpassungen für Kleidungsstücke im digitalen Kleiderschrank */

function WardrobeEntryCard({ wardrobeEntry, onEdit, onDelete, isEntryAvailable }) {
    if (!wardrobeEntry) {
        return null;
    }

    return (
        <Card>
            <CardContent>
                <Typography variant="h5" style={{ color: isEntryAvailable(wardrobeEntry) ? 'black' : 'red' }}>
                    {wardrobeEntry.getItemName()}
                </Typography>
                <Typography color="textSecondary" style={{ color: isEntryAvailable(wardrobeEntry) ? 'black' : 'red' }}>
                    Size: {wardrobeEntry.getSize()} <br />
                    Quantity: {wardrobeEntry.getQuantity()}
                    {!isEntryAvailable(wardrobeEntry) && ' (Item not available)'}
                </Typography>
            </CardContent>
            <CardActions>
                <Button size="small" startIcon={<EditIcon />} onClick={() => onEdit(wardrobeEntry)}>Edit</Button>
                <Button size="small" startIcon={<DeleteIcon />} onClick={() => onDelete(wardrobeEntry)}>Delete</Button>
            </CardActions>
        </Card>
    );
}

WardrobeEntryCard.propTypes = {
    wardrobeEntry: PropTypes.object.isRequired, // Kleidungsstück-Objekt
    onEdit: PropTypes.func.isRequired, // Funktion zum Bearbeiten des Kleidungsstücks
    onDelete: PropTypes.func.isRequired, // Funktion zum Löschen des Kleidungsstücks
    isEntryAvailable: PropTypes.func.isRequired // Funktion zur Überprüfung der Verfügbarkeit des Kleidungsstücks
};

export default WardrobeEntryCard;
