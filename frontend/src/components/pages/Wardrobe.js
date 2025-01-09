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
  IconButton,
  Box
} from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';

const Wardrobe = () => {
  const [wardrobe, setWardrobe] = useState([]);
  const [openDialog, setOpenDialog] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [currentClothingIndex, setCurrentClothingIndex] = useState(null);
  const [newClothing, setNewClothing] = useState({
    item_name: '',
    clothing_type: null,
    wardrobe_id: 0,
  });

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
    setNewClothing({ item_name: '', clothing_type: '', wardrobe_id: 0 });
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
    setNewClothing({ item_name: '', clothing_type: '', wardrobe_id: 0 });
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
                  <Typography variant="h6">{clothing.item_name}</Typography>
                  <Typography color="textSecondary" paragraph>
                    Typ: {clothing.clothing_type} | Kleiderschrank ID: {clothing.wardrobe_id}
                  </Typography>
                </CardContent>
                <Box display="flex" justifyContent="flex-end">
                  <IconButton
                    color="primary"
                    onClick={() => handleEditClothing(index)}
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
              label="Name des Kleidungsstücks"
              value={newClothing.item_name}
              onChange={(e) => setNewClothing({ ...newClothing, item_name: e.target.value })}
              required
            />
            <TextField
              fullWidth
              margin="normal"
              label="Typ des Kleidungsstücks"
              value={newClothing.clothing_type}
              onChange={(e) => setNewClothing({ ...newClothing, clothing_type: e.target.value })}
              required
            />
            <TextField
              fullWidth
              margin="normal"
              label="Kleiderschrank ID"
              type="number"
              value={newClothing.wardrobe_id}
              onChange={(e) => setNewClothing({ ...newClothing, wardrobe_id: parseInt(e.target.value, 10) })}
              required
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