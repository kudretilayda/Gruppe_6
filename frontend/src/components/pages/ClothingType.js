import React, { useState, useEffect } from 'react';
import {Typography, Grid, Card, CardContent, Button, Dialog, DialogTitle, DialogContent, DialogActions, TextField, Chip,
  CardActions, IconButton, Box, Select, MenuItem, FormControl, InputLabel} from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';

const ClothingType = () => {
  const [clothingType, set_type] = useState([]);
  const [openDialog, setOpenDialog] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
    const [currentTypeIndex, setCurrentTypeIndex] = useState(null); // Track the index of the style being edited

  const [newType, setNewType] = useState({
    name: '',
    usage: ''
  });
  useEffect(() => {
    const saved = localStorage.getItem('clothingType');
    if (saved) {
      set_type(JSON.parse(saved));
    }
  }, []);

  const handleAddType = () => {
    const updated = [...clothingType, newType];
    set_type(updated);

    // Speichern der neuen Liste in localStorage
    localStorage.setItem('clothingType', JSON.stringify(updated));

    // Reset des Dialogs
    setOpenDialog(false);
    setNewType({ name: '', usage: '' });
  };

  const handleEditType = () => {
    const updated = [...clothingType];
    updated[currentTypeIndex] = newType;
    set_type(updated);

    // Speichern der aktualisierten Liste in localStorage
    localStorage.setItem('clothingType', JSON.stringify(updated));

    // Reset des Dialogs
    setOpenDialog(false);
    setIsEditing(false);
    setNewType({ name: '', usage: '' });
    setCurrentTypeIndex(null);
  };

  const handleDeleteType = (index) => {
    const updated = clothingType.filter((_, i) => i !== index);
    set_type(updated);

    // Speichern der aktualisierten Liste in localStorage
    localStorage.setItem('clothingType', JSON.stringify(updated));
  };

  const handleOpenEditDialog = (index) => {
    setIsEditing(true);
    setCurrentTypeIndex(index);
    setNewType(clothingType[index]);
    setOpenDialog(true);
  };
  return (
      <div className="CT">
        <Grid container spacing={3} alignItems="center" className="mb-4">
          <Grid item xs>
            <Typography variant="h4">Kleidungstypen</Typography>
          </Grid>
          <Grid item>
            <Button
                variant="contained"
                color="primary"
                onClick={() => setOpenDialog(true)}
            >
              Kleidungstyp hinzufügen
            </Button>
          </Grid>
        </Grid>

        <Grid container spacing={3}>
          {clothingType.map((ctype, index) => (
            <Grid item xs={12} sm={6} md={4} key={index}>
              <Card elevation={3}>
                <CardContent>
                  <Typography variant="h6">{ctype.name}</Typography>
                </CardContent>
                <Box display="flex" justifyContent="flex-end">
                  <IconButton
                    color="primary"
                    onClick={() => handleEditType(index)}
                  >
                    <EditIcon />
                  </IconButton>
                  <IconButton
                    color="secondary"
                    onClick={() => handleDeleteType(index)}
                  >
                    <DeleteIcon />
                  </IconButton>
                </Box>
              </Card>
            </Grid>
          ))}
        </Grid>

        <Dialog open={openDialog} onClose={() => setOpenDialog(false)}>
          <DialogTitle>{isEditing ? 'Kleidungstyp bearbeiten' : 'Neues Kleidungstyp hinzufügen'}</DialogTitle>
          <DialogContent>
            <TextField
              fullWidth
              margin="normal"
              label="Kleidungstyp"
              value={newType.name}
              onChange={(e) => setNewType({ ...newType, name: e.target.value })}
              required
            />
            <TextField
              fullWidth
              margin="normal"
              label="Verwendung"
              value={newType.ctype}
              onChange={(e) => setNewType({ ...newType, clothing_type: e.target.value })}
              >
            </TextField>
          </DialogContent>
          <DialogActions>
            <Button onClick={() => setOpenDialog(false)}>Abbrechen</Button>
            <Button
              onClick={isEditing ? handleEditType : handleAddType}
              color="primary"
            >
              {isEditing ? 'Ändern' : 'Hinzufügen'}
            </Button>
          </DialogActions>
        </Dialog>
      </div>
  );
};

export default ClothingType;
