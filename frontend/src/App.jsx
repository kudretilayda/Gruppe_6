import React from "react";
import {
  BrowserRouter,
  Routes,
  Route,
  Link,
  useNavigate,
} from "react-router-dom";
import {
  Typography,
  AppBar,
  Button,
  CssBaseline,
  Grid,
  Toolbar,
  Container,
} from "@mui/material";
import CheckroomIcon from "@mui/icons-material/Checkroom";
import Register from "./components/Login_Register/Register";
import Login from "./components/Login_Register/Login";
import Header from "./Header";
import OutfitBuilder from "./components/Oufit_Builder/OB";

const App = () => {
  const navigate = useNavigate();

  const handleLogin = (username, password) => {
    if (username === "admin" && password === "admin") {
      navigate("/outfitbuilder");
    }
  };

  return (
    <BrowserRouter>
      <CssBaseline />
      <Header />
      <Routes>
        <Route
          path="/"
          element={<main>{/* Home-Seite Code unverändert */}</main>}
        />
        <Route path="/login" element={<Login onLogin={handleLogin} />} />
        <Route path="/register" element={<Register />} />
        <Route path="/outfitbuilder" element={<OutfitBuilder />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;




