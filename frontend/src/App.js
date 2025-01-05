import React, { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { Typography, Button, CssBaseline, Grid, Container, Box, CircularProgress } from '@mui/material';
import { GoogleAuthProvider, signInWithPopup, onAuthStateChanged, signOut } from 'firebase/auth';
import { auth } from './firebase';
import GoogleIcon from '@mui/icons-material/Google';
import Navbar from './components/layout/Navbar';
import Home from './pages/Home';


//init app
const App = () => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
            setUser(currentUser);
            setLoading(false);
        });

        return () => unsubscribe();
    }, []);

    const handleGoogleSignIn = async () => {
        const provider = new GoogleAuthProvider();
        try {
            await signInWithPopup(auth, provider);
        } catch (error) {
            console.error('Error signing in with Google:', error);
        }
    };

    const handleSignOut = async () => {
        try {
            await signOut(auth);
        } catch (error) {
            console.error('Error signing out:', error);
        }
    };

    if (loading) {
        return (
            <Box display="flex" justifyContent="center" alignItems="center" minHeight="100vh">
                <CircularProgress />
            </Box>
        );
    }

    return (
        <BrowserRouter>
            <CssBaseline />
            <Navbar user={user} onLogout={handleSignOut} />
            
            <Routes>
                <Route path="/" element={
                    user ? (
                        <Home />
                    ) : (
                        <Container maxWidth="sm">
                            <Box sx={{ mt: 8, textAlign: 'center' }}>
                                <Typography variant='h2' gutterBottom>
                                    Digital Wardrobe
                                </Typography>
                                <Typography variant='h5' color="text.secondary" paragraph>
                                    Manage your wardrobe smartly and create stunning outfits
                                </Typography>
                                <Button 
                                    variant="contained" 
                                    color="primary"
                                    onClick={handleGoogleSignIn}
                                    startIcon={<GoogleIcon />}
                                    size="large"
                                    sx={{ mt: 2 }}
                                >
                                    Sign in with Google
                                </Button>
                            </Box>
                        </Container>
                    )
                } />

                {/* Protected Routes */}
                <Route 
                    path="/wardrobe" 
                    element={user ? <div>Wardrobe Page</div> : <Navigate to="/" replace />} 
                />
                <Route 
                    path="/styles" 
                    element={user ? <div>Styles Page</div> : <Navigate to="/" replace />} 
                />
                <Route 
                    path="/outfits" 
                    element={user ? <div>Outfits Page</div> : <Navigate to="/" replace />} 
                />
                <Route 
                    path="/profile" 
                    element={user ? <div>Profile Page</div> : <Navigate to="/" replace />} 
                />
            </Routes>
        </BrowserRouter>
    );


}

export default App;