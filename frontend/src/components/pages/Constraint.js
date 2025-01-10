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
  Grid,
} from '@mui/material';
import InfoIcon from '@mui/icons-material/Info';
import { useAuth } from '../../context/AuthContext';
import DigitalWardrobeAPI from '../../api/DigitalWardrobeAPI';

const Constraints = () => {
  // status constraint manager
  const [selectedConstraintType, setSelectedConstraintType] = useState('');
  const [implicationConstraints, setImplicationConstraints] = useState([]);
  const [mutexConstraints, setMutexConstraints] = useState([]);
  const [cardinalityConstraints, setCardinalityConstraints] = useState([]);

  // hilfs text für die constraints
  const constraintInfo = {
    implication: "Eine Implikation definiert eine 'Wenn-Dann' Beziehung zwischen Kleidungstypen",
    mutex: "Ein Mutex verhindert, dass bestimmte Kleidungsstücke zusammen getragen werden",
    cardinality: "Eine Kardinalität legt fest, wie viele Kleidungsstücke eines Typs verwendet werden müssen"
  };

  // handle constraint typ selection
  const handleConstraintTypeChange = (event) => {
    setSelectedConstraintType(event.target.value);
  };

  // läd vorhandene constraints
  useEffect(() => {
    loadConstraints();
  }, []);

  // funktion um alle existierenden constraints zu laden
  const loadConstraints = async () => {
    try {
      // API calls um constraints zu laden
      const implication = await DigitalWardrobeAPI.getAPI().getImplicationConstraints();
      const mutex = await DigitalWardrobeAPI.getAPI().getMutexConstraints();
      const cardinality = await DigitalWardrobeAPI.getAPI().getCardinalityConstraints();

      setImplicationConstraints(implication || []);
      setMutexConstraints(mutex || []);
      setCardinalityConstraints(cardinality || []);
    } catch (error) {
      console.error('Error loading constraints:', error);
    }
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      <Paper elevation={3} sx={{ p: 4 }}>
        <Typography variant="h5" gutterBottom>
          Neuen Constraint erstellen
        </Typography>

        {/* constraint typ auswahl */}
        <FormControl fullWidth sx={{ mt: 2 }}>
          <Box display="flex" alignItems="center" mb={1}>
            <Typography variant="subtitle2" component="label">
              Constraint auswählen*
            </Typography>
          </Box>
          <Select
            value={selectedConstraintType}
            onChange={handleConstraintTypeChange}
            displayEmpty
          >
            <MenuItem value="" disabled>
              Bitte wählen Sie ein Constraint Typ aus
            </MenuItem>
            <MenuItem value="implication">
              <Box display="flex" alignItems="center" justifyContent="space-between" width="100%">
                <span>Implikation</span>
                <Tooltip title={constraintInfo.implication}>
                  <IconButton size="small">
                    <InfoIcon fontSize="small" />
                  </IconButton>
                </Tooltip>
              </Box>
            </MenuItem>
            <MenuItem value="mutex">
              <Box display="flex" alignItems="center" justifyContent="space-between" width="100%">
                <span>Mutex</span>
                <Tooltip title={constraintInfo.mutex}>
                  <IconButton size="small">
                    <InfoIcon fontSize="small" />
                  </IconButton>
                </Tooltip>
              </Box>
            </MenuItem>
            <MenuItem value="cardinality">
              <Box display="flex" alignItems="center" justifyContent="space-between" width="100%">
                <span>Kardinalität</span>
                <Tooltip title={constraintInfo.cardinality}>
                  <IconButton size="small">
                    <InfoIcon fontSize="small" />
                  </IconButton>
                </Tooltip>
              </Box>
            </MenuItem>
          </Select>
        </FormControl>

        {/* vorhandene constraints display */}
        <Box sx={{ mt: 4 }}>
          {/* implication constraint */}
          <Box sx={{ mb: 3 }}>
            <Box display="flex" alignItems="center">
              <Typography variant="subtitle1" component="h3">
                Implikation
              </Typography>
              <Tooltip title={constraintInfo.implication}>
                <IconButton size="small">
                  <InfoIcon fontSize="small" />
                </IconButton>
              </Tooltip>
            </Box>
            <Typography color="textSecondary">
              {implicationConstraints.length === 0 
                ? 'Keine Implikation gespeichert' 
                : implicationConstraints.map((constraint, index) => (
                    <Box key={index} sx={{ mt: 1 }}>
                        <Typography>
                            Wenn {constraint.if_type}, dann {constraint.then_type}
                        </Typography>
                    </Box>
                ))
            }
            </Typography>
          </Box>

          {/* mutex constraint */}
          <Box sx={{ mb: 3 }}>
            <Box display="flex" alignItems="center">
                <Typography variant="subtitle1" component="h3">
                Mutex
                </Typography>
                <Tooltip title={constraintInfo.mutex}>
                <IconButton size="small">
                    <InfoIcon fontSize="small" />
                </IconButton>
                </Tooltip>
            </Box>
            <Typography color="textSecondary">
                {mutexConstraints.length === 0 
                ? 'Kein Mutex gespeichert' 
                : mutexConstraints.map((constraint, index) => (
                    <Box key={index} sx={{ mt: 1 }}>
                        <Typography>
                        {constraint.mutex.map(([item1, item2]) => 
                            `${item1} und ${item2} nicht zusammen`
                        ).join(', ')}
                    </Typography>
                    </Box>
                    ))
                }
                </Typography>
            </Box>

          {/* cardinality constraint */}
          <Box sx={{ mb: 3 }}>
            <Box display="flex" alignItems="center">
              <Typography variant="subtitle1" component="h3">
                Kardinalitäten
              </Typography>
              <Tooltip title={constraintInfo.cardinality}>
                <IconButton size="small">
                  <InfoIcon fontSize="small" />
                </IconButton>
              </Tooltip>
            </Box>
            <Typography color="textSecondary">
              {cardinalityConstraints.length === 0 
                ? 'Keine Kardinalität gespeichert' 
                : {/* Display your cardinality constraints here */}}
            </Typography>
          </Box>
        </Box>
      </Paper>
    </Container>
  )
};

export default Constraints;