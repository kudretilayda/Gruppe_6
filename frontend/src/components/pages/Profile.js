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
    Box
}  from '@mui/material';

import { useAuth } from '../../context/AuthContext';
import DigitalWardrobeAPI from '../../api/DigitalWardrobeAPI';
import UserBO from '../../api/UserBO';

const Profile = () => {
    const { user } = useAuth();
    const [editMode, setEditMode] = useState(false);
    const [UserBO, setUserBO] = useState(null);
    const [formData, setFormData] = useState({
        firstName: '',
        lastName: '',
        nickName: '',
    });
    const [allUsers, setAllUsers] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        if (user?.uid) {
            fetchUserData();
            fetchAllUsers();
        }
    }, [user]);

    const fetchUserData = async () => {
        try {
            const users = await DigitalWardrobeAPI.getAPI().getUserByGoogleID(user.uid);
            if (response) {
                setUserBO(response);
                setFormData({
                    firstname: response.getFirstName(),
                    lastname: response.getLastName(),
                    nickname: response.getNickname(),
                });
            }
        } catch (error) {
            console.error('Error fetching user data:', error);
            setError('Fehler beim laden der Benutzerdaten');
        }
    };

    const fetchAllUsers = async () => {
        try {
            const users = await DigitalWardrobeAPI.getAPI().getUsers();
            setAllUsers(users);
        } catch (error) {
            console.error('Error fetching all users:', error);
        }
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            if (UserBO) {
                const updateUserBO = new UserBO();
                updateUserBO.setID(UserBO.getID());
                updateUserBO.setGoogleID(UserBO.getGoogleID());
                updateUserBO.setFirstName(formData.firstName);
                updateUserBO.setLastName(formData.lastName);
                updateUserBO.setNickname(formData.nickName);
                updateUserBO.setEmail(UserBO.getEmail());

                await DigitalWardrobeAPI.getAPI().updateUser(updateUserBO);
                await fetchAllUsers();
                setEditMode(false);
            }
        } catch (error) {
            console.error('Error updating profile:', error);
            setError('Fehler beim aktualisieren des Profils');
        }
    };

    return (
        <Container maxWidth='lg' sx={{mt: 4}}>
            <Paper elevation={3} sx={{p: 4, mb: 4}}>
                <Typography variant='h5' gutterBottom>
                    Profil anlegen
                </Typography>

                <form onSubmit={handleSubmit}>
                    <TextField 
                        fullWidth
                        label="Vorname"
                        value={formData.firstName}
                        onChange={(e) => setFormData({...formData, firstName: e.target.value})}
                        margin='normal'
                        required
                    />
                    <TextField 
                        fullWidth
                        label = "Nachname"
                        value={formData.value}
                        onChange={(e) => setFormData({...formData, lastName: e.target.value})}
                        margin='normal'
                        required
                    />

                    <TextField 
                        fullWidth
                        label = "Benutzername"
                        value={formData.nickName}
                        onChange={(e) => setFormData({...formData, nickName: e.target.value})}
                        margin='normal'
                        required
                    />

                    <Button
                        variant='contained'
                        color='primary'
                        type='submit'
                        fullWidth
                        sx={{ mt: 3 }}
                    >
                        PROFIL ANLEGEN
                    </Button>

                </form>

            </Paper>

            {/* User Tabelle */}
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
                <TableCell>Aktionen</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {allUsers.length === 0 ? (
                <TableRow>
                  <TableCell colSpan={6} align="center">
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
                    <TableCell>
                    </TableCell>
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
