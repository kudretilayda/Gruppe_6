import React from 'react';
import { AppBar, Toolbar, Typography, Button } from '@material-ui/core';
import { useAuth } from '../../hooks/useAuth';

export default function Navbar() {
  const { user, signOut } = useAuth();

  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" style={{ flexGrow: 1 }}>
          Digitaler Kleiderschrank
        </Typography>
        {user && (
          <Button color="inherit" onClick={signOut}>
            Logout
          </Button>
        )}
      </Toolbar>
    </AppBar>
  );
}