import React from 'react';
import { Typography, AppBar, Button, CssBaseline, Grid, Toolbar, Container } from '@mui/material';
import CheckroomIcon from '@mui/icons-material/Checkroom';
import { useNavigate } from 'react-router-dom';

const App = () => {
    const navigate = useNavigate(); // React Router Navigation Hook

    return (
        <>
            <CssBaseline />
            <AppBar position="relative">
                <Toolbar>
                    <CheckroomIcon />
                    <Typography variant="h6">Kleiderschrank-Projekt</Typography>
                </Toolbar>
            </AppBar>
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
                            <Button variant="contained" color="primary" onClick={() => navigate('/signin')}>
                                Sign-In
                            </Button>
                        </Grid>
                        <Grid item>
                            <Button variant="outlined" color="primary" onClick={() => navigate('/signup')}>
                                Sign-Up
                            </Button>
                        </Grid>
                    </Grid>
                </Container>
            </main>
        </>
    );
};

export default App;




