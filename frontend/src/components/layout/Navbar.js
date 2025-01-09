import React, { useState } from 'react';
import { AppBar, Toolbar, Typography, Button, Box, Menu, MenuItem, IconButton, ListItemIcon } from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu'; // Importiere das Icon
import ExitToAppIcon from '@mui/icons-material/ExitToApp';
import { Link as RouterLink } from 'react-router-dom';

function Navbar() {
  const [anchorEl, setAnchorEl] = useState(null);

  const handleMenuOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  return (
    <AppBar position="static" color="primary">
      <Toolbar>
        {/* Link zur Startseite */}
        <Typography
          variant="h6"
          component={RouterLink}
          to="/"
          style={{
            color: 'white',
            textDecoration: 'none',
            flexGrow: 1,
          }}
        >
          Digital Wardrobe
        </Typography>

        {/* Buttons */}
        <Box>
          <Button
            color="inherit"
            component={RouterLink}
            to="/wardrobe"
            style={{ textTransform: 'none' }}
          >
            Wardrobe
          </Button>

          <Button
            color="inherit"
            component={RouterLink}
            to="/outfits"
            style={{ textTransform: 'none' }}
          >
            Outfits
          </Button>

          <Button
            color="inherit"
            component={RouterLink}
            to="/types"
            style={{ textTransform: 'none' }}
          >
            Types
          </Button>

          <Button
            color="inherit"
            component={RouterLink}
            to="/profile"
            style={{ textTransform: 'none' }}
          >
            Profile
          </Button>

          {/* Hamburger-Icon als Dropdown-Button */}
          <IconButton
            color="inherit"
            aria-controls="more-menu"
            aria-haspopup="true"
            onClick={handleMenuOpen}
          >
            <MenuIcon /> {/* Hier ist das Hamburger-Menü-Icon */}
          </IconButton>
          <Menu
            id="more-menu"
            anchorEl={anchorEl}
            open={Boolean(anchorEl)}
            onClose={handleMenuClose}
          >
            <MenuItem
              onClick={handleMenuClose}
              component={RouterLink}
              to="/profile"
            >
              Profil
            </MenuItem>
            <MenuItem
              onClick={handleMenuClose}
              component={RouterLink}
              to="/wardrobe"
            >
              Kleidungsstück
            </MenuItem>
            <MenuItem
              onClick={handleMenuClose}
              component={RouterLink}
              to="/constraints"
            >
              Constraints
            </MenuItem>
            <MenuItem
              onClick={handleMenuClose}
              component={RouterLink}
              to="/styles"
            >
              Style
            </MenuItem>
            <MenuItem
              onClick={handleMenuClose}
              component={RouterLink}
              to="/outfits"
            >
              Outfit
            </MenuItem>
            <MenuItem
              onClick={handleMenuClose}
              component={RouterLink}
              to="/logout"
            >
              Abmelden
            <ListItemIcon style={{ marginLeft: 'auto' }}>
            <ExitToAppIcon fontSize="small" />
            </ListItemIcon>
            </MenuItem>
          </Menu>
        </Box>
      </Toolbar>
    </AppBar>
  );
}

export default Navbar;