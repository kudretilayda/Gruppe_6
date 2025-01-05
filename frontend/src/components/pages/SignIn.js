import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Button, Grid, Typography } from '@mui/material';

/**
 * Zeigt eine Landingpage für Benutzer, die noch nicht eingeloggt sind.
 * Bietet einen Anmeldebutton an, um sich mit einem bestehenden Google-Konto anzumelden.
 * Die Komponente verwendet Firebase für den Anmeldeprozess über eine Weiterleitung.
 *
 * @see Siehe Googles [firebase authentication](https://firebase.google.com/docs/web/setup)
 * @see Siehe Googles [firebase API reference](https://firebase.google.com/docs/reference/js)
 *
 */
class SignIn extends Component {

	/**
	 * Behandelt das Klicken des Anmeldebuttons und ruft die übergebene onSignIn-Handler-Funktion auf.
	 */
	handleSignInButtonClicked = () => {
		this.props.onSignIn();
	}

	/** Rendert die Anmeldeseite, wenn das Benutzerobjekt null ist */
	render() {
		return (
			<div>
				<Typography sx={{ margin: 2 }} align='center' variant='h6'>
					Willkommen im Digitalen Kleiderschrank
				</Typography>
				<Typography sx={{ margin: 2 }} align='center'>
					Es scheint, dass Sie noch nicht eingeloggt sind.
				</Typography>
				<Typography sx={{ margin: 2 }} align='center'>
					Um die Dienste des Digitalen Kleiderschranks zu nutzen, melden Sie sich bitte an.
				</Typography>
				<Grid container justifyContent='center'>
					<Grid item>
						<Button variant='contained' color='primary' onClick={this.handleSignInButtonClicked}>
							Mit Google anmelden
						</Button>
					</Grid>
				</Grid>
			</div>
		);
	}
}

/** PropTypes */
SignIn.propTypes = {
	/**
	 * Handler-Funktion, die aufgerufen wird, wenn der Benutzer sich anmelden möchte.
	 */
	onSignIn: PropTypes.func.isRequired,
}

export default SignIn;
