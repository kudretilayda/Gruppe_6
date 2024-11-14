import React from 'react';
import { Typography, AppBar, Card, CardActions, CardContent, CardMedia, CssBaseline, Grid2, Toolbar, Container } from '@mui/material';
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
                    </Container>
                </div>
            </main>

        </>
    )
}

export default App;