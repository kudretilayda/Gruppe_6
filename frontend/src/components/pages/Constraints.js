import React, { useState, useEffect } from 'react';
import {
  Container,
  Paper,
  Typography,
  FormControl,
  Select,
  MenuItem,
  Box,
  IconButton,
  Tooltip,
  TextField,
  Button,
  Grid,
  Snackbar,
  Alert
} from '@mui/material';
import InfoIcon from '@mui/icons-material/Info';
import { useAuth } from '../../context/AuthContext';
import DigitalWardrobeAPI from '../../api/DigitalWardrobeAPI';

const Constraints = () => {
  // State-Variablen
  const [selectedConstraintType, setSelectedConstraintType] = useState('');
  const [implicationConstraints, setImplicationConstraints] = useState([]);
  const [mutexConstraints, setMutexConstraints] = useState([]);
  const [cardinalityConstraints, setCardinalityConstraints] = useState([]);

  // Inputs für neue Constraints
  const [newImplication, setNewImplication] = useState({ if_type: '', then_type: '' });
  const [newMutex, setNewMutex] = useState({ item1: '', item2: '' });
  const [newCardinality, setNewCardinality] = useState({ object: '', min_count: 0, max_count: 0 });

  // Snackbar-Status
  const [openSnackbar, setOpenSnackbar] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState('');
  const [snackbarSeverity, setSnackbarSeverity] = useState('success');

  // Hilfstexte für Constraints
  const constraintInfo = {
    implication: "Eine Implikation definiert eine 'Wenn-Dann' Beziehung zwischen Kleidungstypen",
    mutex: "Ein Mutex verhindert, dass bestimmte Kleidungsstücke zusammen getragen werden",
    cardinality: "Eine Kardinalität legt fest, wie viele Kleidungsstücke eines Typs verwendet werden müssen"
  };

  // Lädt Constraints beim Rendern
  useEffect(() => {
    loadConstraints();
  }, []);

  // Funktion: Alle Constraints laden
  const loadConstraints = async () => {
    try {
      const implication = await DigitalWardrobeAPI.getAPI().getImplicationConstraints();
      const mutex = await DigitalWardrobeAPI.getAPI().getMutexConstraints();
      const cardinality = await DigitalWardrobeAPI.getAPI().getCardinalityConstraints();

      setImplicationConstraints(implication || []);
      setMutexConstraints(mutex || []);
      setCardinalityConstraints(cardinality || []);
    } catch (error) {
      console.error('Fehler beim Laden der Constraints:', error);
    }
  };

  // Funktion: Constraint-Typ ändern
  const handleConstraintTypeChange = (event) => {
    setSelectedConstraintType(event.target.value);
  };

  // Snackbar schließen
  const handleCloseSnackbar = () => {
    setOpenSnackbar(false);
  };

  // Funktion: Neues Implication-Constraint speichern
  const saveImplicationConstraint = async () => {
    if (!newImplication.if_type || !newImplication.then_type) {
      alert('Bitte geben Sie gültige Werte für Implikation ein!');
      return;
    }

    try {
      await DigitalWardrobeAPI.getAPI().createImplicationConstraint(newImplication);
      loadConstraints();
      setSnackbarMessage('Implikation erfolgreich gespeichert!');
      setSnackbarSeverity('success');
      setOpenSnackbar(true);
      setNewImplication({ if_type: '', then_type: '' });
    } catch (error) {
      console.error('Fehler beim Speichern der Implikation:', error);
      setSnackbarMessage('Fehler beim Speichern der Implikation');
      setSnackbarSeverity('error');
      setOpenSnackbar(true);
    }
  };

  // Funktion: Neues Mutex-Constraint speichern
  const saveMutexConstraint = async () => {
    if (!newMutex.item1 || !newMutex.item2) {
      alert('Bitte geben Sie gültige Werte für Mutex ein!');
      return;
    }

    try {
      await DigitalWardrobeAPI.getAPI().createMutexConstraint(newMutex);
      loadConstraints();
      setSnackbarMessage('Mutex erfolgreich gespeichert!');
      setSnackbarSeverity('success');
      setOpenSnackbar(true);
      setNewMutex({ item1: '', item2: '' });
    } catch (error) {
      console.error('Fehler beim Speichern des Mutex:', error);
      setSnackbarMessage('Fehler beim Speichern des Mutex');
      setSnackbarSeverity('error');
      setOpenSnackbar(true);
    }
  };

  // Funktion: Neues Cardinality-Constraint speichern
  const saveCardinalityConstraint = async () => {
    const { object, min_count, max_count } = newCardinality;

    if (!object || min_count < 0 || max_count < min_count) {
      alert('Bitte geben Sie gültige Werte für Kardinalität ein!');
      return;
    }

    try {
      await DigitalWardrobeAPI.getAPI().createCardinalityConstraint(newCardinality);
      loadConstraints();
      setSnackbarMessage('Kardinalität erfolgreich gespeichert!');
      setSnackbarSeverity('success');
      setOpenSnackbar(true);
      setNewCardinality({ object: '', min_count: 0, max_count: 0 });
    } catch (error) {
      console.error('Fehler beim Speichern der Kardinalität:', error);
      setSnackbarMessage('Fehler beim Speichern der Kardinalität');
      setSnackbarSeverity('error');
      setOpenSnackbar(true);
    }
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      <Paper elevation={3} sx={{ p: 4 }}>
        <Typography variant="h5" gutterBottom>
          Constraints Manager
        </Typography>

        {/* Constraint-Typ auswählen */}
        <FormControl fullWidth sx={{ mt: 2 }}>
          <Select
            value={selectedConstraintType}
            onChange={handleConstraintTypeChange}
            displayEmpty
          >
            <MenuItem value="" disabled>
              Wählen Sie einen Constraint-Typ
            </MenuItem>
            <MenuItem value="implication">
              Implikation
              <Tooltip title={constraintInfo.implication}>
                <IconButton sx={{ ml: 1 }}>
                  <InfoIcon />
                </IconButton>
              </Tooltip>
            </MenuItem>
            <MenuItem value="mutex">
              Mutex
              <Tooltip title={constraintInfo.mutex}>
                <IconButton sx={{ ml: 1 }}>
                  <InfoIcon />
                </IconButton>
              </Tooltip>
            </MenuItem>
            <MenuItem value="cardinality">
              Kardinalität
              <Tooltip title={constraintInfo.cardinality}>
                <IconButton sx={{ ml: 1 }}>
                  <InfoIcon />
                </IconButton>
              </Tooltip>
            </MenuItem>
          </Select>
        </FormControl>

        {/* Eingabefelder für neue Constraints */}
        {/* Bedingungsauswahl und Eingabeformular für Implication, Mutex und Cardinality */}
        {/* Der Rest des Codes bleibt gleich */}
        
        {/* Bestehende Constraints anzeigen */}
        <Box sx={{ mt: 5 }}>
          <Typography variant="h6">Vorhandene Constraints</Typography>
          <Typography>Implikationen:</Typography>
          {implicationConstraints.map((c, index) => (
            <Typography key={index}>
              Wenn {c.if_type}, dann {c.then_type}
            </Typography>
          ))}

          <Typography>Mutex:</Typography>
          {mutexConstraints.map((c, index) => (
            <Typography key={index}>
              {c.item1} und {c.item2} nicht zusammen
            </Typography>
          ))}

          <Typography>Kardinalitäten:</Typography>
          {cardinalityConstraints.map((c, index) => (
            <Typography key={index}>
              {c.object}: {c.min_count} bis {c.max_count}
            </Typography>
          ))}
        </Box>
      </Paper>

      {/* Snackbar anzeigen */}
      <Snackbar
        open={openSnackbar}
        autoHideDuration={6000}
        onClose={handleCloseSnackbar}
      >
        <Alert onClose={handleCloseSnackbar} severity={snackbarSeverity}>
          {snackbarMessage}
        </Alert>
      </Snackbar>
    </Container>
  );
};

export default Constraints;
