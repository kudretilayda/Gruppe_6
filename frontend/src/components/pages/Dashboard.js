import React from 'react';
import { Typography, Container } from '@mui/material';

const Dashboard = ({ user }) => {
  return (
    <Container>
      <Typography variant="h4">Willkommen zum Dashboard, {user.name}!</Typography>
      {/* Hier kannst du das Dashboard erweitern */}
    </Container>
  );
};

export default Dashboard;



