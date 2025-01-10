import React, { useState, useEffect } from 'react';
import {
  Container,
  TextField,
  Button,
  Typography,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Box,
  Alert,
  CircularProgress
} from '@mui/material';
import { useAuth } from '../../context/AuthContext';
import DigitalWardrobeAPI from '../../api/DigitalWardrobeAPI';

const Profile = () => {
  const { user } = useAuth();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [userBO, setUserBO] = useState(null);
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    nickName: ''
  });
  const [allUsers, setAllUsers] = useState([]);

  // läd user daten 
  useEffect(() => {
    if (user?.uid) {
      loadUserData();
    }
  }, [user]);

  // funktion um alle nötigen user daten zu laden
  const loadUserData = async () => {
    setLoading(true);
    setError(null);
    try {
      // get user daten vom jetzigen nutzer
      const userData = await DigitalWardrobeAPI.getAPI().getUserByGoogleId(user.uid);
      if (userData) {
        setUserBO(userData);
        setFormData({
          firstName: userData.getFirstName(),
          lastName: userData.getLastName(),
          nickName: userData.getNickname()
        });
      }

      // get alle user aus der tabelle
      const users = await DigitalWardrobeAPI.getAPI().getUsers();
      setAllUsers(users);
    } catch (error) {
      console.error('Error loading user data:', error);
      setError('Failed to load user data. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  // handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault();
    setError(null);
    try {
      if (!userBO) {
        throw new Error('No user data found');
      }

      // update user info
      const updatedUser = {
        ...userBO,
        firstName: formData.firstName,
        lastName: formData.lastName,
        nickName: formData.nickName
      };

      await DigitalWardrobeAPI.getAPI().updateUser(updatedUser);
      await loadUserData(); // neu laden um updates zu sehen
    } catch (error) {
      console.error('Error updating profile:', error);
      setError('Failed to update profile. Please try again.');
    }
  };

  if (loading) {
    return (
      <Container sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}>
        <CircularProgress />
      </Container>
    );
  }

  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      {error && (
        <Alert severity="error" sx={{ mb: 2 }}>
          {error}
        </Alert>
      )}

      <Paper elevation={3} sx={{ p: 4, mb: 4 }}>
        <Typography variant="h5" gutterBottom>
          Profil anlegen
        </Typography>

        <form onSubmit={handleSubmit}>
          <TextField
            fullWidth
            label="Vorname"
            value={formData.firstName}
            onChange={(e) => setFormData({...formData, firstName: e.target.value})}
            margin="normal"
            required
          />
          <TextField
            fullWidth
            label="Nachname"
            value={formData.lastName}
            onChange={(e) => setFormData({...formData, lastName: e.target.value})}
            margin="normal"
            required
          />
          <TextField
            fullWidth
            label="Benutzername"
            value={formData.nickName}
            onChange={(e) => setFormData({...formData, nickName: e.target.value})}
            margin="normal"
            required
          />

          <Button
            variant="contained"
            color="primary"
            type="submit"
            fullWidth
            sx={{ mt: 3 }}
          >
            PROFIL ANLEGEN
          </Button>
        </form>
      </Paper>

      <Box sx={{ mt: 4 }}>
        <Typography variant="h6" gutterBottom>
          Angelegte Benutzer
        </Typography>
        <TableContainer component={Paper}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>Index</TableCell>
                <TableCell>Vorname</TableCell>
                <TableCell>Nachname</TableCell>
                <TableCell>Benutzername</TableCell>
                <TableCell>Email</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {allUsers.length === 0 ? (
                <TableRow>
                  <TableCell colSpan={5} align="center">
                    Keine Benutzer angelegt.
                  </TableCell>
                </TableRow>
              ) : (
                allUsers.map((user, index) => (
                  <TableRow key={user.getId()}>
                    <TableCell>{index + 1}</TableCell>
                    <TableCell>{user.getFirstName()}</TableCell>
                    <TableCell>{user.getLastName()}</TableCell>
                    <TableCell>{user.getNickname()}</TableCell>
                    <TableCell>{user.getEmail()}</TableCell>
                  </TableRow>
                ))
              )}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    </Container>
  );
};

export default Profile;