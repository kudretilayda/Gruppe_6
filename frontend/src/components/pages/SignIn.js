/*import React from 'react';
import { Button, Container, Typography, Box } from '@mui/material';
import { useAuth } from '../../context/AuthContext';
import GoogleIcon from '@mui/icons-material/Google';
import { auth } from '../../firebase.js';
import firebaseConfig from '../../firebaseConfig.js'

const SignIn = () => {
    const { signInWithGoogle } = useAuth();

    // funktion um google sign in zu handlen
    const handleSignIn = () => {
        signInWithGoogle();
    };

    return (
        <Container maxWidth="sm">
            <Box sx={{ mt: 8, textAlign: 'center' }}>
                <Typography variant="h4" gutterBottom>
                    Willkommen im Digitalen Kleiderschrank
                </Typography>

                <Typography sx={{ mb: 4 }}>
                    Es scheint, dass Sie noch nicht eingeloggt sind.
                </Typography>

                <Button
                    variant="contained"
                    onClick={handleSignIn}
                    startIcon={<GoogleIcon />}
                >
                    MIT GOOGLE ANMELDEN
                </Button>
            </Box>
        </Container>
    );
};

export default SignIn;
*/


/*import React from 'react';
import PropTypes from 'prop-types';
import { Button, Grid, Typography, Container, Box } from '@mui/material';
import GoogleIcon from '@mui/icons-material/Google'
import { useNavigate } from 'react-router-dom';
import {useAuth} from "../../context/AuthContext";


/*
 * Zeigt eine Landingpage für Benutzer, die noch nicht eingeloggt sind.
 * Bietet einen Anmeldebutton an, um sich mit einem bestehenden Google-Konto anzumelden.
 * Die Komponente verwendet Firebase für den Anmeldeprozess über eine Weiterleitung.
 *
 * @see Siehe Googles [firebase authentication](https://firebase.google.com/docs/web/setup)
 * @see Siehe Googles [firebase API reference](https://firebase.google.com/docs/reference/js)
 *
 */

/*const SignIn = () => {
	const {signInWithGoogle} = useAuth();
	const navigate = useNavigate();
	const handleSignIn = async () => {
		await signInWithGoogle();
		navigate('/home'); // Weiterleitung nach erfolgreichem Sign-In
	};
	return (
		<Button onClick={handleSignIn}>Mit Google anmelden</Button>
	);
};

export default SignIn;

/*
	return (
		<Container maxWidth="sm">
			<Box sx={{
				mt: 8,
				display: 'flex',
				flexDirection: 'column',
				alignItems: 'center',
			}}>
				<Typography variant='h4' gutterBottom align='center'>
					Willkommen im Digitalen Kleiderschrank
				</Typography> 

				<Typography variant='h6' align='center' color='textSecondary' paragraph>
					Es scheint, dass Sie noch nicht eingeloggt sind.
				</Typography> 

				<Typography align='center' color='textSecondary' paragraph>
					Um die Dienste des Digitalen Kleiderschranks zu nutzen,
					melden Sie sich bitte an.
				</Typography>
				
				<Button
					variant='contained'
					color='primary'
					onClick={handleSignInButtonClicked}
					startIcon={<GoogleIcon />}
					size='large'
					sx={{ mt: 3 }}
				>
					Mit Google anmelden
				</Button>
			</Box>
		</Container>
	);
};

SignIn.propTypes = {
	//definiert die benötigte SignIn prop
	onSignIn: PropTypes.func.isRequired,
};

export default SignIn;

 */

import React from 'react';
import { Button, Container, Typography, Box } from '@mui/material';
import { useAuth } from '../../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import GoogleIcon from '@mui/icons-material/Google';

const SignIn = () => {
  const { signInWithGoogle } = useAuth();
  const navigate = useNavigate();

  const handleSignIn = async () => {
    try {
      await signInWithGoogle();
      navigate('/home');
    } catch (error) {
      console.error('Error signing in:', error);
      // Optional: Add error handling UI here
    }
  };

  return (
    <Container maxWidth="sm">
      <Box
        sx={{
          mt: 8,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          gap: 4
        }}
      >
        <Typography variant="h4" component="h1" align="center">
          Willkommen im Digitalen Kleiderschrank
        </Typography>

        <Typography variant="body1" align="center" color="text.secondary">
          Bitte melden Sie sich an, um fortzufahren.
        </Typography>

        <Button
          variant="contained"
          size="large"
          onClick={handleSignIn}
          startIcon={<GoogleIcon />}
          sx={{ mt: 2 }}
        >
          Mit Google anmelden
        </Button>
      </Box>
    </Container>
  );
};

export default SignIn;
