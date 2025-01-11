import React, { useState, useEffect } from 'react';
import {
  AppBar,
  Toolbar,
  Typography,
  IconButton,
  Menu,
  MenuItem,
  Box,
  Divider,
} from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';
import LogoutIcon from '@mui/icons-material/Logout';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import DigitalWardrobeAPI from '../../api/DigitalWardrobeAPI';

const Navbar = () => {
  // status management für user daten
  const [menuAnchor, setMenuAnchor] = useState(null);
  const [userData, setUserData] = useState(null);
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  
  // fetch user daten
  useEffect(() => {
    const fetchUserData = async () => {
      if (user?.uid) {
        try {
          const response = await DigitalWardrobeAPI.getAPI().getUserByGoogleId(user.uid);
          console.log("API Response:", response);
          setUserData(response);
        } catch (error) {
          if (error.response) {
            console.error('Error fetching user data:', error.response.status, error.response.data);
          } else {
            console.error('Error fetching user data:', error.message);
          }
        }
      }
    }
  });
  // menü item config
  const menuItems = [
    { label: 'Home', path: '/home' },
    { label: 'Profil', path: '/profile' },
    { label: 'Kleidungsstück', path: '/wardrobe' },
    { label: 'Constraints', path: '/constraints' },
    { label: 'Style', path: '/styles' },
    { label: 'Outfit', path: '/outfits' },
  ];

  // menü handler
  const handleMenuOpen = (event) => {
    setMenuAnchor(event.currentTarget);
  };

  const handleMenuClose = () => {
    setMenuAnchor(null);
  };

  const handleNavigate = (path) => {
    navigate(path);
    handleMenuClose();
  };

  // logout handler 
  const handleLogout = async () => {
    try {
      await logout(); 
      navigate('/');
      handleMenuClose();
    } catch (error) {
      console.error('Logout error:', error);
    }
  };

  return (
    <AppBar position="static" sx={{ color: '#1976d2' }}>
      <Toolbar>
        {/* LOGO/NAME */}
        <Typography
          variant="h6"
          component="div"
          sx={{ 
            flexGrow: 1, 
            cursor: 'pointer',
            color: 'white'
          }}
          onClick={() => navigate('/')}
        >
          DigitalWardrobe
        </Typography>

        {/* zeigt das menü nur authentifizierten nutzern */}
        {user && (
          <>
            <IconButton
              color="inherit"
              onClick={handleMenuOpen}
              sx={{ ml: 2 }}
            >
              <MenuIcon />
            </IconButton>

            {/* dropdown menü mit @mui */}
            <Menu
              anchorEl={menuAnchor}
              open={Boolean(menuAnchor)}
              onClose={handleMenuClose}
              anchorOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              transformOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              PaperProps={{
                elevation: 3,
                sx: {
                  mt: 5,
                  minWidth: 200,
                  borderRadius: '4px',
                  '& .MuiMenuItem-root': {
                    py: 1,
                    px: 2,
                  }
                }
              }}
            >
              {/* user information falls vorhanden */}
              {userData && (
                <Box sx={{ p: 2, borderBottom: '1px solid rgba(0,0,0,0.12)' }}>
                  <Typography variant="subtitle2">
                    {userData.getNickname() || userData.getFirstName()}
                  </Typography>
                  <Typography variant="body2" color="textSecondary">
                    {userData.getEmail()}
                  </Typography>
                </Box>
              )}

              {/* nav menü items */}
              {menuItems.map((item) => (
                <MenuItem 
                  key={item.path}
                  onClick={() => handleNavigate(item.path)}
                >
                  {item.label}
                </MenuItem>
              ))}

              <Divider sx={{ my: 1 }} />

              {/* logout */}
              <MenuItem 
                onClick={handleLogout}
                sx={{ 
                  color: 'error.main',
                  '&:hover': {
                    backgroundColor: 'error.light',
                  }
                }}
              >
                <LogoutIcon sx={{ mr: 1, fontSize: 20 }} />
                Abmelden
              </MenuItem>
            </Menu>
          </>
        )}
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;