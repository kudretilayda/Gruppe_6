import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate, useLocation } from 'react-router-dom';
import { Container, ThemeProvider, CssBaseline } from '@mui/material';
import { initializeApp } from 'firebase/app';
import { getAuth, signInWithPopup, GoogleAuthProvider, onAuthStateChanged } from 'firebase/auth';
import theme from './theme';
import SignIn from './pages/SignIn';
import firebaseConfig from './firebaseconfig';
import ErrorMessage from './components/shared/ErrorMessage';
import LoadingSpinner from './components/shared/LoadingSpinner';
import Header from './components/layout/Header';
import Footer from './components/layout/Footer';
import Home from './pages/Home';
import Wardrobe from './pages/Wardrobe'; // Neue Seite für den digitalen Kleiderschrank
import Outfits from './pages/Outfits';  // Outfits-Seite
import Styles from './pages/Styles';  // Styles-Seite
import Settings from './pages/Settings'; // Settings-Seite

initializeApp(firebaseConfig);
const auth = getAuth();
const provider = new GoogleAuthProvider();

const App = () => {
    const [currentUser, setCurrentUser] = useState(null);
    const [authError, setAuthError] = useState(null);
    const [authLoading, setAuthLoading] = useState(false);

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
                setAuthLoading(true);
                setCurrentUser(user);
                const token = await user.getIdToken();
                document.cookie = `token=${token};path=/;`;
                setAuthLoading(false);
            } else {
                setCurrentUser(null);
                setAuthLoading(false);
            }
        });

        return () => unsubscribe();
    }, []);

    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <Router>
                <div style={styles.app}>
                    <Header user={currentUser} />
                    <Container component="main" style={styles.main}>
                        <Routes>
                            <Route path="/" element={currentUser ? <Navigate replace to="/home" /> : <SignIn onSignIn={handleSignIn} />} />
                            <Route path="/home" element={<Secured user={currentUser}><Home /></Secured>} />
                            <Route path="/wardrobe" element={<Secured user={currentUser}><Wardrobe /></Secured>} />
                            <Route path="/outfits" element={<Secured user={currentUser}><Outfits /></Secured>} />
                            <Route path="/styles" element={<Secured user={currentUser}><Styles /></Secured>} />
                            <Route path="/settings" element={<Secured user={currentUser}><Settings /></Secured>} />
                        </Routes>
                    </Container>
                    <Footer />
                </div>
                <LoadingSpinner show={authLoading} />
                <ErrorMessage error={authError} contextErrorMsg={`Something went wrong during sign-in`} />
            </Router>
        </ThemeProvider>
    );
};

const Secured = ({ user, children }) => {
    let location = useLocation();
    if (!user) {
        return <Navigate to="/" state={{ from: location }} replace />;
    }
    return children;
};

const styles = {
  app: {
    display: 'flex',
    flexDirection: 'column',
    minHeight: '100vh',
  },
  main: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'flex-start',
  },
};

export default App;
