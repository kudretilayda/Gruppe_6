import React, { useState, useEffect } from 'react';
import { Button, TextField, Grid, Typography, Box, MenuItem, Select, FormControl, InputLabel } from '@mui/material';
import { useAuth } from '../context/AuthContext'; // Falls du ein AuthContext verwendest
import { useNavigate } from 'react-router-dom'; // Für das Weiterleiten nach dem Logout

const Settings = () => {
  const { logout, changePassword, currentUser } = useAuth(); // Wir nehmen an, dass diese Funktionen aus dem AuthContext kommen
  const navigate = useNavigate();

  const [currentPassword, setCurrentPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [passwordError, setPasswordError] = useState('');

  const [clothingStats, setClothingStats] = useState([]); // Zum Speichern der Statistik

  // Funktion zum Ändern des Passworts
  const handlePasswordChange = async (e) => {
    e.preventDefault();
    try {
      if (currentPassword && newPassword) {
        await changePassword(currentPassword, newPassword); // Annahme: changePassword existiert im AuthContext
        alert("Passwort erfolgreich geändert!");
        setCurrentPassword('');
        setNewPassword('');
      } else {
        setPasswordError("Bitte beide Felder ausfüllen.");
      }
    } catch (error) {
      setPasswordError("Es gab einen Fehler beim Ändern des Passworts.");
    }
  };

  // Funktion für den Logout
  const handleLogout = () => {
    logout(); // Annahme: logout entfernt den Benutzer aus dem AuthContext
    navigate('/login'); // Leitet den Benutzer zur Login-Seite weiter
  };

  // Beispiel für eine einfache Statistikberechnung
  useEffect(() => {
    // Angenommen, Kleidungshistorie ist ein Array mit Daten, das du irgendwo speicherst
    const clothingHistory = JSON.parse(localStorage.getItem('clothingHistory')) || [];

    // Gruppiere nach Monat
    const stats = clothingHistory.reduce((acc, item) => {
      const month = new Date(item.date).getMonth();
      if (!acc[month]) acc[month] = 0;
      acc[month]++;
      return acc;
    }, {});

    setClothingStats(stats);
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <Typography variant="h4">Einstellungen</Typography>

      <Grid container spacing={3}>
        <Grid item xs={12} sm={6}>
          <Box>
            <Typography variant="h6">Passwort ändern</Typography>
            <form onSubmit={handlePasswordChange}>
              <TextField
                label="Aktuelles Passwort"
                type="password"
                fullWidth
                margin="normal"
                value={currentPassword}
                onChange={(e) => setCurrentPassword(e.target.value)}
                required
              />
              <TextField
                label="Neues Passwort"
                type="password"
                fullWidth
                margin="normal"
                value={newPassword}
                onChange={(e) => setNewPassword(e.target.value)}
                required
              />
              {passwordError && <Typography color="error">{passwordError}</Typography>}
              <Button type="submit" variant="contained" color="primary" fullWidth>
                Passwort ändern
              </Button>
            </form>
          </Box>
        </Grid>

        <Grid item xs={12} sm={6}>
          <Box>
            <Typography variant="h6">Abmelden</Typography>
            <Button variant="outlined" color="secondary" fullWidth onClick={handleLogout}>
              Abmelden
            </Button>
          </Box>
        </Grid>

        <Grid item xs={12}>
          <Box>
            <Typography variant="h6">Statistik</Typography>
            <FormControl fullWidth margin="normal">
              <InputLabel>Monat</InputLabel>
              <Select
                value="monat" // Monat kann hier dynamisch gesetzt werden
                label="Monat"
              >
                {Array.from({ length: 12 }, (_, index) => (
                  <MenuItem key={index} value={index}>
                    {new Date(2024, index).toLocaleString('default', { month: 'long' })}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>

            <Typography variant="body1">Statistik für das gewählte Jahr/Monat:</Typography>
            {Object.keys(clothingStats).length > 0 ? (
              <div>
                {Object.keys(clothingStats).map((month) => (
                  <Typography key={month}>
                    {new Date(2024, month).toLocaleString('default', { month: 'long' })}: {clothingStats[month]} Kleidungsstücke getragen
                  </Typography>
                ))}
              </div>
            ) : (
              <Typography>Keine Daten vorhanden.</Typography>
            )}
          </Box>
        </Grid>
      </Grid>
    </div>
  );
};

export default Settings;
