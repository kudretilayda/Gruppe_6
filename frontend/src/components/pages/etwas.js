/* import React, { useState, useEffect } from "react";
import {
  TextField,
  Button,
  Select,
  MenuItem,
  Box,
  Typography,
  IconButton,
  FormControl,
  InputLabel,
  Card,
  CardContent,
} from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import DeleteIcon from "@mui/icons-material/Delete";
import EditIcon from "@mui/icons-material/Edit";
import SmartStyleAPI from "../api/SmartStyleAPI";
import KardinalitaetBO from "../api/KardinalitaetBO";
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogActions from '@mui/material/DialogActions';
import CheckIcon from '@mui/icons-material/Check';
import CloseIcon from '@mui/icons-material/Close';
import SaveIcon from '@mui/icons-material/Save';
import Tooltip from '@mui/material/Tooltip';
import Divider from '@mui/material/Divider';
import InfoIcon from '@mui/icons-material/Info';
import '../styles/Constraints.css';

function Constraints({ id }) {
  const [constraints, setConstraints] = useState([]);
  const [savedConstraints, setSavedConstraints] = useState([]);
  const [kardinalitaetData, setkardinalitaetData] = useState({
    anzahl: 0,
    bezugsobjekt: 0,
});
   const [mutexData, setmutexData] = useState({
    id: 0,
    bezugsobjekt1: "",
    bezugsobjekt2: "",
    kleiderschrankid: id || 0
});
   const [implikationData, setimplikationData] = useState({
    id: 0,
    bezugsobjekt1: "",
    bezugsobjekt2: "",
    kleiderschrankid: id || 0
});
  const [kleidungstypen, setKleidungstypen] = useState([]);
  const [kardinalitaet, setKardinalitaeten] = useState([]);
  const [implikation, setImplikationen] = useState([]);
  const [mutex, setMutex] = useState([]);
  const [openDialog, setOpenDialog] = useState(false);
  const [dialogMessage, setDialogMessage] = useState("");
  const [editMutex, setEditMutex] = useState({});
  const [editMutexIndex, setEditMutexIndex] = useState(null);
  const [editImplikation, setEditImplikation] = useState({});
  const [editImplikationIndex, setEditImplikationIndex] = useState(null);
  const [hasImplikationChanges, setHasImplikationChanges] = useState(false);
  const [hasMutexChanges, setHasMutexChanges] = useState(false);
  const [editKardinalitaet, setEditKardinalitaet] = useState({});
  const [editKardinalitaetIndex, setEditKardinalitaetIndex] = useState(null);
  const [hasKardinalitaetChanges, setHasKardinalitaetChanges] = useState(false);

  useEffect(() => {
  console.log("Prop ID hat sich geändert, neue ID:", id);
  setkardinalitaetData((prevData) => ({
    ...prevData,
    kleiderschrankid: id || 0,
  }));
}, [id]);

  useEffect(() => {
  setimplikationData((prevData) => ({
    ...prevData,
    kleiderschrankid: id || 0, // Aktualisiere kleiderschrankid bei Änderungen
  }));
}, [id]);

  useEffect(() => {
  setmutexData((prevData) => ({
    ...prevData,
    kleiderschrankid: id || 0, // Aktualisiere kleiderschrankid bei Änderungen
  }));
}, [id]);

//alle erstellten Kleidungstypen anzeigen
  const loadKleidungstypenConstraint = async () => {
    try {
      const response = await SmartStyleAPI.getAPI().getKleidungstypenByKleiderschrankId(id);
      setKleidungstypen(response);
    } catch (error) {
      console.error("Fehler beim Laden der Kleidungstypen:", error);
    }
  };

  useEffect(() => {
    loadKleidungstypenConstraint();
  }, [id]);

  //neuen Constraint hinzufügen, Anfangzustand
  const addConstraint = () => {
    setConstraints([
      {
        type: "",
        bezugsobjekt1: "",
        bezugsobjekt2: "",
        kleiderschrankid: id
      }
    ]);
  };

  const updateConstraint = (key, value) => {
    const updatedConstraint = { ...constraints[0], [key]: value };
    setConstraints([updatedConstraint]);
  };

  //Dialog Handler
  const handleCloseDialog = () => {
    setOpenDialog(false);
  };

  //Constraint anlegen
  const saveConstraint = async (event) => {
    event.preventDefault();
    const constraint = constraints[0];

    try {
      if (constraint.type === "Kardinalität") {
        if (!kardinalitaetData.bezugsobjekt || !kardinalitaetData.anzahl) {
          setDialogMessage("Bitte füllen Sie alle Felder für die Kardinalität aus.");
          setOpenDialog(true);
          return;
        }
        const kardinalitaet = {
          id: 0,
          bezugsobjekt: kardinalitaetData.bezugsobjekt,
          anzahl: parseInt(kardinalitaetData.anzahl),
          kleiderschrankid: kardinalitaetData.kleiderschrankid
        };

        console.log("Schrank ID:", kardinalitaetData.kleiderschrankid);
        console.log("Kleidungstyp ID:", kardinalitaetData.bezugsobjekt);
        console.log("Payload:", kardinalitaet);

        const response = await SmartStyleAPI.getAPI().createKardinalitaet(kardinalitaet);
        console.log("Kardinalität wurde angelegt.", response);

        // Zustand wird zurückgesetzt
        setConstraints([]);
        setkardinalitaetData({
          anzahl: 0,
          bezugsobjekt: 0,
          kleiderschrankid: id
        });

        await loadKardinalitaeten();

        //Implikation anlegen
      } else if (constraint.type === "Implikation") {
          if (!implikationData.bezugsobjekt1 || !implikationData.bezugsobjekt2) {
            setDialogMessage("Bitte füllen Sie alle Felder für die Implikation aus.");
            setOpenDialog(true);
            return;
          }
        const implikation = {
          id: 0,
          bezugsobjekt1: implikationData.bezugsobjekt1,
          bezugsobjekt2: implikationData.bezugsobjekt2,
          kleiderschrankid: implikationData.kleiderschrankid
        };

        console.log("Schrank ID:", implikationData.kleiderschrankid);
        console.log("ImplikationObjekt1:", implikationData.bezugsobjekt1);
        console.log("ImplikationObjekt2:", implikationData.bezugsobjekt2);
        console.log("Payload:", implikation);

        const response = await SmartStyleAPI.getAPI().postImplikation(implikation);
        console.log("Implikation wurde angelegt.", response);

        //Zustand wird zurückgesetzt
        setConstraints([]);
        setimplikationData({
          bezugsobjekt1: 0,
          bezugsobjekt2: 0,
          kleiderschrankid: id
        });

        await loadImplikationen();

      //Mutex anlegen
      } else if (constraint.type === "Mutex") {
          if (!mutexData.bezugsobjekt1 || !mutexData.bezugsobjekt2) {
            setDialogMessage("Bitte füllen Sie alle Felder für den Mutex aus.");
            setOpenDialog(true);
            return;
          }

          if (!mutexData.kleiderschrankid) {
              console.error("Keine Kleiderschrank ID vorhanden!");
              alert("Fehler: Keine Kleiderschrank ID vorhanden!");
              return;
          }

          const bezugsobjekt1 = parseInt(mutexData.bezugsobjekt1);
          const bezugsobjekt2 = parseInt(mutexData.bezugsobjekt2);
          const kleiderschrankid = parseInt(mutexData.kleiderschrankid);

          if (isNaN(bezugsobjekt1) || isNaN(bezugsobjekt2) || isNaN(kleiderschrankid)) {
              alert("Ungültige Werte für Mutex-Constraint");
              return;
          }

          const mutex = {
              id: 0,
              bezugsobjekt1: bezugsobjekt1,
              bezugsobjekt2: bezugsobjekt2,
              kleiderschrankid: kleiderschrankid
          };

          console.log("Sending Mutex data:", mutex);

          try {
              const response = await SmartStyleAPI.getAPI().postMutex(mutex);
              console.log("Mutex wurde angelegt.", response);

              setConstraints([]);
              setmutexData({
                  bezugsobjekt1: "",
                  bezugsobjekt2: "",
                  kleiderschrankid: id
              });

              // Mutex neu laden
              await loadMutex();

          } catch (error) {
              console.error("Fehler beim Anlegen des Mutex:", error);
              alert("Fehler beim Anlegen des Mutex: " + error.message);
          }
      }
  } catch (error) {
    setDialogMessage("Fehler beim Erstellen des Constraints!");
    setOpenDialog(true);
  }
};

  // Funktion zum Laden der Kardinalitäten
    const loadKardinalitaeten = async () => {
      try {
        const kardinalitaetList = await SmartStyleAPI.getAPI().getKardinalitaet(id);
        console.log("Geladene Kardinalitäten:", kardinalitaetList);
        setKardinalitaeten(kardinalitaetList);
      } catch (error) {
        console.error("Fehler beim Laden der Kardinalitäten:", error);
      }
    };

 // Funktion zum Laden der Implikationen
   const loadImplikationen = async () => {
     try {
       const implikationList = await SmartStyleAPI.getAPI().getImplikationen(id);
       console.log("Geladene Implikationen:", implikationList)
       setImplikationen(implikationList);
     } catch (error) {
       console.error("Fehler beim Laden der Implikationen:", error);
     }
   };

  // Funktion zum Laden der Mutex Constraints
  const loadMutex = async () => {
    try {
      const mutexList = await SmartStyleAPI.getAPI().getMutex(id);
      console.log("Geladene Mutex:", mutexList);
      setMutex(mutexList);
    } catch (error) {
      console.error("Fehler beim Laden der Mutex Constraints:", error);
    }
  };

  useEffect(() => {
    loadKardinalitaeten();
  }, [id]);

  useEffect(() => {
    loadMutex();
  }, [id]);

  useEffect(() => {
    loadImplikationen()
  }, [id]);

  const editConstraint = (index) => {
    const toEdit = savedConstraints[index];
    const editableConstraint = {
      type: toEdit.type,
      kleidungstypen: toEdit.data.kleidungstypen || [{}, {}],
      kardinalität: toEdit.data.kleidungstyp || "",
      anzahl: toEdit.data.anzahl || 1,
    };
    setConstraints([editableConstraint]);

    const updatedSavedConstraints = savedConstraints.filter((_, i) => i !== index);
    setSavedConstraints(updatedSavedConstraints);
  };
  // Löschen einer Kardinalität
    const DeleteKardinalitaet = async (id) => {
        try {
            await SmartStyleAPI.getAPI().deleteKardinalitaet(id);
            await loadKardinalitaeten();
        } catch (error) {
            console.error('Fehler beim Löschen der Kardinalität:', error);
            alert('Fehler beim Löschen der Kardinalität');
        }
    };

  const getKleidungstypBezeichnung = (typId) => {
    const typ = kleidungstypen.find(t => t.id === typId);
    return typ ? typ.bezeichnung : typId;
  };

  //  Bearbeiten eines Mutex
  const EditClickMutex = (index, mutex) => {
    setEditMutexIndex(index);
    setEditMutex({
      bezugsobjekt1: mutex.bezugsobjekt1,
      bezugsobjekt2: mutex.bezugsobjekt2,
      id: mutex.id,
      kleiderschrankid: mutex.kleiderschrankid
    });
    setHasMutexChanges(false);
  };

  // Speichern der Änderung von Mutex
  const SaveEditMutex = async () => {
    try {
        const mutexToUpdate = mutex[editMutexIndex];

        const updatedMutex = {
            id: mutexToUpdate.id,
            bezugsobjekt1: parseInt(editMutex.bezugsobjekt1),
            bezugsobjekt2: parseInt(editMutex.bezugsobjekt2),
            kleiderschrankid: id
        };

        if (!updatedMutex.bezugsobjekt1 || !updatedMutex.bezugsobjekt2) {
            throw new Error("Alle Felder müssen ausgefüllt sein");
        }

        const response = await SmartStyleAPI.getAPI().updateMutex(updatedMutex);

        // Aktualisiere die lokale Liste der Mutex
        const updatedMutexList = [...mutex];
        updatedMutexList[editMutexIndex] = response;
        setMutex(updatedMutexList);

        // neuladen der Liste
        await loadMutex();

        // Beende den Bearbeitungsmodus
        setEditMutexIndex(null);
        setEditMutex({});
        setHasMutexChanges(false);

    } catch (error) {
        console.error("Fehler beim Speichern der Änderungen:", error);
        alert("Fehler beim Speichern der Änderungen. Bitte versuchen Sie es erneut.");
    }
};

  // Löschen eines Mutex
  const DeleteMutex = async (id) => {
    try {
      if (!id) {
        throw new Error('Keine gültige ID zum Löschen');
      }
      await SmartStyleAPI.getAPI().deleteMutex(id);
      await loadMutex();
    } catch (error) {
      console.error('Fehler beim Löschen des Mutex:', error);
      alert('Fehler beim Löschen des Mutex: ' + error.message);
    }
  };

  //  Bearbeiten einer Implikation
  const EditClickImplikation = (index, implikation) => {
    setEditImplikationIndex(index);
    setEditImplikation({
      bezugsobjekt1: implikation.bezugsobjekt1,
      bezugsobjekt2: implikation.bezugsobjekt2,
      id: implikation.id,
      kleiderschrankid: implikation.kleiderschrankid
    });
    setHasImplikationChanges(false);
  };

  // Speichern der Änderung von Implikation
  const SaveEditImplikation = async () => {
    try {
        const implikationToUpdate = implikation[editImplikationIndex];

        if (!implikationToUpdate.id) {
            throw new Error("Keine gültige ID für die Aktualisierung");
        }

        const updatedImplikation = {
            id: implikationToUpdate.id,
            bezugsobjekt1: parseInt(editImplikation.bezugsobjekt1),
            bezugsobjekt2: parseInt(editImplikation.bezugsobjekt2),
            kleiderschrankid: id
        };

        if (!updatedImplikation.bezugsobjekt1 || !updatedImplikation.bezugsobjekt2) {
            throw new Error("Alle Felder müssen ausgefüllt sein");
        }

        const response = await SmartStyleAPI.getAPI().updateImplikation(implikationToUpdate.id, updatedImplikation);

        const updatedImplikationList = [...implikation];
        updatedImplikationList[editImplikationIndex] = response;
        setImplikationen(updatedImplikationList);

        await loadImplikationen();

        setEditImplikationIndex(null);
        setEditImplikation({});
        setHasImplikationChanges(false);

    } catch (error) {
        console.error("Fehler beim Speichern der Änderungen:", error);
        alert("Fehler beim Speichern der Änderungen. Bitte versuchen Sie es erneut.");
    }
};

  // Fügen Sie diese neue Funktion hinzu
  const DeleteImplikation = async (id) => {
    try {
        if (!id) {
            throw new Error('Keine gültige ID zum Löschen');
        }
        await SmartStyleAPI.getAPI().deleteImplikation(id);
        // Nach erfolgreichem Löschen die Liste neu laden
        await loadImplikationen();
    } catch (error) {
        console.error('Fehler beim Löschen der Implikation:', error);
        alert('Fehler beim Löschen der Implikation: ' + error.message);
    }
  };

  const EditClickKardinalitaet = (index, kardinalitaet) => {
    setEditKardinalitaetIndex(index);
    setEditKardinalitaet({
      bezugsobjekt: kardinalitaet.bezugsobjekt,
      anzahl: kardinalitaet.anzahl,
      id: kardinalitaet.id,
      kleiderschrankid: kardinalitaet.kleiderschrankid
    });
    setHasKardinalitaetChanges(false);
  };

  const SaveEditKardinalitaet = async () => {
    try {
      const kardinalitaetToUpdate = kardinalitaet[editKardinalitaetIndex];

      const updatedKardinalitaet = {
        id: kardinalitaetToUpdate.id,
        bezugsobjekt: parseInt(editKardinalitaet.bezugsobjekt),
        anzahl: parseInt(editKardinalitaet.anzahl),
        kleiderschrankid: id
      };

      if (!updatedKardinalitaet.bezugsobjekt || !updatedKardinalitaet.anzahl) {
        throw new Error("Alle Felder müssen ausgefüllt sein");
      }

      await SmartStyleAPI.getAPI().putKardinalitaet(updatedKardinalitaet);

      // Neuladen der Liste
      await loadKardinalitaeten();

      // Beende den Bearbeitungsmodus
      setEditKardinalitaetIndex(null);
      setEditKardinalitaet({});
      setHasKardinalitaetChanges(false);

    } catch (error) {
      console.error("Fehler beim Speichern der Änderungen:", error);
      alert("Fehler beim Speichern der Änderungen: " + error.message);
    }
  };

  return (
    <Card className="constraints-container">
      <Box className="main-container">
        {/* Erster Bereich: Hinzufügen von Constraints }
        <Box>
          <Typography
            variant="h6"
            className="section-header"
          >
            Neuen Constraint erstellen
          </Typography>

          <Card className="content-card">
            <CardContent>
              {/* Hier kommt der bestehende Code für das Hinzufügen von Constraints }
              {constraints.length > 0 && (
                <Card className="content-card">
                  <CardContent>
                    <Box sx={{ mb: 2 }}>
                      <FormControl fullWidth variant="outlined" required>
                        <InputLabel id="constraint-select-label">Constraint auswählen</InputLabel>
                        <Select
                          labelId="constraint-select-label"
                          label="Constraint auswählen"
                          required
                          value={constraints[0].type}
                          onChange={(e) => updateConstraint("type", e.target.value)}
                        >
                          <MenuItem value="">
                            <em>Bitte wählen Sie ein Constraint Typ aus</em>
                          </MenuItem>
                          <MenuItem value="Implikation">
                            <Box className="constraint-menu-item">
                              Implikation
                              <Tooltip title="Eine Implikation bedeutet: Wenn ein bestimmtes Kleidungstyp getragen wird, muss auch ein anderes spezifisches Kleidungstyp getragen werden." placement="right">
                                <InfoIcon className="info-icon" />
                              </Tooltip>
                            </Box>
                          </MenuItem>
                          <MenuItem value="Mutex">
                            <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', width: '100%' }}>
                              Mutex
                              <Tooltip title="Ein Mutex bedeutet: Zwei ausgewählte Kleidungstypen können nicht zusammen in einem Outfit getragen werden." placement="right">
                                <InfoIcon className="info-icon" />
                              </Tooltip>
                            </Box>
                          </MenuItem>
                          <MenuItem value="Kardinalität">
                            <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', width: '100%' }}>
                              Kardinalität
                              <Tooltip title="Eine Kardinalität legt fest, wie oft ein bestimmter Kleidungstyp in einem Outfit vorkommen muss." placement="right">
                                <InfoIcon className="info-icon" />
                              </Tooltip>
                            </Box>
                          </MenuItem>
                        </Select>
                      </FormControl>
                    </Box>

                    {constraints[0].type && (
                      <>
                        {constraints[0].type === "Kardinalität" ? (
                          <>
                            <Divider sx={{ my: 2 }} />
                            <Typography
                              variant="body1"
                              className="constraint-description"
                            >
                              "In einem Outfit muss genau...
                            </Typography>
                            <Box sx={{ mb: 2 }}>
                              <TextField
                                label="Anzahl"
                                type="number"
                                fullWidth
                                value={kardinalitaetData.anzahl}
                                onChange={(e) =>
                                  setkardinalitaetData({
                                    ...kardinalitaetData,
                                    anzahl: e.target.value,
                                  })
                                }
                              />
                            </Box>
                            <Box sx={{ mb: 2 }}>
                              <FormControl fullWidth variant="outlined" required>
                                <InputLabel>Kleidungstyp</InputLabel>
                                <Select
                                  label="Kleidungstyp"
                                  required
                                  value={kardinalitaetData.bezugsobjekt}
                                  onChange={(e) =>
                                    setkardinalitaetData({
                                      ...kardinalitaetData,
                                      bezugsobjekt: e.target.value,
                                    })
                                  }
                                >
                                  <MenuItem value="">
                                    <em>Wähle einen Typ</em>
                                  </MenuItem>
                                  {kleidungstypen.map((typ) => (
                                    <MenuItem key={typ.id} value={typ.id}>
                                      {typ.bezeichnung}
                                    </MenuItem>
                                  ))}
                                </Select>
                              </FormControl>
                            </Box>
                            <Typography
                              variant="body1"
                              className="constraint-description"
                            >
                              ...enthalten sein."
                            </Typography>
                          </>
                        ) : constraints[0].type === "Implikation" ? (
                          <>
                            <Divider sx={{ my: 2 }} />
                            <Typography
                              variant="body1"
                              className="constraint-description"
                            >
                              "Wenn...
                            </Typography>
                            <Box sx={{ mb: 2 }}>
                              <FormControl fullWidth variant="outlined" required>
                                <InputLabel>Kleidungstyp 1</InputLabel>
                                <Select
                                  label="Kleidungstyp 1"
                                  required
                                  value={implikationData.bezugsobjekt1}
                                  onChange={(e) =>
                                    setimplikationData({
                                      ...implikationData,
                                      bezugsobjekt1: e.target.value,
                                    })
                                  }
                                >
                                  <MenuItem value="">
                                    <em>Wähle einen Typ</em>
                                  </MenuItem>
                                  {kleidungstypen.map((typ) => (
                                    <MenuItem key={typ.id} value={typ.id}>
                                      {typ.bezeichnung}
                                    </MenuItem>
                                  ))}
                                </Select>
                              </FormControl>
                            </Box>
                            <Typography
                              variant="body1"
                              className="constraint-description"
                            >
                              ... getragen wird, muss auch...
                            </Typography>
                            <Box sx={{ mb: 2 }}>
                              <FormControl fullWidth variant="outlined" required>
                                <InputLabel>Kleidungstyp 2</InputLabel>
                                <Select
                                  label="Kleidungstyp 2"
                                  required
                                  value={implikationData.bezugsobjekt2}
                                  onChange={(e) =>
                                    setimplikationData({
                                      ...implikationData,
                                      bezugsobjekt2: e.target.value,
                                    })
                                  }
                                >
                                  <MenuItem value="">
                                    <em>Wähle einen Typ</em>
                                  </MenuItem>
                                  {kleidungstypen.map((typ) => (
                                    <MenuItem key={typ.id} value={typ.id}>
                                      {typ.bezeichnung}
                                    </MenuItem>
                                  ))}
                                </Select>
                              </FormControl>
                            </Box>
                            <Typography
                              variant="body1"
                              className="constraint-description"
                            >
                              ... getragen werden."
                            </Typography>
                          </>
                        ) : constraints[0].type === "Mutex" ? (
                          <>
                            <Divider sx={{ my: 2 }} />
                            <Box sx={{ mb: 2 }}>
                              <FormControl fullWidth variant="outlined" required>
                                <InputLabel>Kleidungstyp 1</InputLabel>
                                <Select
                                  label="Kleidungstyp 1"
                                  required
                                  value={mutexData.bezugsobjekt1}
                                  onChange={(e) =>
                                    setmutexData({
                                      ...mutexData,
                                      bezugsobjekt1: e.target.value,
                                    })
                                  }
                                >
                                  <MenuItem value="">
                                    <em>Wähle einen Typ</em>
                                  </MenuItem>
                                  {kleidungstypen.map((typ) => (
                                    <MenuItem key={typ.id} value={typ.id}>
                                      {typ.bezeichnung}
                                    </MenuItem>
                                  ))}
                                </Select>
                              </FormControl>
                            </Box>
                            <Typography
                              variant="body1"
                              className="constraint-description"
                            >
                              und...
                            </Typography>
                            <Box sx={{ mb: 2 }}>
                              <FormControl fullWidth variant="outlined" required>
                                <InputLabel>Kleidungstyp 2</InputLabel>
                                <Select
                                  label="Kleidungstyp 2"
                                  required
                                  value={mutexData.bezugsobjekt2}
                                  onChange={(e) =>
                                    setmutexData({
                                      ...mutexData,
                                      bezugsobjekt2: e.target.value,
                                    })
                                  }
                                >
                                  <MenuItem value="">
                                    <em>Wähle einen Typ</em>
                                  </MenuItem>
                                  {kleidungstypen.map((typ) => (
                                    <MenuItem key={typ.id} value={typ.id}>
                                      {typ.bezeichnung}
                                    </MenuItem>
                                  ))}
                                </Select>
                              </FormControl>
                            </Box>
                            <Typography
                              variant="body1"
                              sx={{
                                mb: 2,
                                fontStyle: 'italic',
                                color: 'text.secondary'
                              }}
                            >
                              ...können nicht zusammen getragen werden.
                            </Typography>
                          </>
                        ) : null}

                        <Box display="flex" justifyContent="space-between">
                          <Button
                            variant="contained"
                            onClick={saveConstraint}
                            sx={{
                              backgroundColor: '#1976d2',
                              color: 'white',
                              '&:hover': {
                                backgroundColor: '#1565c0',
                              }
                            }}
                          >
                            Hinzufügen
                          </Button>
                        </Box>
                      </>
                    )}
                  </CardContent>
                </Card>
              )}

              {constraints.length === 0 && (
                <Box className="add-constraint-box">
                  <Button
                    variant="contained"
                    color="primary"
                    startIcon={<AddIcon />}
                    onClick={addConstraint}
                  >
                    Constraint hinzufügen
                  </Button>
                </Box>
              )}
            </CardContent>
          </Card>
        </Box>

        {/* Zweiter Bereich: Übersicht der bestehenden Constraints }
        <Box>
          <Typography
            variant="h6"
            className="section-header"
          >
            Übersicht aller Constraints
          </Typography>

          <Card className="constraints-overview-card">
            <CardContent>
              <Box className="constraints-overview-container">
                <Card className="constraint-type-card">
                  <Typography variant="h6" className="section-header">
                    Implikation
                    <Tooltip title="Eine Implikation bedeutet: Wenn ein bestimmtes Kleidungstyp getragen wird, muss auch ein anderes spezifisches Kleidungstyp getragen werden." placement="right">
                      <InfoIcon className="info-icon" />
                    </Tooltip>
                  </Typography>
                  {implikation.length === 0 ? (
                    <Box className="empty-constraint-message">
                      Keine Implikation gespeichert
                    </Box>
                  ) : (
                    implikation.map((item, index) => (
                      <Card key={index} className="constraint-item-card">
                        <CardContent className="constraint-content">
                          <Box className="constraint-box">
                            {editImplikationIndex === index ? (
                              <>
                                <Box className="edit-mode-container">
                                  <FormControl size="small" className="form-control-width">
                                    <InputLabel>Kleidungstyp 1</InputLabel>
                                    <Select
                                      value={editImplikation.bezugsobjekt1}
                                      onChange={(e) => {
                                        setEditImplikation({
                                          ...editImplikation,
                                          bezugsobjekt1: e.target.value
                                        });
                                        setHasImplikationChanges(true);
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
                                      value={editImplikation.bezugsobjekt2}
                                      onChange={(e) => {
                                        setEditImplikation({
                                          ...editImplikation,
                                          bezugsobjekt2: e.target.value
                                        });
                                        setHasImplikationChanges(true);
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

                                <Box className="action-buttons-container">
                                  <Tooltip title="Speichern">
                                    <span>
                                      <IconButton
                                        size="small"
                                        onClick={SaveEditImplikation}
                                        color="primary"
                                        disabled={!hasImplikationChanges}
                                      >
                                        <SaveIcon />
                                      </IconButton>
                                    </span>
                                  </Tooltip>
                                  <Tooltip title="Abbrechen">
                                    <IconButton
                                      size="small"
                                      onClick={() => {
                                        setEditImplikationIndex(null);
                                        setEditImplikation({});
                                        setHasImplikationChanges(false);
                                      }}
                                      color="error"
                                    >
                                      <CloseIcon />
                                    </IconButton>
                                  </Tooltip>
                                </Box>
                              </>
                            ) : (
                              // Anzeigemodus
                              <>
                                <Typography className="constraint-text">
                                  Wenn{' '}
                                  <Box component="span" className="constraint-type">
                                    {getKleidungstypBezeichnung(item.bezugsobjekt1)}
                                  </Box>{' '}
                                  getragen wird, muss auch{' '}
                                  <Box component="span" className="constraint-type">
                                    {getKleidungstypBezeichnung(item.bezugsobjekt2)}
                                  </Box>{' '}
                                  getragen werden
                                </Typography>
                                <Box className="constraint-actions">
                                  <Tooltip title="Bearbeiten">
                                    <IconButton
                                      color="primary"
                                      onClick={() => EditClickImplikation(index, item)}
                                      size="small"
                                    >
                                      <EditIcon />
                                    </IconButton>
                                  </Tooltip>
                                  <Tooltip title="Löschen">
                                    <IconButton
                                      color="error"
                                      onClick={() => DeleteImplikation(item.id)}
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

                {/* Mutex Card }
                <Card className="constraint-type-card">
                  <Typography variant="h6" className="section-header">
                    Mutex
                    <Tooltip title="Ein Mutex bedeutet: Zwei ausgewählte Kleidungstypen können nicht zusammen in einem Outfit getragen werden." placement="right">
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
                              // Bearbeitungsmodus
                              <>
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
                                        onClick={SaveEditMutex}
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
                              </>
                            ) : (
                              // Anzeigemodus
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
                                <Box sx={{
                                  display: 'flex',
                                  alignItems: 'center',
                                  margin: 0
                                }}>
                                  <Tooltip title="Bearbeiten">
                                    <IconButton
                                      color="primary"
                                      onClick={() => EditClickMutex(index, item)}
                                      size="small"
                                    >
                                      <EditIcon />
                                    </IconButton>
                                  </Tooltip>
                                  <Tooltip title="Löschen">
                                    <IconButton
                                      color="error"
                                      onClick={() => DeleteMutex(item.id)}
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

                {/* Kardinalitäten Card }
                <Card className="constraint-type-card">
                  <Typography variant="h6" className="section-header">
                    Kardinalitäten
                    <Tooltip title="Eine Kardinalität legt fest, wie oft ein bestimmter Kleidungstyp in einem Outfit vorkommen muss." placement="right">
                      <InfoIcon className="info-icon" />
                    </Tooltip>
                  </Typography>
                  {kardinalitaet.length === 0 ? (
                    <Box className="empty-constraint-message">
                      Keine Kardinalitäten gespeichert
                    </Box>
                  ) : (
                    kardinalitaet.map((item, index) => (
                      <Card key={index} className="constraint-item-card">
                        <CardContent className="constraint-content">
                          <Box className="constraint-box">
                            {editKardinalitaetIndex === index ? (
                              // Bearbeitungsmodus
                              <>
                                <Box className="edit-mode-container">
                                  <FormControl size="small" className="form-control-width">
                                    <InputLabel>Kleidungstyp</InputLabel>
                                    <Select
                                      value={editKardinalitaet.bezugsobjekt}
                                      onChange={(e) => {
                                        setEditKardinalitaet({
                                          ...editKardinalitaet,
                                          bezugsobjekt: e.target.value
                                        });
                                        setHasKardinalitaetChanges(true);
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
                                    value={editKardinalitaet.anzahl}
                                    onChange={(e) => {
                                      setEditKardinalitaet({
                                        ...editKardinalitaet,
                                        anzahl: e.target.value
                                      });
                                      setHasKardinalitaetChanges(true);
                                    }}
                                  />
                                </Box>

                                <Box sx={{ display: 'flex', gap: 0 }}>
                                  <Tooltip title="Speichern">
                                    <span>
                                      <IconButton
                                        size="small"
                                        onClick={SaveEditKardinalitaet}
                                        color="primary"
                                        disabled={!hasKardinalitaetChanges}
                                      >
                                        <SaveIcon />
                                      </IconButton>
                                    </span>
                                  </Tooltip>
                                  <Tooltip title="Abbrechen">
                                    <IconButton
                                      size="small"
                                      onClick={() => {
                                        setEditKardinalitaetIndex(null);
                                        setEditKardinalitaet({});
                                        setHasKardinalitaetChanges(false);
                                      }}
                                      color="error"
                                    >
                                      <CloseIcon />
                                    </IconButton>
                                  </Tooltip>
                                </Box>
                              </>
                            ) : (
                              // Anzeigemodus
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
                                      onClick={() => EditClickKardinalitaet(index, item)}
                                      size="small"
                                    >
                                      <EditIcon />
                                    </IconButton>
                                  </Tooltip>
                                  <Tooltip title="Löschen">
                                    <IconButton
                                      color="error"
                                      onClick={() => DeleteKardinalitaet(item.id)}
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
        </Box>
      </Box>

      {/* Dialog }
      <Dialog
        open={openDialog}
        onClose={handleCloseDialog}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">
          {"Hinweis"}
        </DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            {dialogMessage}
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button
            onClick={handleCloseDialog}
            variant="contained"
            className="dialog-button"
            autoFocus
          >
            OK
          </Button>
        </DialogActions>
      </Dialog>
    </Card>
  );
}

export default Constraints;

 */