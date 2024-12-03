
import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import { Typography, AppBar, Button, CssBaseline, Grid, Toolbar, Container } from '@mui/material';
import CheckroomIcon from '@mui/icons-material/Checkroom';
import Register from '../src/components/Login_Register/Register';
import Login from '../src/components/Login_Register/Login';
import Header from './components/Header';

const App = () => {
    return (
        <BrowserRouter>
            <CssBaseline />
            <Header />
            <Routes>
                <Route path="/" element={
                    <main>
                        <div>
                            <Container maxWidth="sm">
                                <Typography variant='h2' align='center' color='textPrimary' gutterBottom>
                                    Kleiderschrank-Projekt
                                </Typography>
                                <Typography variant='h5' align='center' color='textSecondary' paragraph>
                                    Das ist eine Probe Seite für das Projekt in SOPRA im WS 24/25
                                </Typography>
                                <div>
                                    <Grid container spacing={2} justifyContent="center">
                                        <Grid item>
                                            <Button 
                                                component={Link} 
                                                to="/login" 
                                                variant="contained" 
                                                color='primary'
                                            >
                                                Sign-In
                                            </Button>
                                        </Grid>
                                        <Grid item>
                                            <Button 
                                                component={Link} 
                                                to="/register" 
                                                variant="outlined" 
                                                color='primary'
                                            >
                                                Sign-Up
                                            </Button>
                                        </Grid>
                                    </Grid>
                                </div>
                            </Container>
                        </div>
                    </main>
                } />
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;


