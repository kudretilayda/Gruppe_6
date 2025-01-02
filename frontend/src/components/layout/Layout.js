import React from 'react';
import { Link } from 'react-router-dom'; // React Router Link für Navigation
import { AppBar, Toolbar, Button } from '@mui/material';

const Layout = ({ children }) => {
  return (
    <div>
      <AppBar position="sticky">
        <Toolbar>
          {/* Andere Navigationselemente */}
          <Button color="inherit" component={Link} to="/wardrobe">
            Wardrobe
          </Button>
          <Button color="inherit" component={Link} to="/styles">
            Styles
          </Button>
          <Button color="inherit" component={Link} to="/outfits">
            Outfits
          </Button>
          <Button color="inherit" component={Link} to="/settings"> {/* Hier der Menüpunkt für Einstellungen */}
            Einstellungen
          </Button>
        </Toolbar>
      </AppBar>
      <div>{children}</div>
    </div>
  );
};

export default Layout;
