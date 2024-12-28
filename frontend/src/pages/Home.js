import React from 'react';
import { Link } from 'react-router-dom';
import { Container, Typography, Box, Button } from '@mui/material';

const Home = () => {
  return (
    <Container maxWidth="md">
      <Box sx={{ mt: 8, textAlign: 'center' }}>
        <Typography variant="h3" gutterBottom>
          Willkommen zu deinem digitalen Kleiderschrank
        </Typography>
        <Typography variant="body1" paragraph>
          Verwalte deine Kleidung, Styles und Outfits einfach und effizient.
        </Typography>

        <Box sx={{ mt: 4 }}>
          <Button variant="contained" color="primary" sx={{ m: 1 }}>
            <Link to="/kleiderschrank" style={{ textDecoration: 'none', color: 'white' }}>
              Kleiderschrank
            </Link>
          </Button>

          <Button variant="contained" color="secondary" sx={{ m: 1 }}>
            <Link to="/styles" style={{ textDecoration: 'none', color: 'white' }}>
              Styles
            </Link>
          </Button>

          <Button variant="contained" sx={{ m: 1 }}>
            <Link to="/outfits" style={{ textDecoration: 'none', color: 'black' }}>
              Outfits
            </Link>
          </Button>
        </Box>
      </Box>
    </Container>
  );
};

export default Home;


// src/pages/Home.js
//import React from 'react';
//import { Link } from 'react-router-dom';

//const Home = () => {
 // return (
  //  <div>
   //   <h1>Willkommen zu deinem digitalen Kleiderschrank</h1>
   //   <p>Verwalte deine Kleidung, Styles und Outfits einfach und effizient.</p>
    //  <nav>
    //    <ul>
     //     <li><Link to="/kleiderschrank">Kleiderschrank</Link></li>
     //     <li><Link to="/styles">Styles</Link></li>
     //     <li><Link to="/outfits">Outfits</Link></li>
     //   </ul>
     // </nav>
   // </div>
 // );
//};

//export default Home;