import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div>
      <h1>Willkommen zu deinem digitalen Kleiderschrank</h1>
      <p>Verwalte deine Kleidung, Styles und Outfits einfach und effizient.</p>
      <nav>
        <ul>
          <li><Link to="/wardrobe">Kleiderschrank</Link></li>
          <li><Link to="/styles">Styles</Link></li>
          <li><Link to="/outfits">Outfits</Link></li>
        </ul>
      </nav>
    </div>
  );
};

export default Home;

/*
import React, { useState, useEffect } from 'react';
import { getAuth } from 'firebase/auth';
import { Container, Typography, Box, CircularProgress } from '@mui/material';
import DigitalWardrobeAPI from '../../api/DigitalWardrobeAPI.js';
// Dient als Startseite der App


const Home = () => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        //User Data fetch von unserer API
        const fetchData = async () => {
            try {
                const auth = getAuth();
                const currentUser = auth.currentUser;

                if (currentUser) {


                    const userBO = await DigitalWardrobeAPI.getAPI().getUserByGoogleId(currentUser.uid);

                    if (userBO && userBO[0]) {
                        setUser(userBO[0]);
                    } else {
                        setError('User data not found');
                    }
                } else {
                    setError('No authenticated user found');
                }
            } catch (err) {
                setError('Error fetching user data: ' + err.message);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    //Spinner für Daten fetch
    if (loading) {
        return (
            <Box display='flex' justifyContent='center' alignItems='center' minHeight='80vh'>
                <CircularProgress />
            </Box>
        );
    }

    //Err msg wenn was schief läuft
    if (error) {
        return (
            <Container maxWidth='sm'>
                <Typography color='error' align='center' variant='h6'>
                    {error}
                </Typography>
            </Container>
        );
    }

    // Main content wenn alles geladen hat
    return (
        <Container maxWidth="lg">
            <Box sx={{
                textAlign: 'center',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                minHeight: '80vh',
                pt: 4
            }}>
                <Typography 
                    variant="h3" 
                    component="h1" 
                    gutterBottom 
                    sx={{ color: '#001b33' }}
                >
                    Willkommen, <br /> {user?.nickname} bei Digital Wardrobe!
                </Typography>
                
                <Box sx={{
                    display: 'flex',
                    justifyContent: 'center',
                    alignItems: 'center',
                    flex: 1,
                    width: '100%'
                }}>
                    <Box
                        component="img"
                        src={`${process.env.PUBLIC_URL}/LogoIcon.png`}
                        alt="Digital Wardrobe Logo"
                        sx={{
                            width: {
                                xs: '80vw',
                                sm: '50vw'
                            },
                            maxWidth: '350px',
                            height: 'auto',
                            borderRadius: '50%',
                            opacity: 0.5
                        }}
                    />
                </Box>
            </Box>
        </Container>
    );
};

export default Home;*/