import React, { useState } from "react";
import { Container, TextField, Button, Typography } from "@mui/material";

const ProfilePage = () => {
  const [nickname, setNickname] = useState("User");

  const handleSave = () => {
    console.log("Profile saved:", nickname);
  };

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        My Profile
      </Typography>
      <TextField
        fullWidth
        label="Nickname"
        value={nickname}
        onChange={(e) => setNickname(e.target.value)}
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
