// src/components/LoadingSpinner.js
import React from 'react';
import { CircularProgress, Box } from '@mui/material';

const LoadingSpinner = () => {
  return (
    <Box display="flex" justifyContent="center" m={4}>
      <CircularProgress />
    </Box>
  );
};

export default LoadingSpinner;