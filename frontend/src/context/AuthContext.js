import React, { createContext, useContext, useState } from 'react';

// Erstelle den AuthContext
const AuthContext = createContext();

// AuthProvider-Komponente, die den Authentifizierungsstatus bereitstellt
export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Funktion, um den Benutzer als authentifiziert zu markieren
  const login = () => setIsAuthenticated(true);

  // Funktion, um den Benutzer abzumelden
  const logout = () => setIsAuthenticated(false);

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

// Hook, um den AuthContext zu nutzen
export const useAuth = () => useContext(AuthContext);
