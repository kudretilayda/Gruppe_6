import React, { useState, useEffect } from 'react';
import { ListItemIcon, List, ListItem, ListItemText, CircularProgress, Typography, Box, Card, CardContent, Avatar, Divider, TextField, Button, Dialog, DialogActions, DialogContent, DialogTitle } from '@mui/material';
import { getAuth } from 'firebase/auth';
import WardrobeBO from '../API/WardrobeBO.js'; // Angepasst für Kleiderschrank
import HomeIcon from '@mui/icons-material/Home';
import { useNavigate } from 'react-router-dom';
import DigitalWardrobeAPI from "../api/DigitalWardrobeAPI";

// Komponente für den digitalen Kleiderschrank
const WardrobeList = ({ navigate }) => {
    const [users, setUsers] = useState([]);
    const [wardrobeName, setWardrobeName] = useState('');
    const [newWardrobeName, setNewWardrobeName] = useState('');
    const [newPassword, setNewPassword] = useState('');
    const [enteredPassword, setEnteredPassword] = useState('');
    const [deletePassword, setDeletePassword] = useState(''); // State für Passwort zum Löschen
    const [wardrobeId, setWardrobeId] = useState(null);
    const [selectedWardrobeId, setSelectedWardrobeId] = useState(null);
    const [clothingItems, setClothingItems] = useState([]); // Kleidungselemente
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [wardrobes, setWardrobes] = useState([]);
    const [dialogOpen, setDialogOpen] = useState(false);
    const [passwordDialogOpen, setPasswordDialogOpen] = useState(false);
    const [deleteDialogOpen, setDeleteDialogOpen] = useState(false); // Dialog für Löschung

    useEffect(() => {
        loadWardrobeUsers();
    }, []);

    // Methode zum Laden der Benutzer und Kleiderschrank-Daten
    const loadWardrobeUsers = async () => {
        const auth = getAuth();
        const currentUser = auth.currentUser;
        if (!currentUser) {
            setError("No user logged in");
            setLoading(false);
            return;
        }

        try {
            const userBO = await DigitalWardrobeAPI.getAPI().getUserByGoogleId(currentUser.uid);
            if (userBO && userBO.length > 0 && userBO[0].wardrobe_id) {
                const users = await DigitalWardrobeAPI.getAPI().getUsersByWardrobeID(userBO[0].wardrobe_id);
                const wardrobeArray = await DigitalWardrobeAPI.getAPI().getWardrobeByID(userBO[0].wardrobe_id);
                const wardrobe = wardrobeArray[0]; // Zugriff auf das erste Element
                setUsers(users);
                setWardrobeName(wardrobe.name);
                setNewWardrobeName(wardrobe.name);
                setWardrobeId(userBO[0].wardrobe_id);
                setClothingItems(wardrobe.clothing_items); // Kleidungsliste setzen
                setLoading(false);
            } else {
                setError("User has no associated wardrobe.");
                setLoading(false);
            }
        } catch (error) {
            setError(error.message);
            setLoading(false);
        }
    };

    // Methode zum Aktualisieren des Kleiderschrank-Namens
    const updateWardrobeName = async () => {
        const auth = getAuth();
        const currentUser = auth.currentUser;
        if (!currentUser) {
            setError("No user logged in");
            setLoading(false);
            return;
        }

        try {
            const wardrobeBO = new WardrobeBO(newWardrobeName, ClothingItems);
            wardrobeBO.setId(wardrobeId);
            await DigitalWardrobeAPI.getAPI().updateWardrobe(wardrobeBO);
            setWardrobeName(newWardrobeName);
        } catch (error) {
            setError(error.message);
            setLoading(false);
        }
    };

    // Handler für die Eingabe des Kleiderschrank-Namens
    const handleInputChangeWardrobeName = (event) => {
        setNewWardrobeName(event.target.value);
    };

    // Methode zum Hinzufügen eines neuen Kleiderschranks
    const addWardrobe = async () => {
        const auth = getAuth();
        const currentUser = auth.currentUser;
        if (!currentUser) {
            setError("No user logged in.");
            return;
        }

        if (!newWardrobeName.trim()) {
            alert("Wardrobe name cannot be empty.");
            return;
        }

        if (!newPassword.trim()) {
            alert("Password cannot be empty.");
            return;
        }

        try {
            let wardrobeBO = new WardrobeBO(newWardrobeName, []);
            wardrobeBO.setPassword(newPassword); // Passwort für den Kleiderschrank setzen
            const addedWardrobe = await DigitalWardrobeAPI.getAPI().addWardrobe(wardrobeBO);
            let userBOArray = await DigitalWardrobeAPI.getAPI().getUserByGoogleId(currentUser.uid);
            if (userBOArray && userBOArray.length > 0) {
                let userBO = userBOArray[0];
                userBO.wardrobe_id = addedWardrobe.id;
                await DigitalWardrobeAPI.getAPI().updateUser(userBO);

                setWardrobeId(addedWardrobe.id);
                setWardrobeName(newWardrobeName);
                setNewPassword('');
                setNewWardrobeName('');
                setDialogOpen(false);
                loadWardrobeUsers();
            } else {
                throw new Error("Failed to fetch user data for updating.");
            }
        } catch (error) {
            setError(error.message);
        }
    };

    // Methode zum Löschen des aktuellen Kleiderschranks
    const deleteCurrentWardrobe = async () => {
        const auth = getAuth();
        const currentUser = auth.currentUser;
        if (!currentUser) {
            setError("No user logged in");
            return;
        }
        try {
            const wardrobe_id = await DigitalWardrobeAPI.getAPI().getWardrobeIdByGoogleUserId(currentUser.uid);
            const wardrobeArray = await DigitalWardrobeAPI.getAPI().getWardrobeByID(wardrobe_id.wardrobe_id);
            const wardrobe = wardrobeArray[0];
            if (wardrobe.password) {
                setDeleteDialogOpen(true);
            } else {
                await DigitalWardrobeAPI.getAPI().deleteWardrobe(wardrobe_id.wardrobe_id);
                navigate('/home');
                auth.signOut();
            }
        } catch (error) {
            setError(error.message);
        }
    };

    // Dialoge für das Anzeigen und Erstellen von Kleiderschränken
    const renderDialogs = () => {
        return (
            <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)}>
                <DialogTitle>{wardrobes.length ? "Select or create a wardrobe" : "Create a wardrobe"}</DialogTitle>
                <DialogContent>
                    {error && <Typography color="error" variant="body2" gutterBottom>{error}</Typography>}
                    <List>
                        {wardrobes.map(w => (
                            <ListItem
                                button
                                key={w.id}
                                onClick={() => handleSelectWardrobe(w.id)}
                                sx={{
                                    margin: '10px 0',
                                    border: '1px solid #ccc',
                                    borderRadius: '8px',
                                    padding: '10px 20px',
                                    '&:hover': {
                                        backgroundColor: '#f0f0f0'
                                    }
                                }}
                            >
                                <ListItemIcon>
                                    <HomeIcon color="primary" />
                                </ListItemIcon>
                                <ListItemText primary={w.name} />
                            </ListItem>
                        ))}
                        <ListItem>
                            <TextField
                                label="New wardrobe name"
                                type="text"
                                fullWidth
                                variant="outlined"
                                value={newWardrobeName}
                                onChange={handleInputChangeWardrobeName}
                            />
                        </ListItem>
                        <ListItem>
                            <TextField
                                label="Password"
                                type="password"
                                fullWidth
                                variant="outlined"
                                value={newPassword}
                                onChange={(e) => setNewPassword(e.target.value)}
                            />
                        </ListItem>
                    </List>
                </DialogContent>
                <DialogActions>
                    <Button onClick={addWardrobe} color="primary">Add new wardrobe</Button>
                </DialogActions>
            </Dialog>
        );
    };

    // Weitere Dialoge für Passwort und Löschung
    const renderPasswordDialog = () => {
        return (
            <Dialog open={passwordDialogOpen} onClose={() => { setPasswordDialogOpen(false); setEnteredPassword(''); }}>
                <DialogTitle>Enter Wardrobe Password</DialogTitle>
                <DialogContent>
                    <TextField
                        label="Password"
                        type="password"
                        fullWidth
                        variant="outlined"
                        value={enteredPassword}
                        onChange={(e) => setEnteredPassword(e.target.value)}
                    />
                </DialogContent>
                <DialogActions>
                    <Button onClick={confirmPassword} color="primary">Confirm</Button>
                    <Button onClick={() => setPasswordDialogOpen(false)} color="secondary">Cancel</Button>
                </DialogActions>
            </Dialog>
        );
    };

    const renderDeleteDialog = () => {
        return (
            <Dialog open={deleteDialogOpen} onClose={() => { setDeleteDialogOpen(false); setDeletePassword(''); }}>
                <DialogTitle>Enter Wardrobe Delete Password</DialogTitle>
                <DialogContent style={{color:'red'}}>
                This will delete all clothing and accessories from the current wardrobe, are you sure you want to delete this wardrobe?
                    <TextField
                        label="Delete Password"
                        type="password"
                        fullWidth
                        variant="outlined"
                        value={deletePassword}
                        onChange={(e) => setDeletePassword(e.target.value)}
                    />
                </DialogContent>
                <DialogActions>
                    <Button onClick={confirmDeleteWardrobe} color="primary">Confirm Delete</Button>
                    <Button onClick={() => setDeleteDialogOpen(false)} color="secondary">Cancel</Button>
                </DialogActions>
            </Dialog>
        );
    };

    if (loading) return <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh' }}><CircularProgress /></Box>;

    return (
        <div>
            {renderDialogs()}
            {renderPasswordDialog()}
            {renderDeleteDialog()}

            <Typography variant="h4">{wardrobeName}</Typography>
            <Divider sx={{ marginY: 2 }} />
            <List>
                {clothingItems.map((item, index) => (
                    <ListItem key={index} sx={{ padding: '10px' }}>
                        <ListItemIcon>
                            <Avatar src={item.imageUrl} />
                        </ListItemIcon>
                        <ListItemText primary={item.name} />
                    </ListItem>
                ))}
            </List>
            <Button variant="contained" color="primary" onClick={() => setDialogOpen(true)}>Manage Wardrobe</Button>
        </div>
    );
};

export default WardrobeList;
