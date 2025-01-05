import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate, useLocation } from 'react-router-dom';
import { Container, ThemeProvider, CssBaseline } from "@mui/material";
import { onAuthStateChanged, GoogleAuthProvider, signInWithPopup } from "firebase/auth";
import theme from './theme';
import Navbar from "./components/layout/Navbar";
import Footer from "./components/layout/Footer";
import LoadingSpinner from "./components/dialogs/LoadingSpinner";
import ErrorMessage from "./components/dialogs/ErrorMessage";
import DigitalWardrobeAPI from "./api/DigitalWardrobeAPI";

// Seiten importieren
import SignIn from "./pages/SignIn";
import Home from './pages/Home';
import Wardrobe from './pages/Wardrobe';
import Outfits from './pages/Outfits';
import Styles from './pages/Styles';
import Settings from './pages/Settings';
import Profile from "./pages/Profile";

// Importiere die notwendige Firebase-Funktion
import { initializeApp } from 'firebase/app';
import firebaseConfig from './firebaseConfig'; // Deine Konfiguration importieren

// Initialisiere Firebase mit deiner Konfiguration
const app = initializeApp(firebaseConfig);

// Optional: Firebase-Dienste wie Auth und Firestore können hinzugefügt werden
// Beispiel für Firebase Auth:
import { getAuth } from 'firebase/auth';
const auth = getAuth(app);

// Beispiel für Firestore:
import { getFirestore } from 'firebase/firestore';
const firestore = getFirestore(app);

const App = () => {
    const [currentUser, setCurrentUser] = useState(null);
    const [authLoading, setAuthLoading] = useState(false);
    const [authError, setAuthError] = useState(null);

    const handleSignIn = () => {
        setAuthLoading(true);
        signInWithPopup(auth, provider).then(async (result) => {
            const user = result.user;
            const token = await user.getIdToken();
            document.cookie = `token=${token};path=/;`;
            setAuthLoading(false);
            setCurrentUser(user);
        }).catch((error) => {
            setAuthLoading(false);
            setAuthError(error.message);
        });
    };

    useEffect(() => {
        const unsubscribe = onAuthStateChanged(auth, async (user) => {
            if (user) {
                const token = await user.getIdToken();
                document.cookie = `token=${token};path=/;`;
                setCurrentUser(user);
            } else {
                setCurrentUser(null);
            }
        });
        return () => unsubscribe();
    }, []);

    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <Router>
                <Navbar user={currentUser} onSignOut={() => auth.signOut()} />
                <Container component="main" style={styles.main}>
                    <Routes>
                        <Route path="/" element={currentUser ? <Navigate to="/home" /> : <SignIn onSignIn={handleSignIn} />} />
                        <Route path="/home" element={<Secured user={currentUser}><Home /></Secured>} />
                        <Route path="/wardrobe" element={<Secured user={currentUser}><Wardrobe /></Secured>} />
                        <Route path="/outfits" element={<Secured user={currentUser}><Outfits /></Secured>} />
                        <Route path="/styles" element={<Secured user={currentUser}><Styles /></Secured>} />
                        <Route path="/settings" element={<Secured user={currentUser}><Settings /></Secured>} />
                        <Route path="/profile" element={<Secured user={currentUser}><Profile /></Secured>} />
                    </Routes>
                </Container>
                <Footer />
                <LoadingSpinner show={authLoading} />
                <ErrorMessage error={authError} contextErrorMsg={`Login fehlgeschlagen. Bitte versuchen Sie es erneut.`} onReload={handleSignIn} />
            </Router>
        </ThemeProvider>
    );
};

const Secured = ({ user, children }) => {
    const location = useLocation();
    if (!user) {
        return <Navigate to="/" state={{ from: location }} replace />;
    }
    return children;
};

const styles = {
    main: {
        marginTop: '64px',
        flex: 1,
    },
};

export default App;
