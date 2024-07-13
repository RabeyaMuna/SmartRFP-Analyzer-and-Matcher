import React from 'react';
import { useNavigate } from 'react-router-dom';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import CircularProgress from '@mui/material/CircularProgress';
import { authenticate } from './auth';
import '../styles/login.css';

export default function SignIn() {
  const [isLoading, setIsLoading] = React.useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log('Form submission started');

    const data = new FormData(event.currentTarget);
    const email = data.get('EMAIL');
    const password = data.get('PASSWORD');
    setIsLoading(true);

    console.log('Calling isValidCredentials');
    const response = await isValidCredentials(email, password);
    console.log('isValidCredentials response:', response);
    setIsLoading(false);

    if (response) {
      console.log('Login successful');
      localStorage.setItem('isLoggedIn', 'true');
      navigate('/');
    } else {
      console.log('Login failed');
      alert('Invalid username or password');
    }

    console.log('Form submission ended');
  };

  async function isValidCredentials(email, password) {
    console.log('isValidCredentials called with:', email, password);
    const isAuthenticated = await authenticate(email, password);
    return isAuthenticated;
  }

  return (
    <ThemeProvider theme={createTheme()}>
      <Box className="login-container">
        <Container component="main" maxWidth="xs">
          <CssBaseline />
          <Box className="login-box">
            {isLoading && (
              <CircularProgress color="inherit" className="loading-indicator" />
            )}
            <Avatar sx={{ m: 1, bgcolor: 'black' }}>
              <LockOutlinedIcon style={{ color: '#d4ff00' }} />
            </Avatar>
            <Typography component="h1" variant="h5">
              Sign in
            </Typography>
            <Box component="form" onSubmit={handleSubmit} noValidate className="login-form">
              <TextField
                margin="normal"
                required
                fullWidth
                id="email"
                label="Email Address"
                name="EMAIL"
                autoComplete="email"
                autoFocus
              />
              <TextField
                margin="normal"
                required
                fullWidth
                name="PASSWORD"
                label="Password"
                type="password"
                id="password"
                autoComplete="current-password"
              />
              <FormControlLabel
                control={<Checkbox value="remember" color="primary" />}
                label="Remember me"
              />
              <Button
                type="submit"
                fullWidth
                variant="contained"
                sx={{ mt: 3, mb: 2 }}
              >
                Sign In
              </Button>
              <Grid container>
                <Grid item xs>
                  <Link href="/forgot_password" variant="body2">
                    Forgot password?
                  </Link>
                </Grid>
                <Grid item>
                  <Link href="/signup" variant="body2">
                    Don't have an account? Sign Up
                  </Link>
                </Grid>
              </Grid>
            </Box>
          </Box>
        </Container>
      </Box>
    </ThemeProvider>
  );
}
