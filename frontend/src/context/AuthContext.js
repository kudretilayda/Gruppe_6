import React, { createContext, useState, useContext } from 'react';
import { getAuth, signInWithPopup, GoogleAuthProvider } from 'firebase/auth';
import DigitalWardrobeAPI from '../api/DigitalWardrobeAPI';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const signInWithGoogle = async () => {
        setLoading(true);
        setError(null);
        
        try {
            const auth = getAuth();
            const provider = new GoogleAuthProvider();
            
            // First get Firebase authentication
            const result = await signInWithPopup(auth, provider);
            
            if (result.user) {
                try {
                    // Create API instance
                    const api = DigitalWardrobeAPI.getAPI();
                    
                    // Try to get user from backend
                    const userBO = await api.getUserByGoogleId(result.user.uid);
                    
                    if (!userBO) {
                        // If user doesn't exist, create new user
                        await api.addUser({
                            google_id: result.user.uid,
                            email: result.user.email,
                            firstname: result.user.displayName?.split(' ')[0] || '',
                            lastname: result.user.displayName?.split(' ')[1] || '',
                            nickname: result.user.displayName || ''
                        });
                    }
                    
                    setUser(result.user);
                } catch (error) {
                    console.error('Backend communication error:', error);
                    setError('Failed to communicate with backend');
                }
            }
        } catch (error) {
            console.error('Firebase authentication error:', error);
            setError('Authentication failed');
        } finally {
            setLoading(false);
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

    const value = {
      user,
      loading,
      error,
      signInWithGoogle,
      signOut
    };

    return (
      <AuthContext.Provider value={value}>
        {children}
      </AuthContext.Provider>
    );
};

// export auth context
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};



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