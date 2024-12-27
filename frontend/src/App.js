import React, { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'; // React Router v6
import { ThemeProvider, CssBaseline } from '@mui/material'; // MUI v5
import theme from './theme'; // Dein benutzerdefiniertes Theme
import { AuthProvider, useAuth } from './context/AuthContext'; // AuthContext importieren

// Importiere deine Seitenkomponenten
import SignIn from './pages/SignIn';
import RegisterForm from './pages/Register';
import Layout from './components/layout/Layout';
import HomePage from './pages/Home';
import WardrobePage from './pages/Wardrobe';
import StylesPage from './pages/Styles';
import OutfitsPage from './pages/Outfits';

// Dies ist die Haupt-App-Komponente
const App = () => {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AuthProvider>
        <Router>
          <Routes>
            {/* Login-Route */}
            <Route path="/login" element={<SignIn />} />

            {/* Registrierungs-Route */}
            <Route path="/register" element={<RegisterForm />} />

            {/* Geschützte Routen für den digitalen Kleiderschrank */}
            <Route path="/" element={<ProtectedRoute><HomePage /></ProtectedRoute>} />
            <Route path="/wardrobe" element={<ProtectedRoute><WardrobePage /></ProtectedRoute>} />
            <Route path="/styles" element={<ProtectedRoute><StylesPage /></ProtectedRoute>} />
            <Route path="/outfits" element={<ProtectedRoute><OutfitsPage /></ProtectedRoute>} />
          </Routes>
        </Router>
      </AuthProvider>
    </ThemeProvider>
  );
};

// Geschützte Route, die den Benutzer nur dann zur Seite lässt, wenn er eingeloggt ist
const ProtectedRoute = ({ children }) => {
  const { isAuthenticated } = useAuth();

  if (!isAuthenticated) {
    // Wenn der Benutzer nicht authentifiziert ist, leite ihn zur Login-Seite weiter
    return <Navigate to="/login" />;
  }

  // Wenn der Benutzer authentifiziert ist, zeige die angeforderte Seite
  return children;
};

export default App;
