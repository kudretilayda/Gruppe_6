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

  return (
    <div className="p-4">
      <Grid container spacing={3} alignItems="center" className="mb-4">
        <Grid item xs>
          <Typography variant="h4">Meine Outfits</Typography>
        </Grid>
        <Grid item>
          <Button
            variant="contained"
            color="primary"
            onClick={() => setOpenDialog(true)}
          >
            Outfit erstellen
          </Button>
        </Grid>
      </Grid>

      <Grid container spacing={3}>
        {outfits.map((outfit, index) => (
          <Grid item xs={12} sm={6} md={4} key={index}>
            <Card elevation={3}>
              <CardContent>
                <Typography variant="h6">{outfit.name}</Typography>
                <Typography color="textSecondary" paragraph>
                  {outfit.description}
                </Typography>
                <Box display="flex" flexWrap="wrap">
                  {outfit.items.map((item, i) => (
                    <Chip
                      key={i}
                      label={item}
                      style={{
                        margin: '0.25rem',
                        backgroundColor: '#e0e0e0', // Leichte Hintergrundfarbe für Chips
                        color: '#333',
                        borderRadius: '16px'
                      }}
                    />
                  ))}
                </Box>
              </CardContent>
              <CardActions>
                <IconButton
                  color="primary"
                  onClick={() => handleOpenEditDialog(index)}
                >
                  <EditIcon />
                </IconButton>
                <IconButton
                  color="secondary"
                  onClick={() => handleDeleteOutfit(index)}
                >
                  <DeleteIcon />
                </IconButton>
              </CardActions>
            </Card>
          </Grid>
        ))}
      </Grid>

      
