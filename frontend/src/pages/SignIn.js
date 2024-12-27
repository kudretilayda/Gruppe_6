import React, { useState } from "react";
import { TextField, Button, Container, Box } from "@mui/material";
import { Link, useNavigate } from "react-router-dom"; // useNavigate für Weiterleitung
import { useAuth } from "../context/AuthContext"; // Zugriff auf AuthContext

const SignIn = () => {
   const { login } = useAuth(); // Zugriff auf die login Funktion im AuthContext
   const navigate = useNavigate(); // Zum Weiterleiten nach erfolgreichem Login

   const [email, setEmail] = useState('');
   const [password, setPassword] = useState('');
   const [emailError, setEmailError] = useState(false);
   const [passwordError, setPasswordError] = useState(false);

   const handleSubmit = (event) => {
      event.preventDefault();
      setEmailError(false);
      setPasswordError(false);

      if (email === '' || password === '') {
         if (email === '') setEmailError(true);
         if (password === '') setPasswordError(true);
         return;
      }

      // Beispielhafte Anmeldung: Setzt den Authentifizierungsstatus
      login();

      // Weiterleitung zur digitalen Kleiderschrank-Seite
      navigate('/wardrobe'); // Hier wird der Benutzer zum Kleiderschrank weitergeleitet
   };

   return (
      <Container maxWidth="sm">
         <Box sx={{ mt: 8, mx: 4 }}>
            <form onSubmit={handleSubmit}>
               <h2>Login Form</h2>
               <TextField
                  label="Email"
                  type="email"
                  fullWidth
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  error={emailError}
               />
               <TextField
                  label="Password"
                  type="password"
                  fullWidth
                  required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  error={passwordError}
               />
               <Button type="submit">Login</Button>
               <Box sx={{ mt: 2 }}>
                  <small>Need an account? <Link to="/register">Register here</Link></small>
               </Box>
            </form>
         </Box>
      </Container>
   );
};

export default SignIn;
