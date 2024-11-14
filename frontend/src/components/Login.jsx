import React, {useState} from "react";
import { TextField, FormControl, Button } from "@mui/material";
import { Link } from "react-router-dom";

const Login = () => { // Hier werden 4 Variablen erstellt (email, password, emailError, passwordError)

    const [email, setEmail] = useState(""); // email speichert die Email
    const [password, setPassword] = useState(""); // password speichert das PW
    const [emailError, setEmailError] = useState(false); // emailError überprüft ob die Email richtig eingegeben wurde
    const [passwordError, setPasswordError] = useState(false); // passwordError überprüft ob das PW richtig eingegeben wurde

    const handleSubmit = (Event) => {
        Event.preventDefault();

        setEmailError(false);
        setPasswordError(false);

        if (email === '') {
            setEmailError(true);
        }

        if (password === '') {
            setPasswordError(true);
        }

        if (email && password) {
            console.log("Email:", email, "Password:", password)
            // Authentifizierung kann hier eingebaut werden
        }
    }

    return (
        <React.Fragment>
            <form autoComplete="off" onSubmit={handleSubmit}>
                <h2>Login Form</h2>

                <TextField
                    label = 'Email'
                    onChange = {(e) => setEmail(e.target.value)}
                    required
                    variant = "outlined"
                    color = "secondary"
                    type = "email"
                    sx = {{ mb: 3 }}
                    fullWidth
                    value = {email}
                    error = {emailError}
                />

                <TextField
                    label = 'Password'
                    onChange = {(e) => setPassword(e.target.value)}
                    required
                    variant = "outlined"
                    color = "secondary"
                    type = "password"
                    value = {password}
                    error = {passwordError}
                    fullWidth
                    sx = {{ mb: 3}}
                />

                <Button variant="outlined" color="secondary" type="submit">
                    Login
                </Button>
                
            </form>

            <small>Need an account? <Link to="/register"> Register here </Link>  </small>

        </React.Fragment>
    );
};

export default Login;