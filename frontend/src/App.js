// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // React Router v6
import { ThemeProvider, CssBaseline } from '@mui/material'; // Updated to Material UI v5
import theme from './theme'; // Assuming you have a custom theme defined
import { AuthProvider } from './context/AuthContext'; // If you're using context for authentication


// Import your page components
import Layout from './components/layout/Layout'; // Layout component if you have a consistent layout
import Home from './pages/Home';
import Wardrobe from './pages/Wardrobe';
import Styles from './pages/Styles';
import Outfits from './pages/Outfits';

const App = () => {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AuthProvider>
        <Router>
          <Layout>
            <Routes> {/* Routes is used in React Router v6 instead of Switch */}
              <Route path="/" element={<Home />} />
              <Route path="/wardrobe" element={<Wardrobe />} />
              <Route path="/styles" element={<Styles />} />
              <Route path="/outfits" element={<Outfits />} />
            </Routes>
          </Layout>
        </Router>
      </AuthProvider>
    </ThemeProvider>
  );
};

export default App;
