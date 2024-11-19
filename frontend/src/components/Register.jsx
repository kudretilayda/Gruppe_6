// Importiere die benötigten React Komponenten und Hooks
import React, { useState } from 'react';
// Importiere die Material-UI Komponenten für das Design
import { TextField, Button, Container, Stack, Box } from '@mui/material';
// Importiere die React Router Komponenten für die Navigation
import { Form, Link } from 'react-router-dom';


const RegisterForm = () => {
   // Erstelle State Variablen für die Formulardaten
   const [firstName, setFirstName] = useState(''); // Speichert den Vornamen
   const [lastName, setLastName] = useState('');   // Speichert den Nachnamen
   const [email, setEmail] = useState('');         // Speichert die Email
   const [dateOfBirth, setDateOfBirth] = useState(''); // Speichert das Geburtsdatum
   const [password, setPassword] = useState('');    // Speichert das Passwort

   // Funktion die beim Absenden des Formulars ausgeführt wird
   function handleSubmit(event) {
       event.preventDefault(); // Verhindert das normale Formular-Verhalten
       console.log(firstName, lastName, email, dateOfBirth, password); // Gibt die Formulardaten in der Konsole aus
   }

   return (
       // Container für zentrierte Darstellung mit maximaler Breite
       <Container maxWidth="sm">
           {/* Box für Abstände oben und an den Seiten */}
           <Box sx={{ mt: 8, mx: 4 }}>
               <h2>Register Form</h2>
               {/* Formular mit Submit-Handler und Link zur Login-Seite */}
               <form onSubmit={handleSubmit} action={<Link to='/login' />}>
                   {/* Stack für horizontale Anordnung von Vor- und Nachname */}
                   <Stack spacing={2} direction='row' sx={{marginBottom: 4}}>
                       {/* Textfeld für Vorname */}
                       <TextField
                           type='text'
                           variant='outlined'
                           color='secondary'
                           label='First Name'
                           onChange={e => setFirstName(e.target.value)} // Aktualisiert den Vornamen bei Änderung
                           value={firstName}
                           fullWidth
                           required
                       />
                       {/* Textfeld für Nachname */}
                       <TextField
                           type='text'
                           variant='outlined'
                           color='secondary'
                           label="Last Name"
                           onChange={e => setLastName(e.target.value)} // Aktualisiert den Nachnamen bei Änderung
                           value={firstName}
                           fullWidth
                           required
                       />
                   </Stack>

                   {/* Textfeld für Email */}
                   <TextField
                       type='email'
                       variant='outlined'
                       color='secondary'
                       label="Email"
                       onChange={e => setEmail(e.target.value)} // Aktualisiert die Email bei Änderung
                       value={email}
                       fullWidth
                       required
                       sx={{mb: 4}}
                   />

                   {/* Textfeld für Passwort */}
                   <TextField
                       type='password'
                       variant='outlined'
                       color='secondary'
                       label='Password'
                       onChange={e => setPassword(e.target.value)} // Aktualisiert das Passwort bei Änderung
                       value={password}
                       required
                       fullWidth
                       sx={{mb: 4}}
                   />

                   {/* Textfeld für Geburtsdatum */}
                   <TextField
                       type='date'
                       variant='outlined'
                       color='secondary'
                       label="Date of Birth"
                       onChange={e => setDateOfBirth(e.target.value)} // Aktualisiert das Geburtsdatum bei Änderung
                       value={dateOfBirth}
                       fullWidth
                       required
                       sx={{mb: 4}}
                   />
                   {/* Register Button */}
                   <Button variant='outlined' color='secondary' type='submit'>Register</Button>
                   
                   {/* Link zur Login-Seite mit Abstand nach oben */}
                   <Box sx={{ mt: 2 }}>
                       <small>Already have an account? <Link to='/login'>Login Here</Link></small>
                   </Box>
               </form>
           </Box>
       </Container>
   );
}

// Exportiert die RegisterForm Komponente für die Verwendung in anderen Dateien
export default RegisterForm;