import React from 'react';
import {BrowserRouter, Navigate, Route, Routes} from 'react-router-dom';
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

import {GoogleAuthProvider, signInWithPopup, signOut} from 'firebase/auth';
import {auth} from './firebase';



// Main App komponente
const AppContent = () => {
    const { user } = useAuth();

	const GoogleSignIn = async () => {
    const provider = new GoogleAuthProvider(); // Use 'GoogleAuthProvider' directly
    provider.setCustomParameters({ prompt: 'select_account' });
    try {
        await signInWithPopup(auth, provider); // Use 'provider' directly here
    } catch (error) {
        alert(error.message);
    }};

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
                        <SignIn onSignIn = {GoogleSignIn} />
                    )
                }
                />

                <Route
                    path="/Home"
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
                    path="/Settings"
                    element={user ? <Settings /> : <Navigate to="/" replace />}
                />
                <Route
                    path="/Constraints"
                    element={user ? <Constraints  /> : <Navigate to="/" replace />}
                />
                <Route
                    path="/signin"
                    element={user ? <SignIn  /> : <Navigate to="/" replace />}
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