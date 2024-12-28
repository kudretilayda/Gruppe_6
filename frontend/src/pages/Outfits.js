import React, { useState, useEffect } from 'react';
import {
  Typography,
  Grid,
  Card,
  CardContent,
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  Chip,
  CardActions,
  IconButton,
  Box
} from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';

const Outfits = () => {
  const [outfits, setOutfits] = useState([]);
  const [openDialog, setOpenDialog] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [currentOutfitIndex, setCurrentOutfitIndex] = useState(null);
  const [newOutfit, setNewOutfit] = useState({
    name: '',
    description: '',
    items: [] // Kleidung, die zu diesem Outfit gehört
  });

  // Lädt gespeicherte Outfits beim Start der Seite
  useEffect(() => {
    const saved = localStorage.getItem('outfits');
    if (saved) {
      setOutfits(JSON.parse(saved));
    }
  }, []);

  const handleAddOutfit = () => {
    const updated = [...outfits, newOutfit];
    setOutfits(updated);
    localStorage.setItem('outfits', JSON.stringify(updated));
    setOpenDialog(false);
    setNewOutfit({ name: '', description: '', items: [] });
  };

  const handleEditOutfit = () => {
    const updated = [...outfits];
    updated[currentOutfitIndex] = newOutfit;
    setOutfits(updated);
    localStorage.setItem('outfits', JSON.stringify(updated));
    setOpenDialog(false);
    setIsEditing(false);
    setNewOutfit({ name: '', description: '', items: [] });
    setCurrentOutfitIndex(null);
  };

  const handleDeleteOutfit = (index) => {
    const updated = outfits.filter((_, i) => i !== index);
    setOutfits(updated);
    localStorage.setItem('outfits', JSON.stringify(updated));
  };

  const handleOpenEditDialog = (index) => {
    setIsEditing(true);
    setCurrentOutfitIndex(index);
    setNewOutfit(outfits[index]);
    setOpenDialog(true);
  };

  
