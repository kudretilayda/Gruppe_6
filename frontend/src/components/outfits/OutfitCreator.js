import React, { useState } from 'react';
import { TextField, MenuItem, Select, InputLabel, FormControl, Button, Grid } from '@mui/material';

const OutfitCreator = () => {
  const [outfitName, setOutfitName] = useState('');
  const [outfitSize, setOutfitSize] = useState('');
  const [outfitColor, setOutfitColor] = useState('');
  const [outfitType, setOutfitType] = useState('');

  const handleOutfitSubmit = () => {
    const newOutfit = {
      outfitName,
      outfitSize,
      outfitColor,
      outfitType,
    };

    console.log('Neues Outfit:', newOutfit);
  };

  return (
    <form>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <TextField
            fullWidth
            label="Outfit Name"
            value={outfitName}
            onChange={(e) => setOutfitName(e.target.value)}
            variant="outlined"
          />
        </Grid>

        {/* Outfit-Größe Dropdown */}
        <Grid item xs={12}>
          <FormControl fullWidth variant="outlined">
            <InputLabel>Outfit Größe</InputLabel>
            <Select
              value={outfitSize}
              onChange={(e) => setOutfitSize(e.target.value)}
              label="Outfit Größe"
            >
              <MenuItem value="S">S</MenuItem>
              <MenuItem value="M">M</MenuItem>
              <MenuItem value="L">L</MenuItem>
              <MenuItem value="XL">XL</MenuItem>
            </Select>
          </FormControl>
        </Grid>

        {/* Outfit-Farbe Dropdown */}
        <Grid item xs={12}>
          <FormControl fullWidth variant="outlined">
            <InputLabel>Outfit Farbe</InputLabel>
            <Select
              value={outfitColor}
              onChange={(e) => setOutfitColor(e.target.value)}
              label="Outfit Farbe"
            >
              <MenuItem value="Rot">Rot</MenuItem>
              <MenuItem value="Blau">Blau</MenuItem>
              <MenuItem value="Grün">Grün</MenuItem>
            </Select>
          </FormControl>
        </Grid>

        {/* Outfit-Typ Dropdown */}
        <Grid item xs={12}>
          <FormControl fullWidth variant="outlined">
            <InputLabel>Outfit-Typ</InputLabel>
            <Select
              value={outfitType}
              onChange={(e) => setOutfitType(e.target.value)}
              label="Outfit-Typ"
            >
              <MenuItem value="Casual">Casual</MenuItem>
              <MenuItem value="Sportlich">Sportlich</MenuItem>
              <MenuItem value="Business">Business</MenuItem>
            </Select>
          </FormControl>
        </Grid>

        <Grid item xs={12}>
          <Button variant="contained" color="primary" onClick={handleOutfitSubmit}>
            Outfit erstellen
          </Button>
        </Grid>
      </Grid>
    </form>
  );
};

export default OutfitCreator;
