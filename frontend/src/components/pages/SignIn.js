import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { Button, Grid, Typography, CircularProgress, Alert } from '@mui/material';

function SignIn({ onSignIn }) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSignInButtonClicked = async () => {
    setLoading(true);
    setError(''); // Fehler zurücksetzen, bevor wir die Anmeldung versuchen
    try {
      await onSignIn();
    } catch (error) {
      setError('Anmeldung fehlgeschlagen. Bitte versuche es später erneut.');
    }
    setLoading(false);
  };

  return (
    <div>
      <Typography sx={{ margin: 2 }} align="center" variant="h6">
        Willkommen in deinem digitalen Kleiderschrank
      </Typography>
      <Typography sx={{ margin: 2 }} align="center">
        Es scheint, dass Sie nicht angemeldet sind.
      </Typography>
      <Typography sx={{ margin: 2 }} align="center">
        Um die Dienste der digitalen Garderobe zu nutzen, melden Sie sich bitte an.
      </Typography>

      {error && (
        <Alert severity="error" sx={{ margin: 2 }}>
          {error}
        </Alert>
      )}

      <Grid container justifyContent="center">
        <Grid item>
          <Button
            variant="contained"
            color="primary"
            onClick={handleSignInButtonClicked}
            disabled={loading}
          >
            {loading ? <CircularProgress size={24} color="inherit" /> : 'Mit Google anmelden'}
          </Button>
        </Grid>
      </Grid>
    </div>
  );
}

SignIn.propTypes = {
  onSignIn: PropTypes.func.isRequired,
};

export default SignIn;
