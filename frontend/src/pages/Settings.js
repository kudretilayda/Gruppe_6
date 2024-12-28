import React from 'react';
import { Typography, Button, Grid } from '@mui/material';

const Settings = () => {
  return (
    <div className="p-4">
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <Typography variant="h4">Einstellungen</Typography>
        </Grid>
        <Grid item xs={12}>
          {/* Hier könnten Optionen für App-Einstellungen oder Präferenzen kommen */}
          <Button variant="contained" color="primary">
            Einstellungen bearbeiten
          </Button>
        </Grid>
      </Grid>
    </div>
  );
};

export default Settings;
