import React, { useState } from 'react';
import {
  Container,
  Paper,
  TextField,
  Button,
  Typography,
  Link,
  Box,
  CircularProgress
} from '@material-ui/core';
import { useNavigate } from 'react-router-dom';
import { getAuth, signInWithEmailAndPassword, GoogleAuthProvider, signInWithPopup } from 'firebase/auth';

export default function SignIn() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const auth = getAuth();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const userCredential = await signInWithEmailAndPassword(auth, email, password);
      const user = userCredential.user;
      // API Call zum Backend, um den User zu verifizieren/erstellen
      const response = await fetch('http://localhost:5000/api/auth/verify', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          google_id: user.uid,
          email: user.email
        })
      });

      if (response.ok) {
        navigate('/dashboard');
      }
    } catch (error) {
      setError('Anmeldung fehlgeschlagen: ' + error.message);
    } finally {
      setLoading(false);
    }
  };

  const handleGoogleLogin = async () => {
    const provider = new GoogleAuthProvider();
    try {
      const result = await signInWithPopup(auth, provider);
      const user = result.user;
      // API Call zum Backend analog zu oben
      navigate('/dashboard');
    } catch (error) {
      setError('Google-Anmeldung fehlgeschlagen: ' + error.message);
    }
  };

  return (
    <Container component="main" maxWidth="xs">
      <Box
        sx={{
          marginTop: 8,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        <Paper elevation={3} style={{ padding: '20px', width: '100%' }}>
          <Typography component="h1" variant="h5" align="center">
            Anmelden
          </Typography>
          
          {error && (
            <Typography color="error" align="center">
              {error}
            </Typography>
          )}

          <form onSubmit={handleSubmit}>
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="email"
              label="E-Mail Adresse"
              name="email"
              autoComplete="email"
              autoFocus
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              name="password"
              label="Passwort"
              type="password"
              id="password"
              autoComplete="current-password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              style={{ marginTop: '16px' }}
              disabled={loading}
            >
              {loading ? <CircularProgress size={24} /> : 'Anmelden'}
            </Button>
            <Button
              fullWidth
              variant="outlined"
              color="primary"
              onClick={handleGoogleLogin}
              style={{ marginTop: '8px' }}
              disabled={loading}
            >
              Mit Google anmelden
            </Button>
          </form>
          
          <Box mt={2}>
            <Link href="/signup" variant="body2">
              {"Noch kein Konto? Registrieren"}
            </Link>
          </Box>
        </Paper>
      </Box>
    </Container>
  );
}








