import React from 'react';
import { AppBar, Toolbar, Typography } from '@mui/material';
import { Link } from 'react-router-dom';
import CheckroomIcon from '@mui/icons-material/Checkroom';

// Definiert die Header-Komponente als Funktion
function Header() {
   return (
       // AppBar erstellt eine Navigationsleiste am oberen Bildschirmrand
       <AppBar position="relative">
           {/* Toolbar organisiert den Inhalt horizontal */}
           <Toolbar>
               {/* Fügt das Kleiderbügel-Icon ein */}
               <CheckroomIcon />
               {/* Link macht den Text klickbar und leitet zur Homepage */}
               <Link to="/" style={{ textDecoration: 'none', color: 'inherit' }}>
                   {/* Typography formatiert den Text einheitlich */}
                   <Typography variant="h6">
                       Kleiderschrank-Projekt
                   </Typography>
               </Link>
           </Toolbar>
       </AppBar>
   );
}

// Macht die Header-Komponente für andere Dateien verfügbar
export default Header;