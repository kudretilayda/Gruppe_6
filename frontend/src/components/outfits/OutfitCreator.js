import React, { useState } from 'react';
import { FormControl, InputLabel, Select, MenuItem, TextField, Button } from '@mui/material';

const sizes = ['XS', 'S', 'M', 'L', 'XL'];
const shoeSizes = ['36', '37', '38', '39', '40'];
const cupSizes = ['A', 'B', 'C', 'D'];
const bandSizes = ['70', '75', '80', '85'];
const colors = ['Red', 'Blue', 'Green', 'Black', 'White'];

const OutfitCreator = () => {
  const [newClothing, setNewClothing] = useState({
    type: '',
    color: '',
    size: '',
    shoeSize: '',
    cupSize: '',
    bandSize: ''
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    // Logik zum Absenden des Outfits
    console.log(newClothing);
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Kleidungsstück-Typ */}
      <FormControl fullWidth margin="normal">
        <InputLabel>Kleidungsstück-Typ</InputLabel>
        <Select
          label="Kleidungsstück-Typ"
          value={newClothing.type}
          onChange={(e) => setNewClothing({ ...newClothing, type: e.target.value })}
          required
        >
          <MenuItem value="Shirt">Shirt</MenuItem>
          <MenuItem value="Pants">Pants</MenuItem>
          <MenuItem value="Jacket">Jacket</MenuItem>
          <MenuItem value="Shoes">Shoes</MenuItem>
          <MenuItem value="Underwear">Underwear</MenuItem>
        </Select>
      </FormControl>

      {/* Größe */}
      <FormControl fullWidth margin="normal">
        <InputLabel>Größe</InputLabel>
        <Select
          label="Größe"
          value={newClothing.size}
          onChange={(e) => setNewClothing({ ...newClothing, size: e.target.value })}
        >
          {sizes.map((size) => (
            <MenuItem key={size} value={size}>
              {size}
            </MenuItem>
          ))}
        </Select>
      </FormControl>

      {/* Schuhgröße - Nur für Schuhe */}
      {newClothing.type.toLowerCase().includes('shoes') && (
        <FormControl fullWidth margin="normal">
          <InputLabel>Schuhgröße</InputLabel>
          <Select
            label="Schuhgröße"
            value={newClothing.shoeSize}
            onChange={(e) => setNewClothing({ ...newClothing, shoeSize: e.target.value })}
          >
            {shoeSizes.map((size) => (
              <MenuItem key={size} value={size}>
                {size}
              </MenuItem>
            ))}
          </Select>
        </FormControl>
      )}

      