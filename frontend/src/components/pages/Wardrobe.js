import React, { useState, useEffect } from 'react';
import {
  Container,
  Paper,
  TextField,
  Button,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Box,
  Alert,
  CircularProgress
} from '@mui/material';
import { useAuth } from '../../context/AuthContext';
import DigitalWardrobeAPI from '../../api/DigitalWardrobeAPI';

const Wardrobe = () => {
  // State management with loading and error states for better user experience
  const { user } = useAuth();
  const [wardrobe, setWardrobe] = useState(null);
  const [clothingItems, setClothingItems] = useState([]);
  const [clothingTypes, setClothingTypes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [newItem, setNewItem] = useState({
    name: '',
    typeId: ''
  });

  // Load initial data when component mounts
  useEffect(() => {
    if (user?.uid) {
      loadInitialData();
    }
  }, [user]);

  // Combined function to load all necessary data
  const loadInitialData = async () => {
    setLoading(true);
    setError(null);
    try {
      // First, get the user's wardrobe
      const wardrobeData = await DigitalWardrobeAPI.getAPI().getWardrobeByGoogleUserId(user.uid);
      setWardrobe(wardrobeData);

      // If we have a wardrobe, load its items
      if (wardrobeData) {
        const items = await DigitalWardrobeAPI.getAPI().getClothingItems(wardrobeData.getId());
        setClothingItems(items);
      }

      // Load clothing types regardless of wardrobe status
      const types = await DigitalWardrobeAPI.getAPI().getClothingTypes();
      setClothingTypes(types);
    } catch (error) {
      console.error('Error loading wardrobe data:', error);
      setError('Failed to load wardrobe data. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  // Handle form submission for new clothing item
  const handleSubmit = async (event) => {
    event.preventDefault();
    setError(null);
    try {
      if (!wardrobe) {
        throw new Error('No wardrobe found');
      }

      // Create and save new clothing item
      const newClothingItem = {
        wardrobeId: wardrobe.getId(),
        name: newItem.name,
        typeId: newItem.typeId
      };

      await DigitalWardrobeAPI.getAPI().addClothingItem(wardrobe.getId(), newClothingItem);
      
      // Reset form and reload items
      setNewItem({ name: '', typeId: '' });
      await loadInitialData();
    } catch (error) {
      console.error('Error adding clothing item:', error);
      setError('Failed to add clothing item. Please try again.');
    }
  };

  // Show loading state
  if (loading) {
    return (
      <Container sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}>
        <CircularProgress />
      </Container>
    );
  }

  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      {/* Error display */}
      {error && (
        <Alert severity="error" sx={{ mb: 2 }}>
          {error}
        </Alert>
      )}

      {/* Add new clothing item form */}
      <Paper elevation={3} sx={{ p: 4, mb: 4 }}>
        <Typography variant="h5" gutterBottom>
          Neues Kleidungsstück anlegen
        </Typography>
        
        <form onSubmit={handleSubmit}>
          <TextField
            fullWidth
            label="Name des Kleidungsstücks"
            value={newItem.name}
            onChange={(e) => setNewItem({...newItem, name: e.target.value})}
            margin="normal"
            required
          />
          
          <FormControl fullWidth margin="normal">
            <InputLabel>Kleidungstyp auswählen</InputLabel>
            <Select
              value={newItem.typeId}
              onChange={(e) => setNewItem({...newItem, typeId: e.target.value})}
              required
            >
              {clothingTypes.map((type) => (
                <MenuItem key={type.getId()} value={type.getId()}>
                  {type.getName()}
                </MenuItem>
              ))}
            </Select>
          </FormControl>

          <Button
            variant="contained"
            color="primary"
            type="submit"
            fullWidth
            sx={{ mt: 3 }}
          >
            KLEIDUNGSSTÜCK HINZUFÜGEN
          </Button>
        </form>
      </Paper>

      {/* Display clothing items */}
      <Paper elevation={3} sx={{ p: 4 }}>
        <Typography variant="h6" gutterBottom>
          Angelegte Kleidungsstücke
        </Typography>
        
        <TableContainer>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>Kleidungsname</TableCell>
                <TableCell>Kleidungstyp</TableCell>
                <TableCell>Aktionen</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {clothingItems.length === 0 ? (
                <TableRow>
                  <TableCell colSpan={3} align="center">
                    Keine Kleidungsstücke vorhanden
                  </TableCell>
                </TableRow>
              ) : (
                clothingItems.map((item) => (
                  <TableRow key={item.getId()}>
                    <TableCell>{item.getName()}</TableCell>
                    <TableCell>
                      {clothingTypes.find(t => t.getId() === item.getTypeId())?.getName()}
                    </TableCell>
                    <TableCell>
                      
                    </TableCell>
                  </TableRow>
                ))
              )}
            </TableBody>
          </Table>
        </TableContainer>
      </Paper>
    </Container>
  );
};

export default Wardrobe;