// src/pages/HomePage.js
import React from 'react';
import { Card, CardContent, Typography, Grid } from '@mui/material';
import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div className="p-4">
      <Typography variant="h4" className="mb-4">
        Willkommen in deinem digitalen Kleiderschrank
      </Typography>

      <Grid container spacing={3}>
        <Grid item xs={12} sm={6} md={4}>
          <Card component={Link} to="/wardrobe" style={{ textDecoration: 'none' }}>
            <CardContent>
              <Typography variant="h5">Kleiderschrank</Typography>
              <Typography color="textSecondary">
                Verwalte deine Kleidungsstücke
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} sm={6} md={4}>
          <Card component={Link} to="/styles" style={{ textDecoration: 'none' }}>
            <CardContent>
              <Typography variant="h5">Styles</Typography>
              <Typography color="textSecondary">
                Entdecke und erstelle neue Styles
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} sm={6} md={4}>
          <Card component={Link} to="/outfits" style={{ textDecoration: 'none' }}>
            <CardContent>
              <Typography variant="h5">Outfits</Typography>
              <Typography color="textSecondary">
                Erstelle neue Outfits
              </Typography>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </div>
  );
};

export default HomePage;
