// Importiere die benötigten React Komponenten und Hooks
import React, {useState} from "react";
// Importiere die Material-UI Komponenten für das Design
import { TextField, Button, Container, Box } from "@mui/material";
// Importiere die Link-Komponente für Navigation
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../../AuthContext";


const Login = () => {

    const Navigate = useNavigate();
    const { Login } = useAuth();

   // State Variablen für User und Passwort
   const [User, setUser] = useState(""); // Speichert die eingegebene User
   const [password, setPassword] = useState(""); // Speichert das eingegebene Passwort
   // State Variablen für Fehleranzeige
   const [UserError, setUserError] = useState(false); // Zeigt Fehler bei User-Eingabe
   const [passwordError, setPasswordError] = useState(false); // Zeigt Fehler bei Passwort-Eingabe

   // Funktion wird beim Absenden des Formulars ausgeführt
   const handleSubmit = (Event) => {
       Event.preventDefault(); // Verhindert Standard-Formularverhalten

       // Setzt Fehleranzeigen zurück
       setUserError(false);
       setPasswordError(false);

       // Prüft ob User-Feld leer ist
       if (User === '') {
           setUserError(true);
       }

       // Prüft ob Passwort-Feld leer ist
       if (password === '') {
           setPasswordError(true);
       }

       // Wenn beide Felder ausgefüllt sind
       if (User === 'admin' && password === 'admin') {
            Login({ username: User });
            Navigate('frontend/src/components/pages/Home.js');
       } else {
            setUserError(true);
            setPasswordError(true);
            alert('Falsche Angaben bei der Anmeldung!!')
       }
           // Hier kann später die Authentifizierung eingebaut werden
       }
   

   return (
       // Container für zentrierte Darstellung
       <Container maxWidth="sm">
           {/* Box für Abstände oben und an den Seiten */}
           <Box sx={{ mt: 8, mx: 4 }}>
               {/* Formular mit automatischer Vervollständigung aus */}
               <form autoComplete="off" onSubmit={handleSubmit}>
                   <h2>Login Form</h2>

                   {/* User Eingabefeld */}
                   <TextField
                       label="User"
                       onChange={(e) => setUser(e.target.value)} // Aktualisiert User bei Änderung
                       required
                       variant="outlined"
                       color="secondary"
                       type="User"
                       sx={{ mb: 3 }}
                       fullWidth
                       value={User}
                       error={UserError} // Zeigt Fehler an wenn UserError true ist
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