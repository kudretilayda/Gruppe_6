import React, { useState } from 'react';
import { FormControl, InputLabel, Select, MenuItem } from '@mui/material';

const ClothingItemForm = () => {
  const [clothingItem, setClothingItem] = useState({
    type: '',
    color: '',
    size: ''
  });

  return (
    <form>
      <FormControl fullWidth margin="normal">
        <InputLabel>Kleidungsstück-Typ</InputLabel>
        <Select
          value={clothingItem.type}
          onChange={(e) => setClothingItem({ ...clothingItem, type: e.target.value })}
        >
          <MenuItem value="Shirt">Shirt</MenuItem>
          <MenuItem value="Pants">Pants</MenuItem>
          <MenuItem value="Jacket">Jacket</MenuItem>
        </Select>
      </FormControl>

      <FormControl fullWidth margin="normal">
        <InputLabel>Größe</InputLabel>
        <Select
          value={clothingItem.size}
          onChange={(e) => setClothingItem({ ...clothingItem, size: e.target.value })}
        >
          <MenuItem value="S">S</MenuItem>
          <MenuItem value="M">M</MenuItem>
          <MenuItem value="L">L</MenuItem>
        </Select>
      </FormControl>
    </form>
  );
};

export default ClothingItemForm;
