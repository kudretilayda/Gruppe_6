import React from "react";
import { AppBar, Toolbar, Typography, Button, Box } from "@mui/material";
import { Link } from "react-router-dom";

const Navbar = ({ user, onLogout }) => {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" sx={{ flexGrow: 1 }}>
          Digital Wardrobe
        </Typography>

        {/* Navigation Links */}
        {user && (
          <Box sx={{ display: "flex", gap: "10px" }}>
            <Button color="inherit" component={Link} to="/">
              Home
            </Button>
            <Button color="inherit" component={Link} to="/wardrobe">
              Wardrobe
            </Button>
            <Button color="inherit" component={Link} to="/styles">
              Styles
            </Button>
            <Button color="inherit" component={Link} to="/outfits">
              Outfits
            </Button>
            <Button color="inherit" component={Link} to="/profile">
              Profile
            </Button>
          </Box>
        )}

        {/* Logout Button */}
        {user ? (
          <Button color="inherit" onClick={onLogout}>
            Logout
          </Button>
        ) : (
          <Button color="inherit" component={Link} to="/login">
            Login
          </Button>
        )}
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
