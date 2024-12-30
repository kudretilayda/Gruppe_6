// src/context/AuthContext.js
import React, { createContext, useContext, useState } from 'react';
import Login from './components/Login_Register/Login';

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    // Simplified login function for demo purposes
    const login = (username, password) => {
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

    const logout = () => {
        setUser(null);
    };

    return (
        <AuthContext.Provider value={{ user, Login, logout, loading, error }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => useContext(AuthContext);