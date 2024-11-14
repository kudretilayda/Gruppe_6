import React from 'react';
import { Typography, AppBar, Button, Card, CardActions, CardContent, CardMedia, CssBaseline, Grid, Toolbar, Container } from '@mui/material';
import CheckroomIcon from '@mui/icons-material/Checkroom';

const App = () => {
    return (
        <>
            <CssBaseline />
            <AppBar position = "relative">
                <Toolbar>
                    <CheckroomIcon />
                    <Typography variant = "h6">
                        Kleiderschrank-Projekt
                    </Typography>
                </Toolbar>
            </AppBar>
            <main>
                <div>
                    <Container maxWidth = "sm">
                        <Typography variant='h2' align='center' color='textPrimary' gutterBottom>
                            Kleiderschrank-Projekt
                        </Typography>
                        <Typography variant='h5' align='center' color='textSecondary' paragraph>
                            Das ist eine Probe Seite für das Projekt in SOPRA im WS 24/25
                        </Typography>
                        <div>
                            <Grid container spacing = {2} justifyContent = "center">
                                <Grid item>
                                    <Button variant="contained" color='primary'>
                                        Sign-In
                                    </Button>
                                </Grid>
                                <Grid item>
                                    <Button variant="outlined" color='primary'>
                                        Sign-Up
                                    </Button>
                                </Grid>
                            </Grid>
                        </div>
                    </Container>
                </div>
            </main>

        </>
    )
}

export default App;