import React from 'react';
import { Button, Card, CardContent, CardActions, Typography } from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import PropTypes from 'prop-types';

/**Optische Anpassungen für die Kleidungsstücke im digitalen Kleiderschrank */

const WardrobeEntryCard = ({ entry, onEdit, onDelete }) => (
    <Card>
        <CardContent>
            <Typography variant="h5">{entry.getItemName()}</Typography>
            <Typography color="textSecondary">
                Size: {entry.getSize()} <br />
                Quantity: {entry.getQuantity()}
            </Typography>
        </CardContent>
        <CardActions>
            <Button size="small" startIcon={<EditIcon />} onClick={() => onEdit(entry)}>Edit</Button>
            <Button size="small" startIcon={<DeleteIcon />} onClick={() => onDelete(entry.getItemName())}>Delete</Button>
        </CardActions>
    </Card>
);

WardrobeEntryCard.propTypes = {
    entry: PropTypes.object.isRequired, // Das Kleidungsstück-Objekt
    onEdit: PropTypes.func.isRequired, // Funktion zum Bearbeiten des Kleidungsstücks
    onDelete: PropTypes.func.isRequired // Funktion zum Löschen des Kleidungsstücks
};

export default WardrobeEntryCard;
