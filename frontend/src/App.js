import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import { Container, ThemeProvider, CssBaseline } from '@mui/material';
import { getAuth, onAuthStateChanged, GoogleAuthProvider, signInWithPopup } from 'firebase/auth';
import Theme from './theme'; // Dein Theme
import firebaseConfig from './firebaseconfig';
import SignIn from './components/pages/SignIn';
import Header from './components/layout/Header';
import Home from './components/pages/Home';
import Wardrobe from './components/pages/Wardrobe';
import StyleList from './components/pages/StyleList';
import OutfitPlanner from './components/pages/OutfitPlaner';
import Settings from './components/pages/Settings';
import DigitalWardrobeAPI from "./api/DigitalWardrobeAPI";
import LoadingSpinner from './components/dialogs/LoadingSpinner';
import { initializeApp } from "firebase/app"; // Firebase Initialisierung


const auth = getAuth();
const provider = new GoogleAuthProvider();


// Funktionale Komponente App
function App() {
  const [currentUser, setCurrentUser] = useState(null);
  const [authLoading, setAuthLoading] = useState(true);
  const [appError, setAppError] = useState(null);
  const [authError, setAuthError] = useState(null);

  // Funktion zur Anmeldung
  const handleSignIn = () => {
    setAuthLoading(true);
    signInWithPopup(auth, provider).then(async (result) => {
      const user = result.user;
      const token = await user.getIdToken();
      document.cookie = `token=${token};path=/;`;
      setAuthLoading(false);
      setCurrentUser(user);
      console.log("User signed in:", user);
    }).catch((error) => {
      setAuthLoading(false);
      setAuthError(error.message);
      console.error("Auth error:", error);
    });
  };

  // Überwachung des Auth-Status
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (user) => {
      console.log("Auth state changed:", user);
      if (user) {
        setAuthLoading(true);
        setCurrentUser(user);

        // API-Aufruf nur wenn der Benutzer angemeldet ist
        const api = DigitalWardrobeAPI.getAPI();
        const googleId = user.uid;

        try {
          const fetchedUser = await api.getUserByGoogleId(googleId);
          console.log("User fetched from API:", fetchedUser);

          // Wenn der Benutzer nicht existiert, erstellen wir einen neuen
          if (!fetchedUser) {
            let newUser = {
              id: 0,
              first_name: user.displayName?.split(" ")[0] || "",
              last_name: user.displayName?.split(" ")[1] || "",
              nick_name: user.displayName?.split(" ")[0] || "User",
              google_user_id: user.uid,
              household_id: null
            };
            await api.addUser(newUser); // Neuen Benutzer hinzufügen
            console.log('New user added:', newUser);
          }
        } catch (error) {
          console.error('Error fetching user:', error);
        } finally {
          setAuthLoading(false);
        }

        const token = await user.getIdToken();
        document.cookie = `token=${token};path=/;`;

      } else {
        setCurrentUser(null);
        setAuthLoading(false);
      }
    });

    return () => unsubscribe();
  }, []); // Der leere Abhängigkeits-Array sorgt dafür, dass der Effekt nur einmal ausgeführt wird

  if (authLoading) {
    return <LoadingSpinner show={authLoading} />;
  }

  return (
    <ThemeProvider theme={Theme}>
      <CssBaseline />
      <Router>
        <Container maxWidth='md'>
          <Header user={currentUser} />
          <Routes>
            <Route
              path="/"
              element={currentUser ? <Navigate to="/home" replace /> : <SignIn onSignIn={handleSignIn} />}
            />
            <Route
              path="/home"
              element={<Secured user={currentUser}><Home /></Secured>}
            />
            <Route
              path="/wardrobe"
              element={<Secured user={currentUser}><Wardrobe /></Secured>}
            />
            <Route
              path="/styles"
              element={<Secured user={currentUser}><StyleList /></Secured>}
            />
            <Route
              path="/outfits"
              element={<Secured user={currentUser}><OutfitPlanner /></Secured>}
            />
            <Route
              path="/settings"
              element={<Secured user={currentUser}><Settings /></Secured>}
            />
          </Routes>
        </Container>
      </Router>
    </ThemeProvider>
  );
}

// Hilfskomponente für gesicherte Routen
function Secured({ user, children }) {
  if (!user) {
    return <Navigate to="/" replace />;
  }
  return children;
}

export default App;
