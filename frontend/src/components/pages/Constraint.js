/* import React, { useState } from 'react';
import {
  Box,
  Button,
  Card,
  CardContent,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  FormControl,
  IconButton,
  InputLabel,
  MenuItem,
  Select,
  TextField,
  Tooltip,
  Typography
} from '@mui/material';
import InfoIcon from '@mui/icons-material/Info';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import SaveIcon from '@mui/icons-material/Save';
import CloseIcon from '@mui/icons-material/Close';

// Styles should be imported or defined here.
import './Constraints.css';

const Constraints = ({ kleidungstypen, mutex, cardinality, onMutexSave, onCardinalitySave, onDeleteMutex, onDeleteCardinality }) => {
  const [editMutexIndex, setEditMutexIndex] = useState(null);
  const [editMutex, setEditMutex] = useState({});
  const [hasMutexChanges, setHasMutexChanges] = useState(false);
  const [editCardinalityIndex, setEditCardinalityIndex] = useState(null);
  const [editCardinality, setEditCardinality] = useState({});
  const [hasCardinalityChanges, setHasCardinalityChanges] = useState(false);
  const [openDialog, setOpenDialog] = useState(false);
  const [dialogMessage, setDialogMessage] = useState('');

  // Helpers
  const getKleidungstypBezeichnung = (id) => {
    const typ = kleidungstypen.find((k) => k.id === id);
    return typ ? typ.bezeichnung : 'Unbekannt';
  };

  const handleDialogOpen = (message) => {
    setDialogMessage(message);
    setOpenDialog(true);
  };

  const handleDialogClose = () => {
    setOpenDialog(false);
  };

  const handleEditMutexSave = () => {
    if (onMutexSave) onMutexSave(editMutexIndex, editMutex);
    setEditMutexIndex(null);
    setEditMutex({});
    setHasMutexChanges(false);
  };

  const handleEditCardinalitySave = () => {
    if (onCardinalitySave) onCardinalitySave(editCardinalityIndex, editCardinality);
    setEditCardinalityIndex(null);
    setEditCardinality({});
    setHasCardinalityChanges(false);
  };

  return (
    <Box className="constraints-container">
      <Card className="constraints-card">
        <CardContent>
          <Typography variant="h5" className="constraints-title">
            Einschränkungen
          </Typography>
          <Box className="constraint-section">

            {/* Mutex Section }
            <Card className="constraint-type-card">
              <Typography variant="h6" className="section-header">
                Mutex
                <Tooltip
                  title="Ein Mutex bedeutet: Zwei ausgewählte Kleidungstypen können nicht zusammen in einem Outfit getragen werden."
                  placement="right"
                >
                  <InfoIcon className="info-icon" />
                </Tooltip>
              </Typography>
              {mutex.length === 0 ? (
                <Box className="empty-constraint-message">
                  Kein Mutex gespeichert
                </Box>
              ) : (
                mutex.map((item, index) => (
                  <Card key={index} className="constraint-item-card">
                    <CardContent className="constraint-content">
                      <Box className="constraint-box">
                        {editMutexIndex === index ? (
                          <Box className="edit-mode-container">
                            <FormControl size="small" className="form-control-width">
                              <InputLabel>Kleidungstyp 1</InputLabel>
                              <Select
                                value={editMutex.bezugsobjekt1}
                                onChange={(e) => {
                                  setEditMutex({
                                    ...editMutex,
                                    bezugsobjekt1: e.target.value
                                  });
                                  setHasMutexChanges(true);
                                }}
                                label="Kleidungstyp 1"
                              >
                                {kleidungstypen.map((typ) => (
                                  <MenuItem key={typ.id} value={typ.id}>
                                    {typ.bezeichnung}
                                  </MenuItem>
                                ))}
                              </Select>
                            </FormControl>

                            <FormControl size="small" className="form-control-width">
                              <InputLabel>Kleidungstyp 2</InputLabel>
                              <Select
                                value={editMutex.bezugsobjekt2}
                                onChange={(e) => {
                                  setEditMutex({
                                    ...editMutex,
                                    bezugsobjekt2: e.target.value
                                  });
                                  setHasMutexChanges(true);
                                }}
                                label="Kleidungstyp 2"
                              >
                                {kleidungstypen.map((typ) => (
                                  <MenuItem key={typ.id} value={typ.id}>
                                    {typ.bezeichnung}
                                  </MenuItem>
                                ))}
                              </Select>
                            </FormControl>
                          </Box>

                          <Box sx={{ display: 'flex', gap: 0 }}>
                            <Tooltip title="Speichern">
                              <span>
                                <IconButton
                                  size="small"
                                  onClick={handleEditMutexSave}
                                  color="primary"
                                  disabled={!hasMutexChanges}
                                >
                                  <SaveIcon />
                                </IconButton>
                              </span>
                            </Tooltip>
                            <Tooltip title="Abbrechen">
                              <IconButton
                                size="small"
                                onClick={() => {
                                  setEditMutexIndex(null);
                                  setEditMutex({});
                                  setHasMutexChanges(false);
                                }}
                                color="error"
                              >
                                <CloseIcon />
                              </IconButton>
                            </Tooltip>
                          </Box>
                        ) : (
                          <>
                            <Typography className="constraint-text">
                              <Box component="span" className="constraint-type">
                                {getKleidungstypBezeichnung(item.bezugsobjekt1)}
                              </Box>{' '}
                              und {' '}
                              <Box component="span" className="constraint-type">
                                {getKleidungstypBezeichnung(item.bezugsobjekt2)}
                              </Box>{' '}
                              können nicht zusammen getragen werden
                            </Typography>
                            <Box sx={{ display: 'flex', alignItems: 'center', margin: 0 }}>
                              <Tooltip title="Bearbeiten">
                                <IconButton
                                  color="primary"
                                  onClick={() => {
                                    setEditMutexIndex(index);
                                    setEditMutex(item);
                                  }}
                                  size="small"
                                >
                                  <EditIcon />
                                </IconButton>
                              </Tooltip>
                              <Tooltip title="Löschen">
                                <IconButton
                                  color="error"
                                  onClick={() => onDeleteMutex(item.id)}
                                  size="small"
                                >
                                  <DeleteIcon />
                                </IconButton>
                              </Tooltip>
                            </Box>
                          </>
                        )}
                      </Box>
                    </CardContent>
                  </Card>
                ))
              )}
            </Card>

            {/* Cardinality Section }
            <Card className="constraint-type-card">
              <Typography variant="h6" className="section-header">
                Kardinalitäten
                <Tooltip
                  title="Eine Kardinalität legt fest, wie oft ein bestimmter Kleidungstyp in einem Outfit vorkommen muss."
                  placement="right"
                >
                  <InfoIcon className="info-icon" />
                </Tooltip>
              </Typography>
              {cardinality.length === 0 ? (
                <Box className="empty-constraint-message">
                  Keine Kardinalitäten gespeichert
                </Box>
              ) : (
                cardinality.map((item, index) => (
                  <Card key={index} className="constraint-item-card">
                    <CardContent className="constraint-content">
                      <Box className="constraint-box">
                        {editCardinalityIndex === index ? (
                          <Box className="edit-mode-container">
                            <FormControl size="small" className="form-control-width">
                              <InputLabel>Kleidungstyp</InputLabel>
                              <Select
                                value={editCardinality.bezugsobjekt}
                                onChange={(e) => {
                                  setEditCardinality({
                                    ...editCardinality,
                                    bezugsobjekt: e.target.value
                                  });
                                  setHasCardinalityChanges(true);
                                }}
                                label="Kleidungstyp"
                              >
                                {kleidungstypen.map((typ) => (
                                  <MenuItem key={typ.id} value={typ.id}>
                                    {typ.bezeichnung}
                                  </MenuItem>
                                ))}
                              </Select>
                            </FormControl>

                            <TextField
                              label="Anzahl"
                              type="number"
                              size="small"
                              value={editCardinality.anzahl}
                              onChange={(e) => {
                                setEditCardinality({
                                  ...editCardinality,
                                  anzahl: e.target.value
                                });
                                setHasCardinalityChanges(true);
                              }}
                            />
                          </Box>

                          <Box sx={{ display: 'flex', gap: 0 }}>
                            <Tooltip title="Speichern">
                              <span>
                                <IconButton
                                  size="small"
                                  onClick={handleEditCardinalitySave}
                                  color="primary"
                                  disabled={!hasCardinalityChanges}
                                >
                                  <SaveIcon />
                                </IconButton>
                              </span>
                            </Tooltip>
                            <Tooltip title="Abbrechen">
                              <IconButton
                                size="small"
                                onClick={() => {
                                  setEditCardinalityIndex(null);
                                  setEditCardinality({});
                                  setHasCardinalityChanges(false);
                                }}
                                color="error"
                              >
                                <CloseIcon />
                              </IconButton>
                            </Tooltip>
                          </Box>
                        ) : (
                          <>
                            <Typography className="constraint-text">
                              In einem Outfit {item.anzahl === 1 ? (
                                <>
                                  muss genau{' '}
                                  <Box component="span" className="constraint-number">
                                    {item.anzahl}
                                  </Box>{' '}
                                  <Box component="span" className="constraint-type">
                                    {getKleidungstypBezeichnung(item.bezugsobjekt)}
                                  </Box>{' '}
                                  enthalten sein
                                </>
                              ) : (
                                <>
                                  müssen genau{' '}
                                  <Box component="span" className="constraint-number">
                                    {item.anzahl}
                                  </Box>{' '}
                                  <Box component="span" className="constraint-type">
                                    {getKleidungstypBezeichnung(item.bezugsobjekt)}
                                  </Box>{' '}
                                  enthalten sein
                                </>
                              )}
                            </Typography>
                            <Box className="constraint-actions">
                              <Tooltip title="Bearbeiten">
                                <IconButton
                                  color="primary"
                                  onClick={() => {
                                    setEditCardinalityIndex(index);
                                    setEditCardinality(item);
                                  }}
                                  size="small"
                                >
                                  <EditIcon />
                                </IconButton>
                              </Tooltip>
                              <Tooltip title="Löschen">
                                <IconButton
                                  color="error"
                                  onClick={() => onDeleteCardinality(item.id)}
                                  size="small"
                                >
                                  <DeleteIcon />
                                </IconButton>
                              </Tooltip>
                            </Box>
                          </>
                        )}
                      </Box>
                    </CardContent>
                  </Card>
                ))
              )}
            </Card>
          </Box>
        </CardContent>
      </Card>

      {/* Dialog }
      <Dialog
        open={openDialog}
        onClose={handleDialogClose}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">{"Hinweis"}</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            {dialogMessage}
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button
            onClick={handleDialogClose}
            variant="contained"
            className="dialog-button"
            autoFocus
          >
            OK
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
};

export default Constraints;


 */