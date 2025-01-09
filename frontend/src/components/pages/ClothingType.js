import React, { useState, useEffect } from 'react';
import {Typography, Grid, Card, CardContent, Button, Dialog, DialogTitle, DialogContent, DialogActions, TextField, Chip,
  CardActions, IconButton, Box, Select, MenuItem, FormControl, InputLabel} from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';

const ClothingType = () => {
  const [clothingType, set_type] = useState([]);
  const [openDialog, setOpenDialog] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [newType, setNewType] = useState({
    name: '',
    usage: ''
  });
  useEffect(() => {
    const saved = localStorage.getItem('Types');
    if (saved) {
      setTypes(JSON.parse(saved));
    }
  }, []);

  const handleAddType = () => {
    const updated = [...Types, newType];
    setTypes(updated);

    // Speichern der neuen Liste in localStorage
    localStorage.setItem('Types', JSON.stringify(updated));

    // Reset des Dialogs
    setOpenDialog(false);
    setNewType({ name: '', usage: '' });
  };

  const handleEditType = () => {
    const updated = [...Types];
    updated[currentTypeIndex] = newType;
    setTypes(updated);

    // Speichern der aktualisierten Liste in localStorage
    localStorage.setItem('Types', JSON.stringify(updated));

    // Reset des Dialogs
    setOpenDialog(false);
    setIsEditing(false);
    setNewType({ name: '', usage: '' });
    setCurrentTypeIndex(null);
  };

  const handleDeleteType = (index) => {
    const updated = Types.filter((_, i) => i !== index);
    setTypes(updated);

    // Speichern der aktualisierten Liste in localStorage
    localStorage.setItem('Types', JSON.stringify(updated));
  };

  const handleOpenEditDialog = (index) => {
    setIsEditing(true);
    setCurrentTypeIndex(index);
    setNewType(Types[index]);
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
                  <Typography color="textSecondary" paragraph>
                    Typ: {ctype.usage}
                  </Typography>
                </CardContent>
                <Box display="flex" justifyContent="flex-end">
                  <IconButton
                    color="primary"
                    onClick={() => handleAddctype(index)}
                  >
                    <EditIcon />
                  </IconButton>
                  <IconButton
                    color="secondary"
                    onClick={() => handleDeletectype(index)}
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
              label="Name des Kleidungstyp"
              value={newctype.name}
              onChange={(e) => setNewctype({ ...newctype, name: e.target.value })}
              required
            />
            <TextField
              fullWidth
              margin="normal"
              label="Typ des Kleidungstyp"
              value={newctype.ctype_type}
              onChange={(e) => setNewctype({ ...newctype, clothing_type: e.target.value })}
              required>
            </TextField>
          </DialogContent>
          <DialogActions>
            <Button onClick={() => setOpenDialog(false)}>Abbrechen</Button>
            <Button
              onClick={isEditing ? handleEditctype : handleAddctype}
              color="primary"
            >
              {isEditing ? 'Ändern' : 'Hinzufügen'}
            </Button>
          </DialogActions>
        </Dialog>
      </div>
  );
}