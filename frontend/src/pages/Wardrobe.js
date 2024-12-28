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
  MenuItem,
  Select,
  FormControl,
  InputLabel,
  IconButton,
  Box
} from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';

const Wardrobe = () => {
  const [wardrobe, setWardrobe] = useState([
    { id: 1, type: 'Shirt', color: 'blue', size: 'M' },
    { id: 2, type: 'Pants', color: 'black', size: 'M' },
    { id: 3, type: 'Jacket', color: 'green', size: 'L' }
  ]);
  const [styles, setStyles] = useState([
    { id: 1, name: 'Casual Look', requiredItems: ['Shirt', 'Pants'] },
    { id: 2, name: 'Business Look', requiredItems: ['Shirt', 'Pants', 'Jacket'] }
  ]);

  const [openDialog, setOpenDialog] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [currentClothingIndex, setCurrentClothingIndex] = useState(null);
  const [newClothing, setNewClothing] = useState({
    type: '',
    color: '',
    size: '',
    material: '',
    season: '',
    shoeSize: '',
    cupSize: '',
    bandSize: '',
    otherColor: ''
  });

  const sizes = ['XS', 'S', 'M', 'L', 'XL', 'XXL'];
  const shoeSizes = Array.from({ length: 14 }, (_, i) => 35 + i); // Schuhgrößen von 35 bis 48
  const cupSizes = ['A', 'B', 'C', 'D'];
  const bandSizes = ['60', '65', '70', '75', '80', '85', '90', '95'];
  const colors = ['Red', 'Blue', 'Green', 'Black', 'White', 'Yellow', 'Pink', 'Purple', 'Gray', 'Orange'];

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
    setNewClothing({ type: '', color: '', size: '', material: '', season: '', shoeSize: '', cupSize: '', bandSize: '', otherColor: '' });
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
    setNewClothing({ type: '', color: '', size: '', material: '', season: '', shoeSize: '', cupSize: '', bandSize: '', otherColor: '' });
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

  return (
    <div className="p-4">
      <Grid container spacing={3} alignItems="center" className="mb-4">
        <Grid item xs>
          <Typography variant="h4">Mein Kleiderschrank</Typography>
        </Grid>
        <Grid item>
          <Button
            variant="contained"
            color="primary"
            onClick={() => setOpenDialog(true)}
          >
            Kleidungsstück hinzufügen
          </Button>
        </Grid>
      </Grid>

      <Grid container spacing={3}>
        {wardrobe.map((clothing, index) => (
          <Grid item xs={12} sm={6} md={4} key={index}>
            <Card elevation={3}>
              <CardContent>
                <Typography variant="h6">{clothing.type}</Typography>
                <Typography color="textSecondary" paragraph>
                  {clothing.color} | {clothing.size} | {clothing.material} | {clothing.season}
                </Typography>
              </CardContent>
              <Box display="flex" justifyContent="flex-end">
                <IconButton
                  color="primary"
                  onClick={() => handleOpenEditDialog(index)}
                >
                  <EditIcon />
                </IconButton>
                <IconButton
                  color="secondary"
                  onClick={() => handleDeleteClothing(index)}
                >
                  <DeleteIcon />
                </IconButton>
              </Box>
            </Card>
          </Grid>
        ))}
      </Grid>

      <Dialog open={openDialog} onClose={() => setOpenDialog(false)}>
        <DialogTitle>{isEditing ? 'Kleidungsstück bearbeiten' : 'Neues Kleidungsstück hinzufügen'}</DialogTitle>
        <DialogContent>
          <TextField
            fullWidth
            margin="normal"
            label="Kleidungsstück-Typ"
            value={newClothing.type}
            onChange={(e) => setNewClothing({ ...newClothing, type: e.target.value })}
            required
          />
          <TextField
            fullWidth
            margin="normal"
            label="Farbe"
            value={newClothing.color}
            onChange={(e) => setNewClothing({ ...newClothing, color: e.target.value })}
            required
          />

          <FormControl fullWidth margin="normal">
            <InputLabel>Größe</InputLabel>
            <Select
              label="Größe"
              value={newClothing.size}
              onChange={(e) => setNewClothing({ ...newClothing, size: e.target.value })}
              required
            >
              {sizes.map((size) => (
                <MenuItem key={size} value={size}>
                  {size}
                </MenuItem>
              ))}
            </Select>
          </FormControl>

          {/* Zusätzliche Optionen für Unterwäsche (Körbchen- und Bandgröße) */}
          {newClothing.type.toLowerCase().includes('unterwäsche') && (
            <>
              <FormControl fullWidth margin="normal">
                <InputLabel>Körbchengröße</InputLabel>
                <Select
                  label="Körbchengröße"
                  value={newClothing.cupSize}
                  onChange={(e) => setNewClothing({ ...newClothing, cupSize: e.target.value })}
                >
                  {cupSizes.map((cup) => (
                    <MenuItem key={cup} value={cup}>
                      {cup}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>

              <FormControl fullWidth margin="normal">
                <InputLabel>Bandgröße</InputLabel>
                <Select
                  label="Bandgröße"
                  value={newClothing.bandSize}
                  onChange={(e) => setNewClothing({ ...newClothing, bandSize: e.target.value })}
                >
                  {bandSizes.map((size) => (
                    <MenuItem key={size} value={size}>
                      {size}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </>
          )}

          {/* Schuhgrößen Auswahl */}
          {newClothing.type.toLowerCase().includes('schuhe') && (
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

          {/* Weitere Farben über Textfeld */}
          <TextField
            fullWidth
            margin="normal"
            label="Weitere Farbe"
            value={newClothing.otherColor}
            onChange={(e) => setNewClothing({ ...newClothing, otherColor: e.target.value })}
            helperText="Füge bei Bedarf eine andere Farbe hinzu"
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenDialog(false)}>Abbrechen</Button>
          <Button
            onClick={isEditing ? handleEditClothing : handleAddClothing}
            color="primary"
          >
            {isEditing ? 'Ändern' : 'Hinzufügen'}
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default Wardrobe;
