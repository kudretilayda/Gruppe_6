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
  IconButton,
  Box
} from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';

const Wardrobe = () => {
  const [wardrobe, setWardrobe] = useState([]);
  const [openDialog, setOpenDialog] = useState(false);
  const [isEditing, setIsEditing] = useState(false); // Track if we're editing or adding
  const [currentClothingIndex, setCurrentClothingIndex] = useState(null); // Track the index of the clothing being edited
  const [newClothing, setNewClothing] = useState({
    type: '',
    color: '',
    size: '',
    material: '',
    season: ''
  });

  // Lädt gespeicherte Kleiderschrank-Daten beim Start der Seite
  useEffect(() => {
    const savedWardrobe = localStorage.getItem('wardrobe');
    if (savedWardrobe) {
      setWardrobe(JSON.parse(savedWardrobe));
    }
  }, []);

  const handleAddClothing = () => {
    const updatedWardrobe = [...wardrobe, newClothing];
    setWardrobe(updatedWardrobe);

    // Speichern des aktualisierten Kleiderschranks in localStorage
    localStorage.setItem('wardrobe', JSON.stringify(updatedWardrobe));

    // Reset des Dialogs
    setOpenDialog(false);
    setNewClothing({ type: '', color: '', size: '', material: '', season: '' });
  };

  const handleEditClothing = () => {
    const updatedWardrobe = [...wardrobe];
    updatedWardrobe[currentClothingIndex] = newClothing;
    setWardrobe(updatedWardrobe);

    // Speichern der aktualisierten Liste in localStorage
    localStorage.setItem('wardrobe', JSON.stringify(updatedWardrobe));

    // Reset des Dialogs
    setOpenDialog(false);
    setIsEditing(false);
    setNewClothing({ type: '', color: '', size: '', material: '', season: '' });
    setCurrentClothingIndex(null);
  };

  const handleDeleteClothing = (index) => {
    const updatedWardrobe = wardrobe.filter((_, i) => i !== index);
    setWardrobe(updatedWardrobe);

    // Speichern der aktualisierten Liste in localStorage
    localStorage.setItem('wardrobe', JSON.stringify(updatedWardrobe));
  };

  const handleOpenEditDialog = (index) => {
    setIsEditing(true);
    setCurrentClothingIndex(index);
    setNewClothing(wardrobe[index]);
    setOpenDialog(true);
  };

  
