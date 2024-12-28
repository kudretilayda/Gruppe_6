import React, { useState } from 'react';
import { TextField, Button, Select, MenuItem, FormControl, InputLabel, FormHelperText } from '@mui/material';

const ClothingItemForm = ({ onAddItem }) => {
  const [type, setType] = useState('');
  const [usage, setUsage] = useState('');
  const [color, setColor] = useState('');
  const [error, setError] = useState(false); // Zustand für Fehlerbehandlung

  const handleSubmit = (e) => {
    e.preventDefault();

    // Validierung, dass alle Felder ausgefüllt sind
    if (type && usage && color) {
      onAddItem({ type, usage, color });
      setType('');  // Formular zurücksetzen
      setUsage('');
      setColor('');
      setError(false); // Fehler zurücksetzen
    } else {
      setError(true); // Fehler anzeigen, wenn eines der Felder leer ist
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <TextField
        label="Kleidungsstück"
        value={type}
        onChange={(e) => setType(e.target.value)}
        fullWidth
        margin="normal"
        required // sorgt dafür, dass das Feld nicht leer gelassen werden kann
      />
      {/* Farbe Auswahl (Dropdown) */}
      <FormControl fullWidth margin="normal" required error={error && !color}>
        <InputLabel>Farbe</InputLabel>
        <Select
          value={color}
          onChange={(e) => setColor(e.target.value)}
          label="Farbe"  // Hier Label hinzufügen
        >
          <MenuItem value="Rot">Rot</MenuItem>
          <MenuItem value="Blau">Blau</MenuItem>
          <MenuItem value="Grün">Grün</MenuItem>
          <MenuItem value="Schwarz">Schwarz</MenuItem>
          <MenuItem value="Weiß">Weiß</MenuItem>
          <MenuItem value="Pink">Pink</MenuItem>
          <MenuItem value="Lila">Lila</MenuItem>
          <MenuItem value="Braun">Braun</MenuItem>
          <MenuItem value="Beige">Beige</MenuItem>
        </Select>
        {error && !color && <FormHelperText>Bitte eine Farbe auswählen</FormHelperText>} {/* Fehlermeldung anzeigen */}
      </FormControl>
      <TextField
        label="Verwendung"
        value={usage}
        onChange={(e) => setUsage(e.target.value)}
        fullWidth
        margin="normal"
        required
      />
      <Button type="submit" variant="contained" color="primary">
        Hinzufügen
      </Button>
    </form>
  );
};

export default ClothingItemForm;
