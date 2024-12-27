// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // React Router v6
import { ThemeProvider, CssBaseline } from '@mui/material'; // Updated to Material UI v5
import theme from './theme'; // Assuming you have a custom theme defined
import { AuthProvider } from './context/AuthContext'; // If you're using context for authentication

// Import your page components
import Layout from './components/layout/Layout'; // Layout component if you have a consistent layout
import HomePage from './pages/Home';
import WardrobePage from './pages/Wardrobe';
import StylesPage from './pages/Styles';
import OutfitsPage from './pages/Outfits';

const App = () => {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AuthProvider>
        <Router>
          <Layout>
            <Routes> {/* Routes is used in React Router v6 instead of Switch */}
              <Route path="/" element={<HomePage />} />
              <Route path="/wardrobe" element={<WardrobePage />} />
              <Route path="/styles" element={<StylesPage />} />
              <Route path="/outfits" element={<OutfitsPage />} />
            </Routes>
          </Layout>
        </Router>
      </AuthProvider>
    </ThemeProvider>
  );
};

export default App;
