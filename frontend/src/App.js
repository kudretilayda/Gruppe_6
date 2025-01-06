import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { Typography, Button, CssBaseline, Grid, Container, Box, CircularProgress } from '@mui/material';
import { GoogleAuthProvider, signInWithPopup, onAuthStateChanged, signOut } from 'firebase/auth';
import { auth } from './firebase';
import { AuthProvider, useAuth } from './context/AuthContext';

import Navbar from './components/layout/Navbar';

import Home from './components/pages/Home';
import Wardrobe from './components/pages/Wardrobe';
import Outfits from './components/pages/Outfits';
import Styles from './components/pages/Styles';
import Profile from './components/pages/Profile';
import Settings from './components/pages/Settings';
import SignIn from './components/pages/SignIn';


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
        <>
            <CssBaseline />
            <Navbar user={user} onLogout={handleSignOut} />
            
            <Routes>
                <Route path="/" element={
                    user ? (
                        <Home />
                    ) : (
                        <SignIn onSignIn = {handleGoogleSignIn} />
                    )
                } />

                {/* Protected Routes */}
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