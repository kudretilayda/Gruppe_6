import React, {useEffect} from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.js';
import { CssBaseline } from '@mui/material';
import { ThemeProvider, createTheme } from '@mui/material/styles';

// Create a theme instance
const theme = createTheme();

/*
fetch("http://localhost:3000")
    .then(res => res.json())
    .then(data => console.log(data))

const express = require('express')
const app = express()

app.get("http://localhost:3000")
app.listen(3000)
*/

const response = await fetch("http://localhost:3000/styles", {
    method: "GET",
    credentials: "include", // Wichtig
    headers: {
        "Content-Type": "application/json",
    },
});

const cors = require('cors')


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <App />
    </ThemeProvider>
  </React.StrictMode>
);
