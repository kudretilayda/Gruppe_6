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
          to="/home"
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
            KLEIDUNGSSTÜCK
          </Button>

          <Button
            color="inherit"
            component={RouterLink}
            to="/Outfits"
            style={{ textTransform: 'none' }}
          >
            OUTFIT
          </Button>

          <Button
            color="inherit"
            component={RouterLink}
            to="/styles"
            style={{ textTransform: 'none' }}
          >
            STYLE
          </Button>
          
          <Button
            color="inherit"
            component={RouterLink}
            to="/Profile"
            style={{ textTransform: 'none' }}
          >
            PROFIL
          </Button>

          <Button
            color="inherit"
            component={RouterLink}
            to="/constraints"
            style={{ textTransform: 'none' }}
          >
            CONSTRAINTS
          </Button>

          <Button
            color="inherit"
            component={RouterLink}
            to="/settings"
            style={{ textTransform: 'none' }}
          >
            EINSTELLUNGEN
          </Button>

          <Button
            color="inherit"
            component={RouterLink}
            to="/Logout"
            style={{ textTransform: 'none' }}
          >
            ABMELDEN
            <ListItemIcon style={{ marginLeft: 'auto', color: 'white' }}>
            <ExitToAppIcon fontSize="small" />
            </ListItemIcon>
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
              to="/Wardrobe"
            >
              Kleidungsstück
            </MenuItem>


            <MenuItem
              onClick={handleMenuClose}
              component={RouterLink}
              to="/Outfits"
            >
              Outfit
            </MenuItem>


            <MenuItem
              onClick={handleMenuClose}
              component={RouterLink}
              to="/Styles"
            >
              Style
            </MenuItem>


            <MenuItem
              onClick={handleMenuClose}
              component={RouterLink}
              to="/Profile"
            >
              Profil
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
              to="/settings"
            >
              Einstellungen
            </MenuItem>


            <MenuItem
              onClick={handleMenuClose}
              component={RouterLink}
              to="/SignIn"
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