import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Login from './components/pages/Login';  // Statt SignIn
import Register from './components/pages/Register';  // Statt SignUp
import Header from './components/pages/Header';  // Optional, falls du den Header nutzen möchtest

const AppRoutes = () => (
  <Routes>
    {/* Login und Register statt SignIn und SignUp */}
    <Route path="/login" element={<Login />} />
    <Route path="/register" element={<Register />} />

    {/* Optional Header, wenn du diesen in deiner Route haben möchtest */}
    <Route path="/" element={<Header />} />  {/* Die Startseite oder Header-Seite */}
  </Routes>
);

export default AppRoutes;
