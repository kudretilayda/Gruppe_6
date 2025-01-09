import React from 'react';
import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import { Link as RouterLink } from 'react-router-dom';

function Navbar() {
  return (
      <AppBar position="static" color="primary">
          <Toolbar>
              <Typography
                  variant="h6"
                  component={RouterLink}
                  to="/"
                  style={{
                      color: 'white',
                      textDecoration: 'none',
                      flexGrow: 1, // Pushes the buttons to the right
              }}
              >
                  Digital Wardrobe
              </Typography>
              <Box>
                  <Button color="inherit" component={RouterLink} to="/wardrobe" style={{ textTransform: 'none' }}>
                      Wardrobe
                  </Button>

                  <Button color="inherit" component={RouterLink} to="/outfits" style={{ textTransform: 'none' }}>
                      Outfits
                  </Button>

                  <Button color="inherit" component={RouterLink} to="/styles" style={{ textTransform: 'none' }}>
                      Styles
                  </Button>

                  <Button color="inherit" component={RouterLink} to="/types" style={{ textTransform: 'none' }}>
                      Types
                  </Button>

                  <Button color="inherit" component={RouterLink} to="/profile" style={{ textTransform: 'none' }}>
                      Profile
                  </Button>
              </Box>
          </Toolbar>
      </AppBar>
  );
}

export default Navbar;
