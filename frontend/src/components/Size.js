import React, { useState, useEffect } from 'react';
import WardrobeAPI from '../API/DigitalWardrobeAPI';
import SizeBO from '../API/Size';
import { getAuth } from 'firebase/auth';
import {
  Container,
  Typography,
  Box,
  Button,
  TextField,
  List,
  ListItem,
  ListItemText,
  IconButton,
  Snackbar,
  Alert,
  LinearProgress
} from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';

// Liste der erlaubten Größen für Kleidungsstücke
const realSizes = ['XS', 'S', 'M', 'L', 'XL', 'XXL', '3XL'];

const SizeList = ({ wardrobeId }) => {
  const [sizes, setSizes] = useState([]);
  const [newSize, setNewSize] = useState('');
  const [error, setError] = useState('');
  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchSizes();
  }, []);

  const fetchSizes = async () => {
    setLoading(true);
    const auth = getAuth();
    const currentUser = auth.currentUser;
    const wardrobe_id = await WardrobeAPI.getAPI().getWardrobeIdByGoogleUserId(currentUser.uid);
    try {
      const fetchedSizes = await WardrobeAPI.getAPI().getSizeByWardrobeId(wardrobe_id.wardrobe_id);
      setSizes(fetchedSizes || []);
    } catch (error) {
      console.error('Failed to fetch sizes:', error);
      setSizes([]);
    }
    setLoading(false);
  };

  const handleAddSize = async () => {
    if (!realSizes.includes(newSize.toUpperCase())) {
      setError('Invalid size. Please enter a valid clothing size.');
      return;
    }

    const auth = getAuth();
    const currentUser = auth.currentUser;
    try {
      const wardrobe_id = await WardrobeAPI.getAPI().getWardrobeIdByGoogleUserId(currentUser.uid);
      const sizeBO = new SizeBO(newSize, wardrobe_id.wardrobe_id);

      await WardrobeAPI.getAPI().addSize(sizeBO);
      fetchSizes();
      setNewSize('');
      setError('');
      setSnackbarOpen(true);
    } catch (error) {
      console.error('Failed to add size:', error);
      setError('Failed to add size');
    }
  };

  const handleDeleteSize = async (sizeId) => {
    try {
      await WardrobeAPI.getAPI().deleteSize(sizeId);
      fetchSizes();
    } catch (error) {
      console.error('Failed to delete size:', error);
    }
  };

  const handleSnackbarClose = () => {
    setSnackbarOpen(false);
  };

  return (
    <Container>
      <Typography variant="h4" gutterBottom style={{ display: 'flex', justifyContent: 'center', textAlign: 'center', border: '1px solid #ccc', borderRadius: '5px', margin: '20px' }}>
        All available sizes
      </Typography>
      {loading ? (
        <LinearProgress />
      ) : sizes.length === 0 ? (
        <Typography variant="body1" style={{ textAlign: 'center', marginTop: '20px' }}>
          No sizes available.
        </Typography>
      ) : (
        <List>
          {sizes.map((size) => (
            <ListItem style={{ border: '1px solid #ccc', borderRadius: '5px', marginBottom: '5px' }}
              key={size.id}
              secondaryAction={
                <IconButton edge="end" aria-label="delete" onClick={() => handleDeleteSize(size.id)}>
                  <DeleteIcon />
                </IconButton>
              }
            >
              <ListItemText primary={size.designation} />
            </ListItem>
          ))}
        </List>
      )}
      <Box mt={4}>
        <Typography variant="h5" gutterBottom>
          Add Size
        </Typography>

        <TextField
          label="New Size"
          value={newSize}
          onChange={(e) => setNewSize(e.target.value)}
          fullWidth
          variant="outlined"
        />
        <Box mt={2}>
          <Button variant="contained" color="primary" onClick={handleAddSize} sx={{ width: '150px', height: '40px' }}>
            Add
          </Button>
        </Box>

        {error && (
          <Box mt={2}>
            <Alert severity="error">{error}</Alert>
          </Box>
        )}
      </Box>

      <Snackbar
        open={snackbarOpen}
        autoHideDuration={6000}
        onClose={handleSnackbarClose}
      >
        <Alert onClose={handleSnackbarClose} severity="success" sx={{ width: '100%' }}>
          Size added successfully!
        </Alert>
      </Snackbar>
    </Container>
  );
};

export default SizeList;