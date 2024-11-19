import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider } from '@material-ui/core/styles';
import { theme } from './theme';
import { AuthProvider, useAuth } from './contexts/AuthContext';

// Komponenten importieren
import MainLayout from './components/layout/MainLayout';
import SignIn from './components/pages/SignIn';
import SignUp from './components/pages/SignUp';
import Dashboard from './components/pages/Dashboard';
import KleiderschrankPage from './components/pages/KleiderschrankPage';
import OutfitPage from './components/pages/OutfitPage';
import StylePage from './components/pages/StylePage';

// Protected Route Component
const ProtectedRoute = ({ children }) => {
  const { user } = useAuth();
  if (!user) {
    return <Navigate to="/signin" replace />;
  }
  return children;
};

function App() {
  return (
    <ThemeProvider theme={theme}>
      <AuthProvider>
        <Router>
          <Routes>
            {/* Public Routes */}
            <Route path="/signin" element={<SignIn />} />
            <Route path="/signup" element={<SignUp />} />

            {/* Protected Routes */}
            <Route path="/" element={
              <ProtectedRoute>
                <MainLayout>
                  <Dashboard />
                </MainLayout>
              </ProtectedRoute>
            } />
            
            <Route path="/kleiderschrank" element={
              <ProtectedRoute>
                <MainLayout>
                  <KleiderschrankPage />
                </MainLayout>
              </ProtectedRoute>
            } />

            <Route path="/outfits" element={
              <ProtectedRoute>
                <MainLayout>
                  <OutfitPage />
                </MainLayout>
              </ProtectedRoute>
            } />

            <Route path="/styles" element={
              <ProtectedRoute>
                <MainLayout>
                  <StylePage />
                </MainLayout>
              </ProtectedRoute>
            } />
          </Routes>
        </Router>
      </AuthProvider>
    </ThemeProvider>
  );
}

export default App;
