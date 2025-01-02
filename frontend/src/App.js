// src/App.js
import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { ThemeProvider, CssBaseline } from '@mui/material';
import { AuthProvider } from './AuthContext';
import ProtectedRoute from './components/ProtectedRoutes';
import Login from './components/Login_Register/Login';
import Register from './components/Login_Register/Register';
import Layout from './components/layout/Layout';
import Home from './components/pages/Home';
import Wardrobe from './components/pages/Wardrobe';
import Styles from './components/pages/Styles';
import Outfits from './components/pages/Outfits';
import Settings from './components/pages/Settings';
import theme from './theme';
import './firebaseconfig';

const App = () => {
    return (
        <AuthProvider>
            <ThemeProvider theme={theme}>
                <CssBaseline />
                <BrowserRouter>
                    <Routes>
                        {/* Public routes */}
                        <Route path="/login" element={<Login />} />
                        <Route path="/register" element={<Register />} />
                        <Route path="/" element={
                            <ProtectedRoute>
                                <Layout>
                                    <Routes>
                                        <Route path="/" element={<Home />} />
                                        <Route path="/Wardrobe" element={<Wardrobe />} />
                                        <Route path="/Styles" element={<Styles />} />
                                        <Route path="/Outfits" element={<Outfits />} />
                                        <Route path="/Settings" element={<Settings />} />
                                    </Routes>
                                </Layout>
                            </ProtectedRoute>
                        } />
                        
                    </Routes>
                </BrowserRouter>
            </ThemeProvider>
        </AuthProvider>
    );
};

export default App;



//To-Do's:
// - Login to Homepage Connect mit Admin Cred erstellen
//      - AuthContext.js überprüfen
//      - Login.js überprüfen
//      - App.js überprüfen und zum laufen bekommen