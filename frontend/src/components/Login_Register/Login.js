// Importiere die benötigten React Komponenten und Hooks
import React, {useState} from "react";
// Importiere die Material-UI Komponenten für das Design
import { TextField, Button, Container, Box } from "@mui/material";
// Importiere die Link-Komponente für Navigation
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../../AuthContext";


const Login = () => {

    const navigate = useNavigate();
    const { login } = useAuth();

   // State Variablen für User und Passwort
   const [username, setUsername] = useState(""); // Speichert die eingegebene User
   const [password, setPassword] = useState(""); // Speichert das eingegebene Passwort
   // State Variablen für Fehleranzeige
   const [usernameError, setUsernameError] = useState(false); // Zeigt Fehler bei User-Eingabe
   const [passwordError, setPasswordError] = useState(false); // Zeigt Fehler bei Passwort-Eingabe

    console.log('Auth Context Werte:', useAuth());

   // Funktion wird beim Absenden des Formulars ausgeführt
   const handleSubmit = async (event) => {
       event.preventDefault(); // Verhindert Standard-Formularverhalten
       console.log('Login-Versuch mit:', username, password);

       if (!username || !password) {
        setUsernameError(!username);
        setPasswordError(!password);
        return;
       }



       if (username === 'admin' && password === 'admin') {
        console.log('Korrekte Anmeldedaten, versuche Login...');
        try {
            await login({ username: 'admin'});
            console.log('Login erfolgreich, navigiere zur Hauptseite');
            navigate('/');
        } catch (error) {
            console.error('Login-Fehler', error);
            setUsernameError(true);
            setPasswordError(true);
        } 

       } else {
        console.log('Falsche Anmeldedaten');
        setUsernameError(true);
        setPasswordError(true);
        alert('Bitte verwenden Sie admin/admin');
       }
   };

   

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
                       onChange={(e) => setUsername(e.target.value)} // Aktualisiert User bei Änderung
                       required
                       variant="outlined"
                       color="secondary"
                       type="text"
                       sx={{ mb: 3 }}
                       fullWidth
                       value={username}
                       error={usernameError} // Zeigt Fehler an wenn UserError true ist
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