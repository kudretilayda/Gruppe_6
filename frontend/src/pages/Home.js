import React, { useState, useEffect } from 'react';
import { getAuth } from 'firebase/auth';
import { useNavigate } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button, Box, Container, Paper } from '@mui/material';
import LoadingSpinner from "../components/dialogs/LoadingSpinner";
import DigitalWardrobeAPI from "../api/DigitalWardrobeAPI";
/**Dient als Startseite der App */

const Home = () => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true); // Zum Anzeigen des Ladezustands
    const navigate = useNavigate()

    useEffect(() => {
        const fetchData = async () => {
            const auth = getAuth();
            const currentUser = auth.currentUser;

            if (currentUser) {
                try {
                    // Hole Benutzerdaten anhand der Google-User-ID
                    const userBO = await DigitalWardrobeAPI.getAPI().getUserByGoogleId(currentUser.uid);

                    if (userBO && userBO.length > 0) {
                        setUser(userBO[0]);
                    } else {
                        // Falls der Benutzer nicht gefunden wird, handle dies hier (z. B. Fehlerbehandlung)
                        console.error('User not found');
                    }
                } catch (error) {
                    console.error('Fehler beim Abrufen der Benutzerdaten:', error);
                }
            } else {
                console.error('Kein authentifizierter Benutzer');
            }

            setLoading(false); // Ladezustand nach der Datenabfrage
        };

        fetchData();
    }, []);

    const handleLogout = () => {
        const auth = getAuth();
            auth.signOut();
            navigate('/')
    };

    if (loading) {
        return <LoadingSpinner />;
    }

    if (!user) {
        return <div>Benutzerdaten konnten nicht geladen werden. Bitte versuche es später erneut.</div>;
    }

    return (
        <Box sx={styles.root}>
            {/* Navigation Bar */}
            <AppBar position="static" sx={styles.appBar}>
                <Toolbar>
                    <Typography variant="h6" sx={styles.title}>
                        Digital Wardrobe
                    </Typography>
                    <Box sx={styles.navButtons}>
                        <Button color="inherit" onClick={() => navigate('/home')}>HOME</Button>
                        <Button color="inherit" onClick={() => navigate('/wardrobe')}>WARDROBE</Button>
                        <Button color="inherit" onClick={() => navigate('/styles')}>STYLES</Button>
                        <Button color="inherit" onClick={() => navigate('/outfits')}>OUTFITS</Button>
                        <Button color="inherit" onClick={() => navigate('/profile')}>PROFILE</Button>
                        <Button color="inherit" onClick={handleLogout}>LOGOUT</Button>
                    </Box>
                </Toolbar>
            </AppBar>

            {/* Main Content */}
            <Container sx={styles.container}>
                <Paper elevation={3} sx={styles.welcomeCard}>
                    <Typography variant="h4" sx={styles.welcomeText}>
                        Willkommen,
                    </Typography>
                    <Typography variant="h4" sx={styles.userName}>
                        {user.nick_name} bei DigitalWardrobe!
                    </Typography>
                </Paper>

                <Box sx={styles.logoContainer}>
                    <img
                        src={`${process.env.PUBLIC_URL}/LogoIcon.png`}
                        alt="DigitalWardrobe Logo"
                        style={styles.logo}
                    />
                </Box>

                {/* Quick Access Buttons */}
                <Box sx={styles.buttonContainer}>
                    <Button
                        variant="contained"
                        onClick={() => navigate('/wardrobe')}
                        sx={styles.actionButton}
                    >
                        Wardrobe verwalten
                    </Button>
                    <Button
                        variant="contained"
                        onClick={() => navigate('/outfits')}
                        sx={styles.actionButton}
                    >
                        Outfits erstellen
                    </Button>
                </Box>
            </Container>

            {/* Footer */}
            <Box sx={styles.footer}>
                <Typography variant="body2" color="textSecondary">
                    © 2024 DigitalWardrobe, Inc. all rights reserved.
                </Typography>
                <Button color="inherit" size="small" onClick={() => navigate('/about')}>
                    About
                </Button>
            </Box>
        </Box>
    );
};

const styles = {
    root: {
        minHeight: '100vh',
        display: 'flex',
        flexDirection: 'column',
        bgcolor: '#f5f5f5',
    },
    appBar: {
        backgroundColor: '#4285f4',
    },
    title: {
        flexGrow: 1,
        fontWeight: 'bold',
    },
    navButtons: {
        display: 'flex',
        gap: 2,
    },
    container: {
        flex: 1,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        padding: '2rem',
        gap: 4,
    },
    welcomeCard: {
        padding: '2rem',
        textAlign: 'center',
        width: '100%',
        maxWidth: 600,
        marginTop: 2,
    },
    welcomeText: {
        color: '#001b33',
        marginBottom: 1,
    },
    userName: {
        color: '#4285f4',
        fontWeight: 'bold',
    },
    logoContainer: {
        display: 'flex',
        justifyContent: 'center',
        width: '100%',
        margin: '2rem 0',
    },
    logo: {
        width: '50%',
        maxWidth: '350px',
        height: 'auto',
        borderRadius: '50%',
        opacity: 0.5,
    },
    buttonContainer: {
        display: 'flex',
        gap: 2,
        justifyContent: 'center',
        width: '100%',
        maxWidth: 600,
    },
    actionButton: {
        backgroundColor: '#4285f4',
        '&:hover': {
            backgroundColor: '#3367d6',
        },
        padding: '0.75rem 1.5rem',
    },
    footer: {
        padding: '1rem',
        textAlign: 'center',
        backgroundColor: '#fff',
        borderTop: '1px solid #e0e0e0',
    },
};

export default Home;