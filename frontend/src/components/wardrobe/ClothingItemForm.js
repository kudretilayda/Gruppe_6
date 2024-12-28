import React, { useState } from 'react';
import { TextField, MenuItem, Select, InputLabel, FormControl, Button, Grid } from '@mui/material';

const ClothingItemForm = () => {
  const [size, setSize] = useState('');
  const [color, setColor] = useState('');
  const [itemType, setItemType] = useState('');
  const [itemName, setItemName] = useState('');

  const handleSizeChange = (event) => {
    setSize(event.target.value);
  };

  const handleColorChange = (event) => {
    setColor(event.target.value);
  };

  const handleItemTypeChange = (event) => {
    setItemType(event.target.value);
  };

  const handleSubmit = () => {
    // Hier kannst du den neuen Kleidungseintrag speichern, z.B. in localStorage
    const newClothingItem = {
      name: itemName,
      size,
      color,
      itemType,
    };

    console.log(newClothingItem);
    // Optional: localStorage.setItem('clothingItems', JSON.stringify([...existingItems, newClothingItem]));
  };

  return (
    <form>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <TextField
            fullWidth
            label="Kleidungsstück Name"
            value={itemName}
            onChange={(e) => setItemName(e.target.value)}
            variant="outlined"
          />
        </Grid>

        {/* Größe Dropdown */}
        <Grid item xs={12}>
          <FormControl fullWidth variant="outlined">
            <InputLabel>Größe</InputLabel>
            <Select
              value={size}
              onChange={handleSizeChange}
              label="Größe"
            >
              <MenuItem value="S">S</MenuItem>
              <MenuItem value="M">M</MenuItem>
              <MenuItem value="L">L</MenuItem>
              <MenuItem value="XL">XL</MenuItem>
              <MenuItem value="XXL">XXL</MenuItem>
            </Select>
          </FormControl>
        </Grid>

        {/* Farbe Dropdown */}
        <Grid item xs={12}>
          <FormControl fullWidth variant="outlined">
            <InputLabel>Farbe</InputLabel>
            <Select
              value={color}
              onChange={handleColorChange}
              label="Farbe"
            >
              <MenuItem value="Rot">Rot</MenuItem>
              <MenuItem value="Blau">Blau</MenuItem>
              <MenuItem value="Schwarz">Schwarz</MenuItem>
              <MenuItem value="Weiß">Weiß</MenuItem>
              <MenuItem value="Grün">Grün</MenuItem>
            </Select>
          </FormControl>
        </Grid>

        {/* Kleidungsstück-Typ Dropdown */}
        <Grid item xs={12}>
          <FormControl fullWidth variant="outlined">
            <InputLabel>Kleidungsstück-Typ</InputLabel>
            <Select
              value={itemType}
              onChange={handleItemTypeChange}
              label="Kleidungsstück-Typ"
            >
              <MenuItem value="T-Shirt">T-Shirt</MenuItem>
              <MenuItem value="Hose">Hose</MenuItem>
              <MenuItem value="Jacke">Jacke</MenuItem>
              <MenuItem value="Hemd">Hemd</MenuItem>
              <MenuItem value="Pullover">Pullover</MenuItem>
            </Select>
          </FormControl>
        </Grid>

        {/* Submit Button */}
        <Grid item xs={12}>
          <Button variant="contained" color="primary" onClick={handleSubmit}>
            Kleidungsstück hinzufügen
          </Button>
        </Grid>
      </Grid>
    </form>
  );
};

export default ClothingItemForm;
