import React, { useState, useEffect } from "react";
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
  Box,
  MenuItem,
  Select,
  InputLabel,
  FormControl,
} from "@mui/material";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";

const Wardrobe = () => {
  const [wardrobe, setWardrobe] = useState([]);
  const [openDialog, setOpenDialog] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [currentClothingIndex, setCurrentClothingIndex] = useState(null);
  const [clothingTypes, setClothingTypes] = useState(["T-Shirt", "Hose", "Jacke"]); // Vorhandene Typen
  const [newType, setNewType] = useState(""); // Neuer Kleidungsstücktyp

  const [newClothing, setNewClothing] = useState({
    item_name: "",
    clothing_type: null,
  });

  // Load wardrobe from localStorage when page loads
  useEffect(() => {
    const savedWardrobe = localStorage.getItem("wardrobe");
    if (savedWardrobe) {
      setWardrobe(JSON.parse(savedWardrobe));
    }
  }, []);

  const handleAddClothing = () => {
    const updatedWardrobe = [...wardrobe, newClothing];
    setWardrobe(updatedWardrobe);

    // Save to localStorage
    localStorage.setItem("wardrobe", JSON.stringify(updatedWardrobe));

    setOpenDialog(false);
    setNewClothing({ item_name: "", clothing_type: "" });
  };

  const handleEditClothing = () => {
    const updatedWardrobe = [...wardrobe];
    updatedWardrobe[currentClothingIndex] = newClothing;
    setWardrobe(updatedWardrobe);

    localStorage.setItem("wardrobe", JSON.stringify(updatedWardrobe));

    setOpenDialog(false);
    setIsEditing(false);
    setNewClothing({ item_name: "", clothing_type: ""});
    setCurrentClothingIndex(null);
  };

  const handleDeleteClothing = (index) => {
    const updatedWardrobe = wardrobe.filter((_, i) => i !== index);
    setWardrobe(updatedWardrobe);

    localStorage.setItem("wardrobe", JSON.stringify(updatedWardrobe));
  };

  const handleAddNewType = () => {
    if (newType && !clothingTypes.includes(newType)) {
      setClothingTypes([...clothingTypes, newType]);
      setNewType("");
    }
  };

  return (
    <div className="p-4">
      <Grid container spacing={3} alignItems="center" className="mb-4">
        <Grid item xs>
          <Typography variant="h4">Mein Kleiderschrank</Typography>
        </Grid>
        <Grid item>
          <Button variant="contained" color="primary" onClick={() => setOpenDialog(true)}>
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
                  Typ: {clothing.clothing_type}
                </Typography>
              </CardContent>
              <Box display="flex" justifyContent="flex-end">
                <IconButton color="primary" onClick={() => {
                  setIsEditing(true);
                  setCurrentClothingIndex(index);
                  setNewClothing(wardrobe[index]);
                  setOpenDialog(true);
                }}>
                  <EditIcon />
                </IconButton>
                <IconButton color="secondary" onClick={() => handleDeleteClothing(index)}>
                  <DeleteIcon />
                </IconButton>
              </Box>
            </Card>
          </Grid>
        ))}
      </Grid>

      <Dialog open={openDialog} onClose={() => setOpenDialog(false)}>
        <DialogTitle>{isEditing ? "Kleidungsstück bearbeiten" : "Neues Kleidungsstück hinzufügen"}</DialogTitle>
        <DialogContent>
          <TextField
            fullWidth
            margin="normal"
            label="Name des Kleidungsstücks"
            value={newClothing.item_name}
            onChange={(e) => setNewClothing({ ...newClothing, item_name: e.target.value })}
            required
          />

          {/* Select Dropdown for Clothing Types */}
          <FormControl fullWidth margin="normal">
            <InputLabel>Typ des Kleidungsstücks</InputLabel>
            <Select
              value={newClothing.clothing_type || ""}
              onChange={(e) => setNewClothing({ ...newClothing, clothing_type: e.target.value })}
              required
            >
              {clothingTypes.map((type, index) => (
                <MenuItem key={index} value={type}>
                  {type}
                </MenuItem>
              ))}
            </Select>
          </FormControl>

          {/* Option to Add New Clothing Type */}
          <Box display="flex" gap={1} alignItems="center" marginY={2}>
            <TextField
              label="Neuen Typ hinzufügen"
              value={newType}
              onChange={(e) => setNewType(e.target.value)}
            />
            <Button variant="outlined" onClick={handleAddNewType}>
              Hinzufügen
            </Button>
          </Box>

        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenDialog(false)}>Abbrechen</Button>
          <Button onClick={isEditing ? handleEditClothing : handleAddClothing} color="primary">
            {isEditing ? "Ändern" : "Hinzufügen"}
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default Wardrobe;
