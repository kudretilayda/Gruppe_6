// src/pages/StylePage.js
import React, { useState, useEffect } from 'react';
import Style from '../../api/StyleBO';
import DigitalWardrobeAPI from '../../api/DigitalWardrobeAPI'


const StylePage = () => {
  const [styles, setStyles] = useState([]);

  useEffect(() => {
    const loadStyles = async () => {
      const data = await fetch(Style);
      setStyles(data);
    };

    loadStyles();
  }, []);

  return (
    <div>
      <h2>Meine Styles</h2>
      {styles.map((style) => (
          <Style key={style.id} name={style.name} />
      ))}
    </div>
  );
};

export default StylePage;

/*
import React, { useState, useEffect } from 'react';
import {
  Container,
  Paper,
  TextField,
  Button,
  Typography,
  FormControl,
  Select,
  MenuItem,
  Box,
  Grid,
} from '@mui/material';
import { useAuth } from '../../context/AuthContext';
import DigitalWardrobeAPI from '../../api/DigitalWardrobeAPI';

const Styles = () => {
  // status management 
  const [styleName, setStyleName] = useState('');
  const [selectedMutex, setSelectedMutex] = useState('');
  const [selectedImplication, setSelectedImplication] = useState('');
  const [selectedCardinality, setSelectedCardinality] = useState('');
  const [styles, setStyles] = useState([]);
  const [constraints, setConstraints] = useState([]);

  // läd vorhandene styles
  useEffect(() => {
    loadStyles();
  }, []);

  // funktion um existierende styles zu laden
  const loadStyles = async () => {
    try {
      const stylesData = await DigitalWardrobeAPI.getAPI().getStyles();
      setStyles(stylesData);
    } catch (error) {
      console.error('Error loading styles:', error);
    }
  };

  // funktion um neue constraint hinzuzufügen
  const addConstraint = (type) => {
    let constraint;
    switch(type) {
      case 'mutex':
        constraint = selectedMutex;
        break;
      case 'implication':
        constraint = selectedImplication;
        break;
      case 'cardinality':
        constraint = selectedCardinality;
        break;
      default:
        return;
    }

    if (constraint) {
      setConstraints([...constraints, { type, value: constraint }]);
      // reset des dazugehörigen feldes
      switch(type) {
        case 'mutex':
          setSelectedMutex('');
          break;
        case 'implication':
          setSelectedImplication('');
          break;
        case 'cardinality':
          setSelectedCardinality('');
          break;
      }
    }
  };

  // funktion um style zu speichern
  const handleSaveStyle = async () => {
    try {
      const newStyle = {
        name: styleName,
        constraints: constraints
      };
      
      await DigitalWardrobeAPI.getAPI().createStyle(newStyle);
      // reset form und neuladen der styles
      setStyleName('');
      setConstraints([]);
      loadStyles();
    } catch (error) {
      console.error('Error saving style:', error);
    }
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      <Paper elevation={3} sx={{ p: 4 }}>
        <Typography variant="h5" gutterBottom>
          Style erstellen
        </Typography>

        {/* input style name }
        <TextField
          fullWidth
          label="Style Name"
          value={styleName}
          onChange={(e) => setStyleName(e.target.value)}
          margin="normal"
          required
        />

        {/* constraint abschnitt }
        <Grid container spacing={3} sx={{ mt: 2 }}>
          {/* mutex constraint }
          <Grid item xs={12} md={4}>
            <FormControl fullWidth>
              <Typography variant="subtitle2" gutterBottom>
                Mutex Constraint
              </Typography>
              <Select
                value={selectedMutex}
                onChange={(e) => setSelectedMutex(e.target.value)}
              >
                <MenuItem value="">
                  <em>Auswählen</em>
                </MenuItem>
                
              </Select>
              <Button
                onClick={() => addConstraint('mutex')}
                variant="outlined"
                sx={{ mt: 1 }}
              >
                MUTEX HINZUFÜGEN
              </Button>
            </FormControl>
          </Grid>

          {/* implikation constraint }
          <Grid item xs={12} md={4}>
            <FormControl fullWidth>
              <Typography variant="subtitle2" gutterBottom>
                Implikation Constraint
              </Typography>
              <Select
                value={selectedImplication}
                onChange={(e) => setSelectedImplication(e.target.value)}
              >
                <MenuItem value="">
                  <em>Auswählen</em>
                </MenuItem>
                
              </Select>
              <Button
                onClick={() => addConstraint('implication')}
                variant="outlined"
                sx={{ mt: 1 }}
              >
                IMPLIKATION HINZUFÜGEN
              </Button>
            </FormControl>
          </Grid>

          {/* kardinalität constraint }
          <Grid item xs={12} md={4}>
            <FormControl fullWidth>
              <Typography variant="subtitle2" gutterBottom>
                Kardinalität Constraint
              </Typography>
              <Select
                value={selectedCardinality}
                onChange={(e) => setSelectedCardinality(e.target.value)}
              >
                <MenuItem value="">
                  <em>Auswählen</em>
                </MenuItem>
                
              </Select>
              <Button
                onClick={() => addConstraint('cardinality')}
                variant="outlined"
                sx={{ mt: 1 }}
              >
                KARDINALITÄT HINZUFÜGEN
              </Button>
            </FormControl>
          </Grid>
        </Grid>

        {/* constraint list }
        <Box sx={{ mt: 4 }}>
          <Typography variant="h6" gutterBottom>
            Hinzugefügte Constraints
          </Typography>
          {constraints.length === 0 ? (
            <Typography color="textSecondary">
              Sie haben noch keine Constraints hinzugefügt.
            </Typography>
          ) : (
            constraints.map((constraint, index) => (
              <Typography key={index}>
                {constraint.type}: {constraint.value}
              </Typography>
            ))
          )}
        </Box>

        {/* speicher knopf }
        <Button
          variant="contained"
          onClick={handleSaveStyle}
          sx={{ mt: 4 }}
          disabled={!styleName}
        >
          STYLE SPEICHERN
        </Button>

        {/* existierende styles }
        <Box sx={{ mt: 4 }}>
          <Typography variant="h6" gutterBottom>
            Vorhandene Styles
          </Typography>
          {styles.length === 0 ? (
            <Typography color="textSecondary">
              Sie haben noch keine Styles gespeichert.
            </Typography>
          ) : (
            styles.map((style, index) => (
              <Paper key={index} sx={{ p: 2, mt: 2 }}>
                <Typography variant="subtitle1">{style.getName()}</Typography>
              </Paper>
            ))
          )}
        </Box>
      </Paper>
    </Container>
  );
};

export default Styles;
*/


/*
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
    setNewStyle({ name: '', features: [] });
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
    setNewStyle({ name: '', features: [] });
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
*/