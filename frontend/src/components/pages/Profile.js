import React, { useState, useEffect } from "react";
import { Container, TextField, Button, Typography } from "@mui/material";

const ProfilePage = () => {
  const [nickname, setNickname] = useState("");
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");

  // Lade die Daten aus localStorage, wenn die Komponente geladen wird
  useEffect(() => {
    const savedNickname = localStorage.getItem("nickname");
    const savedFirstname = localStorage.getItem("firstname");
    const savedLastname = localStorage.getItem("lastname");

    if (savedNickname) setNickname(savedNickname);
    if (savedFirstname) setFirstname(savedFirstname);
    if (savedLastname) setLastname(savedLastname);
  }, []);

  // Speichere die Daten in localStorage, wenn der Benutzer "Save Changes" drückt
  const handleSave = () => {
    localStorage.setItem("nickname", nickname);
    localStorage.setItem("firstname", firstname);
    localStorage.setItem("lastname", lastname);

    alert("Profile saved successfully!");
  };

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        My Profile
      </Typography>

      {/* Nickname */}
      <TextField
        fullWidth
        label="Nickname"
        value={nickname}
        onChange={(e) => setNickname(e.target.value)}
        style={{ marginBottom: "20px" }}
      />

      {/* Firstname */}
      <TextField
        fullWidth
        label="Firstname"
        value={firstname}
        onChange={(e) => setFirstname(e.target.value)}
        style={{ marginBottom: "20px" }}
      />

      {/* Lastname */}
      <TextField
        fullWidth
        label="Lastname"
        value={lastname}
        onChange={(e) => setLastname(e.target.value)}
        style={{ marginBottom: "20px" }}
      />

      <Button
        variant="contained"
        color="primary"
        style={{ marginTop: "20px" }}
        onClick={handleSave}
      >
        Save Changes
      </Button>
    </Container>
  );
};

export default ProfilePage;
