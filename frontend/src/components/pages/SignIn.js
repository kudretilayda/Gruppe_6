import React from 'react';
import PropTypes from 'prop-types';
import { Button, Grid, Typography, Container, Box } from '@mui/material';
import GoogleIcon from '@mui/icons-material/Google'

/**
 * Zeigt eine Landingpage für Benutzer, die noch nicht eingeloggt sind.
 * Bietet einen Anmeldebutton an, um sich mit einem bestehenden Google-Konto anzumelden.
 * Die Komponente verwendet Firebase für den Anmeldeprozess über eine Weiterleitung.
 *
 * @see Siehe Googles [firebase authentication](https://firebase.google.com/docs/web/setup)
 * @see Siehe Googles [firebase API reference](https://firebase.google.com/docs/reference/js)
 *
 */
const SignIn = ({ onSignIn }) => {
	//Button Click handler
	const handleSignInButtonClicked = () => {
		if (typeof onSignIn !== 'function') {
			console.error('onSingIn prop is not a function:', onSignIn);
			return;
		}
		onSignIn();
	};

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
