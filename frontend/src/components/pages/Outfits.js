import React, { useState, useEffect } from 'react';
import {Typography, Grid, Card, CardContent, Button, Dialog, DialogTitle, DialogContent, DialogActions, TextField, Chip,
  CardActions, IconButton, Box, Select, MenuItem, FormControl, InputLabel} from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import Wardrobe from "./Wardrobe";

const Outfits = ({ wardrobeItems = [], styles = [] }) => {
  const [outfits, setOutfits] = useState([]);
  const [openDialog, setOpenDialog] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [currentOutfitIndex, setCurrentOutfitIndex] = useState(null);
  const [newOutfit, setNewOutfit] = useState({
    outfit_name: '',
    items: [],
    style: null,
  });

  // Load saved outfits on component mount
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
    setNewOutfit({ outfit_name: '', items: [], style: null });
  };

  const handleEditOutfit = () => {
    const updated = [...outfits];
    updated[currentOutfitIndex] = newOutfit;
    setOutfits(updated);
    localStorage.setItem('outfits', JSON.stringify(updated));
    setOpenDialog(false);
    setIsEditing(false);
    setNewOutfit({ outfit_name: '', items: [], style: null });
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
                <Typography variant="h6">{outfit.outfit_name}</Typography>
                <Typography color="textSecondary" paragraph>
                  Style: {outfit.style ? outfit.style.features : 'Kein Style ausgewählt'}
                </Typography>
                <Box display="flex" flexWrap="wrap">
                  {outfit.items.map((item, i) => (
                    <Chip
                      key={i}
                      label={wardrobeItems.find((wi) => wi.id === item)?.item_name}
                      style={{
                        margin: '0.25rem',
                        backgroundColor: '#e0e0e0',
                        color: '#333',
                        borderRadius: '16px',
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

      <Dialog open={openDialog} onClose={() => setOpenDialog(false)}>
        <DialogTitle>{isEditing ? 'Outfit bearbeiten' : 'Neues Outfit erstellen'}</DialogTitle>
        <DialogContent>
          <TextField
            fullWidth
            margin="normal"
            label="Name des Outfits"
            value={newOutfit.outfit_name}
            onChange={(e) => setNewOutfit({ ...newOutfit, outfit_name: e.target.value })}
            required
          />
          <FormControl fullWidth margin="normal">
            <InputLabel>Style</InputLabel>
            <Select
              value={newOutfit.style || ''}
              onChange={(e) => setNewOutfit({ ...newOutfit, style: styles.find((s) => s.id === e.target.value) })}
              required
            >
              {styles.map((style) => (
                <MenuItem key={style.id} value={style.id}>
                  {style.features}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
          <FormControl fullWidth margin="normal">
            <InputLabel>Kleidungsstücke</InputLabel>
            <Select
              multiple
              value={newOutfit.items}
              onChange={(e) => setNewOutfit({ ...newOutfit, items: e.target.value })}
              renderValue={(selected) =>
                selected.map((id) => wardrobeItems.find((wi) => wi.id === id)?.item_name || 'Unbekannt').join(', ')
              }
              required
            >
              {wardrobeItems.map((item) => (
                <MenuItem key={item.id} value={item.id}>
                  {item.item_name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenDialog(false)}>Abbrechen</Button>
          <Button
            onClick={isEditing ? handleEditOutfit : handleAddOutfit}
            color="primary"
          >
            {isEditing ? 'Ändern' : 'Erstellen'}
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default Outfits;
