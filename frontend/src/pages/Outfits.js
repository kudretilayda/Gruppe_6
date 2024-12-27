// src/pages/OutfitsPage.js
import React, { useState } from 'react';
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
  Select,
  MenuItem,
  FormControl,
  InputLabel
} from '@material-ui/core';

const OutfitsPage = () => {
  const [outfits, setOutfits] = useState([]);
  const [openDialog, setOpenDialog] = useState(false);
  const [selectedStyle, setSelectedStyle] = useState('');

  const handleCreateOutfit = () => {
    // Hier würde normalerweise die Logik zur Outfit-Generierung basierend auf dem Style kommen
    const newOutfit = {
      style: selectedStyle,
      items: ['Blaue Jeans', 'Weißes T-Shirt', 'Schwarze Sneaker'] // Beispielitems
    };

    setOutfits([...outfits, newOutfit]);
    setOpenDialog(false);
    setSelectedStyle('');
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
            <Card>
              <CardContent>
                <Typography variant="h6">Outfit {index + 1}</Typography>
                <Typography color="textSecondary">Style: {outfit.style}</Typography>
                <Typography variant="subtitle2" className="mt-2">Enthaltene Items:</Typography>
                {outfit.items.map((item, i) => (
                  <Typography key={i}>• {item}</Typography>
                ))}
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>

      <Dialog open={openDialog} onClose={() => setOpenDialog(false)}>
        <DialogTitle>Neues Outfit erstellen</DialogTitle>
        <DialogContent>
          <FormControl fullWidth margin="normal">
            <InputLabel>Style auswählen</InputLabel>
            <Select
              value={selectedStyle}
              onChange={(e) => setSelectedStyle(e.target.value)}
            >
              <MenuItem value="Casual">Casual</MenuItem>
              <MenuItem value="Business">Business</MenuItem>
              <MenuItem value="Sport">Sport</MenuItem>
              <MenuItem value="Elegant">Elegant</MenuItem>
            </Select>
          </FormControl>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenDialog(false)}>Abbrechen</Button>
          <Button onClick={handleCreateOutfit} color="primary">Erstellen</Button>
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default OutfitsPage;