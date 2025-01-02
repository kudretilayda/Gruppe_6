// src/components/ErrorMessage.js
import React from 'react';
import { Alert } from '@material-ui/lab';

const ErrorMessage = ({ message }) => {
  if (!message) return null;

  return (
    <Alert severity="error" style={{ marginBottom: '1rem' }}>
      {message}
    </Alert>
  );
};

export default ErrorMessage;