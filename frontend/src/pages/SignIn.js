import React from "react";
import { Button, Container, Typography } from "@mui/material";
import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";

const LoginPage = () => {
  const handleGoogleSignIn = () => {
    const auth = getAuth();
    const provider = new GoogleAuthProvider();
    signInWithPopup(auth, provider)
      .then((result) => console.log("User signed in:", result.user))
      .catch((error) => console.error("Error signing in:", error));
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
