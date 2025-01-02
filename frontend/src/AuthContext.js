// src/context/AuthContext.js
import React, { createContext, useContext, useEffect, useState } from 'react';
import { auth } from './firebaseconfig';
import { signInWithEmailAndPassword, onAuthStateChanged, signOut } from 'firebase/auth';

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    //Auth-Status überwachen
    useEffect(() => {
        const unsubscribe = onAuthStateChanged(auth, (user) => {
            console.log('Auth Status geändert:', user);
            setUser(user);
            setLoading(false);
        });

        //Cleanup
        return () => unsubscribe();
            
    }, []);

    const login = async (username, password) => {
        setLoading(true);
        try {
            console.log('Login-Versuch mit:', username);

            if (username === 'admin' && password === 'admin') {
                const testUser = {
                    email: 'admin@test.com',
                    displayName: 'Admin'
                };
                setUser(testUser);
                return true;
            }

            setError('Ungültige Anmeldedaten');
            return false;
        } catch (err) {
            console.error('Login-Fehler:', err);
            setError(err.message);
            return false;
        } finally {
            setLoading(false);
        }
        
    };

    const logout = async () => {
        try {
            await signOut(auth);
            setUser(null);
        } catch (err) {
            console.error('Logout-Fehler:', err)
            setError(err.message);
        }
    };

    const value = {
        user,
        login,
        logout,
        loading,
        error
    };

    if (loading) {
        return <div>Laden...</div>;
    }

    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error('useAuth muss innerhalb eines AuthProvider verwendet werden');
    }
    return context;
};

/*

// Simplified login function for demo purposes
    const Login = (username, password) => {
        setLoading(true);
        // Simulating an API call
        setTimeout(() => {
            if (username === 'admin' && password === 'admin') {
                setUser({ username: 'admin', role: 'admin' });
                setError(null);
            } else {
                setError('Invalid credentials');
            }
            setLoading(false);
        }, 1000);
    };

    */