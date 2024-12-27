import React, { useState } from 'react';
import { TextField, Button, Container, Stack, Box } from '@mui/material';
import { Link, useNavigate } from 'react-router-dom';

const RegisterForm = () => {
   const [firstName, setFirstName] = useState('');
   const [lastName, setLastName] = useState('');
   const [email, setEmail] = useState('');
   const [password, setPassword] = useState('');
   const navigate = useNavigate(); // Navigation nach Registrierung

   const handleSubmit = (event) => {
      event.preventDefault();
      // Hier würdest du die Registrierung durchführen
      console.log(firstName, lastName, email, password);

      // Weiterleitung nach erfolgreicher Registrierung zur Login-Seite
      navigate('/login');
   };

   return (
      <Container maxWidth="sm">
         <Box sx={{ mt: 8, mx: 4 }}>
            <h2>Register Form</h2>
            <form onSubmit={handleSubmit}>
               <TextField
                  label="First Name"
                  fullWidth
                  required
                  value={firstName}
                  onChange={(e) => setFirstName(e.target.value)}
               />
               <TextField
                  label="Last Name"
                  fullWidth
                  required
                  value={lastName}
                  onChange={(e) => setLastName(e.target.value)}
               />
               <TextField
                  label="Email"
                  fullWidth
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
               />
               <TextField
                  label="Password"
                  type="password"
                  fullWidth
                  required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
               />
               <Button type="submit">Register</Button>
               <Box sx={{ mt: 2 }}>
                  <small>Already have an account? <Link to="/login">Login here</Link></small>
               </Box>
            </form>
         </Box>
      </Container>
   );
};

export default RegisterForm;
