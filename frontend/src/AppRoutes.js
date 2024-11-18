import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import SignIn from './components/pages/SignIn';   // Pfad zu SignIn anpassen
import SignUp from './components/pages/SignUp';   // Pfad zu SignUp anpassen
import Dashboard from './components/pages/Dashboard'; // Pfad zu Dashboard anpassen

const AppRoutes = () => {
    return (
        <Routes>
            <Route path="/" element={<Navigate to="/signin" />} />
            <Route path="/signin" element={<SignIn />} />
            <Route path="/signup" element={<SignUp />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="*" element={<h1>404: Seite nicht gefunden</h1>} />
        </Routes>
    );
};

export default AppRoutes;



