import React, { useState, useEffect } from 'react';
import StyleConstraints from '../styles/StyleConstraints';
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
  Chip,
  CardActions,
  IconButton,
  Box
} from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';

const Styles = () => {
  const [styles, setStyles] = useState([]);
  const [openDialog, setOpenDialog] = useState(false);
  const [isEditing, setIsEditing] = useState(false); // Track if we're editing or adding
  const [currentStyleIndex, setCurrentStyleIndex] = useState(null); // Track the index of the style being edited
  const [newStyle, setNewStyle] = useState({
    name: '',
    description: '',
    features: []
  });

  // Lädt gespeicherte Styles beim Start der Seite
  useEffect(() => {
    const saved = localStorage.getItem('styles');
    if (saved) {
      setStyles(JSON.parse(saved));
    }
  }, []);

  const handleAddStyle = () => {
    const updated = [...styles, newStyle];
    setStyles(updated);

    // Speichern der neuen Liste in localStorage
    localStorage.setItem('styles', JSON.stringify(updated));

    // Reset des Dialogs
    setOpenDialog(false);
    setNewStyle({ name: '', description: '', features: [] });
  };

  const handleEditStyle = () => {
    const updated = [...styles];
    updated[currentStyleIndex] = newStyle;
    setStyles(updated);

    // Speichern der aktualisierten Liste in localStorage
    localStorage.setItem('styles', JSON.stringify(updated));

    // Reset des Dialogs
    setOpenDialog(false);
    setIsEditing(false);
    setNewStyle({ name: '', description: '', features: [] });
    setCurrentStyleIndex(null);
  };

  const handleDeleteStyle = (index) => {
    const updated = styles.filter((_, i) => i !== index);
    setStyles(updated);

    // Speichern der aktualisierten Liste in localStorage
    localStorage.setItem('styles', JSON.stringify(updated));
  };

  const handleOpenEditDialog = (index) => {
    setIsEditing(true);
    setCurrentStyleIndex(index);
    setNewStyle(styles[index]);
    setOpenDialog(true);
  };

  return (
    <div className="p-4">
      <Grid container spacing={3} alignItems="center" className="mb-4">
        <Grid item xs>
          <Typography variant="h4">Meine Styles</Typography>
        </Grid>
        <Grid item>
          <Button
            variant="contained"
            color="primary"
            onClick={() => setOpenDialog(true)}
          >
            Style erstellen
          </Button>
        </Grid>
      </Grid>

      <Grid container spacing={3}>
        {styles.map((style, index) => (
          <Grid item xs={12} sm={6} md={4} key={index}>
            <Card elevation={3}>
              <CardContent>
                <Typography variant="h6">{style.name}</Typography>
                <Typography color="textSecondary" paragraph>
                  {style.description}
                </Typography>
                <Box display="flex" flexWrap="wrap">
                  {style.features.map((feature, i) => (
                    <Chip
                      key={i}
                      label={feature}
                      style={{
                        margin: '0.25rem',
                        backgroundColor: '#e0e0e0', // Leichte Hintergrundfarbe für Chips
                        color: '#333',
                        borderRadius: '16px'
                      }}
                    />
                  ))}
                </Box>
              </CardContent>
              <CardActions>
                <IconButton
                  color="primary"
                  onClick={() => handleOpenEditDialog(index)}
                >
                  <EditIcon />
                </IconButton>
                <IconButton
                  color="secondary"
                  onClick={() => handleDeleteStyle(index)}
                >
                  <DeleteIcon />
                </IconButton>
              </CardActions>
            </Card>
          </Grid>
        ))}
      </Grid>

      <Dialog open={openDialog} onClose={() => setOpenDialog(false)}>
        <DialogTitle>{isEditing ? 'Style bearbeiten' : 'Neuen Style erstellen'}</DialogTitle>
        <DialogContent>
          <TextField
            fullWidth
            margin="normal"
            label="Name"
            value={newStyle.name}
            onChange={(e) => setNewStyle({ ...newStyle, name: e.target.value })}
            required
          />
          <TextField
            fullWidth
            margin="normal"
            label="Beschreibung"
            multiline
            rows={3}
            value={newStyle.description}
            onChange={(e) =>
              setNewStyle({ ...newStyle, description: e.target.value })
            }
            required
          />
          <TextField
            fullWidth
            margin="normal"
            label="Features (kommagetrennt)"
            value={newStyle.features.join(', ')}
            onChange={(e) =>
              setNewStyle({
                ...newStyle,
                features: e.target.value.split(',').map((f) => f.trim())
              })
            }
            helperText="z.B.: casual, business, sportlich"
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenDialog(false)}>Abbrechen</Button>
          <Button
            onClick={isEditing ? handleEditStyle : handleAddStyle}
            color="primary"
          >
            {isEditing ? 'Ändern' : 'Erstellen'}
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default Styles;