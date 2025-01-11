import React, { createContext, useState, useContext } from 'react';
import { getAuth, signInWithPopup, GoogleAuthProvider } from 'firebase/auth';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);

    const signInWithGoogle = async () => {
        const auth = getAuth();
        const provider = new GoogleAuthProvider();
        
        try {
            const result = await signInWithPopup(auth, provider);
            setUser(result.user);
        } catch (error) {
            console.error('Sign in error:', error);
        }
    };

    const signOut = async () => {
        const auth = getAuth();
        try {
            await auth.signOut();
            setUser(null);
        } catch (error) {
            console.error('Sign out error:', error);
        }
    };

    return (
        <AuthContext.Provider value={{ user, signInWithGoogle, signOut }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => useContext(AuthContext);



/*
import React, { createContext, useState, useContext, useEffect } from 'react';
import { auth } from '../firebase.js';
import { onAuthStateChanged } from 'firebase/auth';

//erstellt context mit standard wert
const AuthContext = createContext({
  user: null,
  login: () => {},
  logout: () => {}
});

export const AuthProvider = ({ children }) => {
  //Authetifizierter User Status tracker
  const [user, setUser] = useState(null);
  //Checken wir immernoch den Authentifizierungs Status?
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    //schaut auf auth state änderungen
    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
      //updatet den user status wenn auth status sich ändert
      setUser(currentUser);
      //fertig mit laden
      setLoading(false);
    });

    //bereinigt useEffect wenn komponente nicht mehr läuft
    return () => unsubscribe();
  }, []);


  const login = (userData) => {
    setUser(userData);
  };

  const logout = () => {
    setUser(null);
  };

  if (loading) {
    return null;
  }

  //übergibt auth context an die komponenten die hiervon erben ('children')
  return (
    <AuthContext.Provider value={{ user, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

*/