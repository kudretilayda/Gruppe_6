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
  Card,
  CardContent,
  Button,
  CircularProgress,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  TextField,
  Snackbar,
  Alert,
} from '@mui/material';
import InfoIcon from '@mui/icons-material/Info';
import DeleteIcon from '@mui/icons-material/Delete';
import EditIcon from '@mui/icons-material/Edit';
import { useAuth } from '../../context/AuthContext';
import DigitalWardrobeAPI from '../../api/DigitalWardrobeAPI';

const Constraints = () => {
  const [selectedConstraintType, setSelectedConstraintType] = useState('');
  const [implicationConstraints, setImplicationConstraints] = useState([]);
  const [mutexConstraints, setMutexConstraints] = useState([]);
  const [cardinalityConstraints, setCardinalityConstraints] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const [snackbarMessage, setSnackbarMessage] = useState('');
  const [openSnackbar, setOpenSnackbar] = useState(false);
  const [openDialog, setOpenDialog] = useState(false);
  const [dialogData, setDialogData] = useState({});
  const { user } = useAuth();

  // Info texts for constraints
  const constraintInfo = {
    implication: "Eine Implikation definiert eine 'Wenn-Dann' Beziehung zwischen Kleidungstypen",
    mutex: "Ein Mutex verhindert, dass bestimmte Kleidungsstücke zusammen getragen werden",
    cardinality: "Eine Kardinalität legt fest, wie viele Kleidungsstücke eines Typs verwendet werden müssen",
  };

  useEffect(() => {
    if (user) {
      loadConstraints();
    }
  }, [user]);

  const loadConstraints = async () => {
    setIsLoading(true);
    try {
      const implication = await DigitalWardrobeAPI.getAPI().getImplicationConstraints();
      const mutex = await DigitalWardrobeAPI.getAPI().getMutexConstraints();
      const cardinality = await DigitalWardrobeAPI.getAPI().getCardinalityConstraints();

      setImplicationConstraints(Array.isArray(implication) ? implication : []);
      setMutexConstraints(Array.isArray(mutex) ? mutex : []);
      setCardinalityConstraints(Array.isArray(cardinality) ? cardinality : []);
    } catch (err) {
      console.error('Fehler beim Laden der Constraints:', err);
      setError('Fehler beim Laden der Constraints.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleConstraintTypeChange = (event) => {
    setSelectedConstraintType(event.target.value);
  };

  const handleDialogOpen = (constraint = {}) => {
    setDialogData(constraint);
    setOpenDialog(true);
  };

  const handleDialogClose = () => {
    setOpenDialog(false);
    setDialogData({});
  };

  const handleSaveConstraint = async () => {
    try {
      // API-Aufruf je nach Constraint-Typ (Neuerstellung oder Bearbeitung)
      if (dialogData.id) {
        await DigitalWardrobeAPI.getAPI().updateConstraint(dialogData);
        setSnackbarMessage('Constraint erfolgreich aktualisiert.');
      } else {
        await DigitalWardrobeAPI.getAPI().createConstraint(dialogData);
        setSnackbarMessage('Constraint erfolgreich hinzugefügt.');
      }
      setOpenSnackbar(true);
      handleDialogClose();
      loadConstraints();
    } catch (err) {
      console.error('Fehler beim Speichern des Constraints:', err);
      setSnackbarMessage('Fehler beim Speichern des Constraints.');
      setOpenSnackbar(true);
    }
  };

  const handleDeleteConstraint = async (constraint) => {
    if (window.confirm('Möchten Sie dieses Constraint wirklich löschen?')) {
      try {
        await DigitalWardrobeAPI.getAPI().deleteConstraint(constraint.id);
        setSnackbarMessage('Constraint erfolgreich gelöscht.');
        setOpenSnackbar(true);
        loadConstraints();
      } catch (err) {
        console.error('Fehler beim Löschen des Constraints:', err);
        setSnackbarMessage('Fehler beim Löschen des Constraints.');
        setOpenSnackbar(true);
      }
    }
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4, backgroundColor: '#f5f5f5', minHeight: '100vh' }}>
      <Paper elevation={3} sx={{ p: 4, backgroundColor: 'white', borderRadius: 2 }}>
        <Typography variant="h6" gutterBottom sx={{ mb: 3 }}>
          Constraints verwalten
        </Typography>

        {user ? (
          <>
            <FormControl fullWidth sx={{ mb: 4 }}>
              <Typography variant="subtitle2" sx={{ mb: 1 }}>
                Constraint auswählen:
              </Typography>
              <Select
                value={selectedConstraintType}
                onChange={handleConstraintTypeChange}
                displayEmpty
                sx={{
                  backgroundColor: 'white',
                  '& .MuiSelect-select': {
                    p: 1.5,
                  },
                }}
              >
                <MenuItem value="" disabled>
                  Bitte wählen Sie ein Constraint Typ aus
                </MenuItem>
                {Object.keys(constraintInfo).map((type) => (
                  <MenuItem key={type} value={type}>
                    {type.charAt(0).toUpperCase() + type.slice(1)}
                    <Tooltip title={constraintInfo[type]}>
                      <IconButton size="small" sx={{ ml: 1 }}>
                        <InfoIcon fontSize="small" />
                      </IconButton>
                    </Tooltip>
                  </MenuItem>
                ))}
              </Select>
            </FormControl>

            {isLoading ? (
              <CircularProgress />
            ) : (
              <Box sx={{ mt: 4 }}>
                {[{ title: 'Implikationen', data: implicationConstraints },
                  { title: 'Mutex', data: mutexConstraints },
                  { title: 'Kardinalitäten', data: cardinalityConstraints }].map(
                  ({ title, data }) => (
                    <Card key={title} sx={{ mb: 2, backgroundColor: '#f8f9fa' }}>
                      <CardContent>
                        <Typography variant="subtitle1" sx={{ display: 'flex', alignItems: 'center' }}>
                          {title}
                          <Tooltip title={constraintInfo[title.toLowerCase()]}>
                            <IconButton size="small" sx={{ ml: 1 }}>
                              <InfoIcon fontSize="small" />
                            </IconButton>
                          </Tooltip>
                        </Typography>
                        {data.length > 0 ? (
                          data.map((c, i) => (
                            <Box
                              key={i}
                              sx={{
                                display: 'flex',
                                justifyContent: 'space-between',
                                alignItems: 'center',
                                mt: 1,
                              }}
                            >
                              <Typography variant="body2">{JSON.stringify(c)}</Typography>
                              <Box>
                                <IconButton
                                  size="small"
                                  onClick={() => handleDialogOpen(c)}
                                >
                                  <EditIcon />
                                </IconButton>
                                <IconButton
                                  size="small"
                                  onClick={() => handleDeleteConstraint(c)}
                                >
                                  <DeleteIcon />
                                </IconButton>
                              </Box>
                            </Box>
                          ))
                        ) : (
                          <Typography variant="body2" color="text.secondary">
                            Keine Daten verfügbar
                          </Typography>
                        )}
                      </CardContent>
                    </Card>
                  )
                )}
              </Box>
            )}
          </>
        ) : (
          <Typography color="error">Sie müssen angemeldet sein, um Constraints zu verwalten.</Typography>
        )}
      </Paper>

      {/* Dialog */}
      <Dialog open={openDialog} onClose={handleDialogClose}>
        <DialogTitle>Constraint bearbeiten</DialogTitle>
        <DialogContent>
          <TextField
            label="Daten"
            value={dialogData.value || ''}
            onChange={(e) =>
              setDialogData({ ...dialogData, value: e.target.value })
            }
            fullWidth
            sx={{ mt: 2 }}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleDialogClose}>Abbrechen</Button>
          <Button onClick={handleSaveConstraint}>Speichern</Button>
        </DialogActions>
      </Dialog>

      {/* Snackbar */}
      <Snackbar
        open={openSnackbar}
        autoHideDuration={6000}
        onClose={() => setOpenSnackbar(false)}
      >
        <Alert severity="info">{snackbarMessage}</Alert>
      </Snackbar>
    </Container>
  );
};

export default Constraints;
