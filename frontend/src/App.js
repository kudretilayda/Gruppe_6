import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import { Typography, Button, CssBaseline, Grid, Container } from '@mui/material';
import Register from './components/pages/Register';  // Korrigiere den Pfad
import Login from './components/pages/Login';  // Korrigiere den Pfad
import Header from './components/pages/Header';  // Korrigiere den Pfad

const App = () => {
    return (
        <BrowserRouter>
            <CssBaseline />
            <Header />
            <Routes>
                <Route path="/" element={
                    <main>
                        <Container maxWidth="sm">
                            <Typography variant="h2" align="center" color="textPrimary" gutterBottom>
                                Kleiderschrank-Projekt
                            </Typography>
                            <Typography variant="h5" align="center" color="textSecondary" paragraph>
                                Das ist eine Probe Seite für das Projekt in SOPRA im WS 24/25
                            </Typography>
                            <Grid container spacing={2} justifyContent="center">
                                <Grid item>
                                    <Button 
                                        component={Link} 
                                        to="/login" 
                                        variant="contained" 
                                        color="primary"
                                    >
                                        Sign-In
                                    </Button>
                                </Grid>
                                <Grid item>
                                    <Button 
                                        component={Link} 
                                        to="/register" 
                                        variant="outlined" 
                                        color="primary"
                                    >
                                        Sign-Up
                                    </Button>
                                </Grid>
                            </Grid>
                        </Container>
                    </main>
                } />
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
