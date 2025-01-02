import React from 'react';
import { Card, CardContent, CardActions, Typography, Button } from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';

function ClothingItemCard({ clothingItem, onEdit, onDelete }) {
    return (
        <Card sx={{ width: '100%', height: '100%' }}>
            <CardContent>
                <Typography variant="h6" component="div">
                    {clothingItem.getDesignation()} ({clothingItem.getSize()})
                </Typography>
                <Typography variant="body2" color="text.secondary">
                    Color: {clothingItem.getColor()}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                    Quantity: {clothingItem.getQuantity()}
                </Typography>
            </CardContent>
            <CardActions>
                <Button size="small" color="primary" onClick={() => onEdit(clothingItem)}>
                    <EditIcon />
                    Edit
                </Button>
                <Button size="small" color="secondary" onClick={() => onDelete(clothingItem)}>
                    <DeleteIcon />
                    Delete
                </Button>
            </CardActions>
        </Card>
    );
}

export default ClothingItemCard;
