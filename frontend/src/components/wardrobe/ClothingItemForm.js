import React, { useState } from 'react';
import { TextField, Button, Select, MenuItem } from '@mui/material';

const ClothingItemForm = ({ onAddItem }) => {
  const [type, setType] = useState('');
  const [usage, setUsage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (type && usage) {
      onAddItem({ type, usage });
      setType(''); // Formular zurücksetzen
      setUsage('');
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: '2rem' }}>
      <TextField
        label="Kleidungsstück"
        value={type}
        onChange={(e) => setType(e.target.value)}
        fullWidth
        required
        style={{ marginBottom: '1rem' }}
      />
      <Select
        value={usage}
        onChange={(e) => setUsage(e.target.value)}
        displayEmpty
        fullWidth
        required
        style={{ marginBottom: '1rem' }}
      >
        <MenuItem value="" disabled>
          Nutzung auswählen
        </MenuItem>
        <MenuItem value="Freizeit">Freizeit</MenuItem>
        <MenuItem value="Arbeit">Arbeit</MenuItem>
        <MenuItem value="Sport">Sport</MenuItem>
      </Select>
      <Button type="submit" variant="contained" color="primary" fullWidth>
        Hinzufügen
      </Button>
    </form>
  );
};

export default ClothingItemForm;
