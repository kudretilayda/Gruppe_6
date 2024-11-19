// src/components/layout/MainLayout.jsx
import React from 'react';
import { Box } from '@material-ui/core';
import Navbar from './Navbar'; // Navbar-Komponente, die die obere Navigation enthält
import Sidebar from './Sidebar'; // Sidebar-Komponente, die seitlich navigiert werden kann

export function MainLayout({ children }) {
  return (
    <Box display="flex">
      <Navbar />
      <Sidebar />
      <Box
        component="main"
        sx={{
          flexGrow: 1,
          p: 3,
          marginTop: '64px', // Höhe der Navbar, damit der Inhalt darunter beginnt
          marginLeft: '240px', // Breite der Sidebar, damit der Inhalt rechts davon erscheint
        }}
      >
        {children} {/* Hier wird der Inhalt (Content) angezeigt */}
      </Box>
    </Box>
  );
}
