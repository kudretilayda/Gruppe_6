import React, {createContext, useContext, useEffect, useState} from 'react';
import {BrowserRouter, Navigate, Route, Routes, useLocation, useNavigate} from 'react-router-dom';
import {CssBaseline} from '@mui/material';
import {AuthProvider, useAuth} from './context/AuthContext';

import Navbar from './components/layout/Navbar';
import Home from './components/pages/Home.js';
import Profile from './components/pages/Profile';
import Wardrobe from './components/pages/Wardrobe';
import Outfits from './components/pages/Outfits';
import Styles from './components/pages/Styles';
import SignIn from './components/pages/SignIn';
import Settings from './components/pages/Settings';
import Constraints from './components/pages/Constraints';

import {GoogleAuthProvider, onAuthStateChanged, signInWithPopup, getAuth, signInWithRedirect, signOut} from 'firebase/auth';
import {auth} from './firebase';

// Main App komponente
const AppContent = () => {
    const { user } = useAuth();

    const GoogleSignIn = async () => {
        const provider = new GoogleAuthProvider();
        provider.setCustomParameters({ prompt: 'select_account' });
        try {
            await signInWithPopup(auth, provider); // Popup statt Redirect
        } catch (error) {
            console.error('Error during Google Sign-In:', error.message);
        }
    };

    const location = useLocation();
    const navigate = useNavigate();

    const handleSignIn = async () => {
        try {
            await signInWithPopup(auth, new GoogleAuthProvider());
            const from = location.state?.from || "/home";
            navigate(from);
        } catch (error) {
            console.error("Error during sign-in:", error.message);
        }
    };


    const SignOut = async () => {
        try {
            await signOut(auth);
        }   catch (error) {
            console.error('Error signing out:', error);
        }
    };

    return (
        <><CssBaseline />
            <Navbar user={user} onLogout={SignOut} />

            <Routes>
                <Route path="/"  element={
                    user ? (
                        <Home />
                    ) : (
                        <SignIn onSignIn = {handleSignIn} />
                    )
                }
                />

                <Route
                    path="/home"
                    element={user ? <Home /> : <Navigate to="/" replace/>}
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
                    path="/settings"
                    element={user ? <Profile /> : <Navigate to="/" replace />}
                />

                <Route
                    path="/constraints"
                    element={user ? <Profile /> : <Navigate to="/" replace />}
                />

                <Route
                    path="/profile"
                    element={user ? (<Profile />) : (<Navigate to="/" state={{ from: "/profile" }} replace />)}
                />

            </Routes>
        </>
    );
};

const App = () => {
    return (
        <BrowserRouter>
            <AuthProvider>
                <CssBaseline/>
                <AppContent/>
            </AuthProvider>
        </BrowserRouter>
    );
};

export default App;
/*
import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { CssBaseline } from '@mui/material';
import { GoogleAuthProvider, signInWithPopup, onAuthStateChanged, signOut } from 'firebase/auth';
import { auth } from './firebase'
import { AuthProvider, useAuth } from './context/AuthContext';

// imports
import Navbar from './components/layout/Navbar';
import Home from './components/pages/Home';
import Profile from './components/pages/Profile';
import Wardrobe from './components/pages/Wardrobe';
import Outfits from './components/pages/Outfits';
import Styles from './components/pages/Styles';
import SignIn from './components/pages/SignIn';

// geschützte route um auth zu checken


// Main App komponente
const App = () => {
  return (
    <BrowserRouter>
      <AuthProvider>
        <CssBaseline />
        <Navbar />
        <Routes>
          {/* öffentliche route - sign in }
          <Route path="/" element={<SignIn />} />

          {/* geschützte routen - einsehbar wenn man angemeldet ist }
          <Route path="/home" element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          } />
          <Route path="/profile" element={
            <ProtectedRoute>
              <Profile />
            </ProtectedRoute>
          } />
          <Route path="/wardrobe" element={
            <ProtectedRoute>
              <Wardrobe />
            </ProtectedRoute>
          } />
          <Route path="/outfits" element={
            <ProtectedRoute>
              <Outfits />
            </ProtectedRoute>
          } />
          <Route path="/styles" element={
            <ProtectedRoute>
              <Styles />
            </ProtectedRoute>
          } />
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
};

export default App;

/*
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
    const { user, setUser, loading } = useAuth();

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
*/