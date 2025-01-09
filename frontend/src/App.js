import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { Typography, Button, CssBaseline, Grid,Container, Box, CircularProgress} from '@mui/material';
import { GoogleAuthProvider, signInWithPopup, onAuthStateChanged, signOut} from 'firebase/auth';
import { auth } from './firebase.js';
import { AuthProvider, useAuth } from './context/AuthContext.js';

import Navbar from './components/layout/Navbar.js';

import Home from './components/pages/Home.js';
import Wardrobe from './components/pages/Wardrobe.js';
import Outfits from './components/pages/Outfits.js';
import Styles from './components/pages/Styles.js';
import Profile from './components/pages/Profile.js';
import ClothingType from "./components/pages/ClothingType.js";
import Settings from './components/pages/Settings.js';
import SignIn from './components/pages/SignIn.js';


//init app
const AppContent = () => {
    const { user, loading } = useAuth();

    //Google SignIn
    const handleGoogleSignIn = async () => {
        const provider = new GoogleAuthProvider();
        try {
            console.log('Starting Google sign in...');
            await signInWithPopup(auth, provider);
            console.log('Sign in successful')
        }   catch (error) {
            console.error('Error singing in with Google:', error);
        }
    };

    //SignOut
    const handleSignOut = async () => {
        try {
            await signOut(auth);
        }   catch (error) {
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
        <><CssBaseline />
            <Navbar user={user} onLogout={handleSignOut} />
            
            <Routes>
                <Route path="/" element={
                    user ? (
                        <Home />
                    ) : (
                        <SignIn onSignIn = {handleGoogleSignIn} />
                    )
                }
                />

                <Route
                    path="/wardrobe" 
                    element={user ? <Wardrobe /> : <Navigate to="/" replace />} 
                />
                    <Route
                    path="/styles"
                    element={user ? <Styles /> : <Navigate to="/" replace />} 
                />
                <Route 
                    path="/outfits" 
                    element={user ? <Outfits /> : <Navigate to="/" replace />}
                />
                <Route 
                    path="/profile" 
                    element={user ? <Profile /> : <Navigate to="/" replace />}
                />
                <Route
                    path="/types"
                    element={user ? <ClothingType /> : <Navigate to="/" replace />}
                />
            </Routes>
        </>
    );
};

const App = () => {
    return (
        <BrowserRouter>
            <AuthProvider>
                <CssBaseline />
                <AppContent />
            </AuthProvider>
        </BrowserRouter>
    );
};

export default App;