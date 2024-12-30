// Importiere die benötigten React Komponenten und Hooks
import React, {useState} from "react";
// Importiere die Material-UI Komponenten für das Design
import { TextField, FormControl, Button, Container, Box } from "@mui/material";
// Importiere die Link-Komponente für Navigation
import { Link } from "react-router-dom";


const Login = () => {
   // State Variablen für Email und Passwort
   const [email, setEmail] = useState(""); // Speichert die eingegebene Email
   const [password, setPassword] = useState(""); // Speichert das eingegebene Passwort
   // State Variablen für Fehleranzeige
   const [emailError, setEmailError] = useState(false); // Zeigt Fehler bei Email-Eingabe
   const [passwordError, setPasswordError] = useState(false); // Zeigt Fehler bei Passwort-Eingabe

   // Funktion wird beim Absenden des Formulars ausgeführt
   const handleSubmit = (Event) => {
       Event.preventDefault(); // Verhindert Standard-Formularverhalten

       // Setzt Fehleranzeigen zurück
       setEmailError(false);
       setPasswordError(false);

       // Prüft ob Email-Feld leer ist
       if (email === '') {
           setEmailError(true);
       }

       // Prüft ob Passwort-Feld leer ist
       if (password === '') {
           setPasswordError(true);
       }

       // Wenn beide Felder ausgefüllt sind
       if (email && password) {
           console.log("Email:", email, "Password:", password)
           // Hier kann später die Authentifizierung eingebaut werden
       }
   }

   return (
       // Container für zentrierte Darstellung
       <Container maxWidth="sm">
           {/* Box für Abstände oben und an den Seiten */}
           <Box sx={{ mt: 8, mx: 4 }}>
               {/* Formular mit automatischer Vervollständigung aus */}
               <form autoComplete="off" onSubmit={handleSubmit}>
                   <h2>Login Form</h2>

                   {/* Email Eingabefeld */}
                   <TextField
                       label="Email"
                       onChange={(e) => setEmail(e.target.value)} // Aktualisiert Email bei Änderung
                       required
                       variant="outlined"
                       color="secondary"
                       type="email"
                       sx={{ mb: 3 }}
                       fullWidth
                       value={email}
                       error={emailError} // Zeigt Fehler an wenn emailError true ist
                   />

                   {/* Passwort Eingabefeld */}
                   <TextField
                       label="Password"
                       onChange={(e) => setPassword(e.target.value)} // Aktualisiert Passwort bei Änderung
                       required
                       variant="outlined"
                       color="secondary"
                       type="password"
                       value={password}
                       error={passwordError} // Zeigt Fehler an wenn passwordError true ist
                       fullWidth
                       sx={{ mb: 3}}
                   />

                   {/* Login Button */}
                   <Button variant="outlined" color="secondary" type="submit">
                       Login
                   </Button>
                   
                   {/* Link zur Registrierung mit Abstand nach oben */}
                   <Box sx={{ mt: 2 }}>
                       <small>Need an account? <Link to="/register"> Register here </Link></small>
                   </Box>
               </form>
           </Box>
       </Container>
   );
};

// Exportiert die Login Komponente für die Verwendung in anderen Dateien
export default Login;