import React, { useState } from 'react';
import { Button, TextField, Container, Typography } from '@mui/material';

const SignIn = ({ onSignIn }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    // Simuliere erfolgreiche Anmeldung
    onSignIn({ name: email.split('@')[0] }); // Nur zur Demonstration (Name basierend auf der E-Mail)
  };

  return (
    <Container maxWidth="xs">
      <Typography variant="h5" gutterBottom align="center">
        Sign-In
      </Typography>
      <form onSubmit={handleSubmit}>
        <TextField
          label="E-Mail"
          type="email"
          fullWidth
          margin="normal"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <TextField
          label="Password"
          type="password"
          fullWidth
          margin="normal"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <Button type="submit" variant="contained" color="primary" fullWidth>
          Sign-In
        </Button>
      </form>
    </Container>
  );
};

export default SignIn;





