import React from 'react';
import { Link } from 'react-router-dom';
import { AppBar, Toolbar, Button } from '@mui/material';

const Layout = ({ children }) => {
  return (
    <>
      <AppBar position="static">
        <Toolbar>
          <Button component={Link} to="/" color="inherit">
            Home
          </Button>
          <Button component={Link} to="/wardrobe" color="inherit">
            Kleiderschrank
          </Button>
          <Button component={Link} to="/styles" color="inherit">
            Styles
          </Button>
          <Button component={Link} to="/outfits" color="inherit">
            Outfits
          </Button>
        </Toolbar>
      </AppBar>
      <div>{children}</div> {/* This renders the page content inside Layout */}
    </>
  );
};

export default Layout;
