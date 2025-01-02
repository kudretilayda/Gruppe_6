import React from "react";
import { Button, Container, Typography } from "@mui/material";
import { auth } from "../firebaseConfig"; // Firebase-Setup importieren
import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";

const LoginPage = ({ onLoginSuccess }) => {
  const handleGoogleSignIn = () => {
    const provider = new GoogleAuthProvider();
    try {
      const result = await signInWithPopup(auth, provider);
      const user = result.user;
      console.log("User signed in:", user);
      onLoginSuccess(user); // Benachrichtige die App über den erfolgreichen Login
    } catch (error) {
      console.error("Login failed:", error);
    }
  };
  return (
    <Container
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        height: "100vh",
      }}
    >
      <Typography variant="h4" gutterBottom>
        Welcome to Digital Wardrobe
      </Typography>
      <Button
        variant="contained"
        color="primary"
        onClick={handleGoogleSignIn}
        style={{ marginTop: "20px" }}
      >
        Sign in with Google
      </Button>
    </Container>
  );
};

export default LoginPage;
