import React from 'react';
import ReactDOM from 'react-dom';
import AppRoutes from './AppRoutes';  // Richtiger Pfad
import { BrowserRouter as Router } from 'react-router-dom';
import './index.css';

ReactDOM.render(
  <React.StrictMode>
    <Router>
      <AppRoutes />
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);
