import React, { useState, useEffect } from 'react';
import {
  Typography,
  Grid,
  Card,
  CardContent,
  Button,
  TextField,
  Chip,
  CardActions,
  IconButton,
  Box,
  Container
} from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';

const Styles = () => {
  const [styles, setStyles] = useState([]);
  const [newStyle, setNewStyle] = useState({
    name: '',
    features: [],
    constraints: []
  });

  // Load saved styles on initialization
  useEffect(() => {
    const saved = localStorage.getItem('styles');
    if (saved) {
      setStyles(JSON.parse(saved));
    }
  }, []);

  const handleSaveStyle = () => {
    const updated = [...styles, newStyle];
    setStyles(updated);

    // Save updated list to localStorage
    localStorage.setItem('styles', JSON.stringify(updated));
    setNewStyle({ name: '', features: [], constraints: [] });
  };

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Style erstellen
      </Typography>
      <Grid container spacing={3} justifyContent="center">
        <Grid item xs={12} md={8}>
          <TextField
            fullWidth
            margin="normal"
            label="Style Name"
            value={newStyle.name}
            onChange={(e) => setNewStyle({ ...newStyle, name: e.target.value })}
            placeholder="Style Name"
          />
        </Grid>
        <Grid item xs={12} md={8}>
          <Grid container spacing={2}>
            <Grid item xs={4}>
              <Button
                variant="outlined"
                fullWidth
                style={{
                  backgroundColor: '#fff3f3',
                  color: '#d32f2f',
                  fontWeight: 'bold'
                }}
              >
                Mutex Constraint
              </Button>
            </Grid>
            <Grid item xs={4}>
              <Button
                variant="outlined"
                fullWidth
                style={{
                  backgroundColor: '#f3f4ff',
                  color: '#303f9f',
                  fontWeight: 'bold'
                }}
              >
                Implikation Constraint
              </Button>
            </Grid>
            <Grid item xs={4}>
              <Button
                variant="outlined"
                fullWidth
                style={{
                  backgroundColor: '#f3fff3',
                  color: '#388e3c',
                  fontWeight: 'bold'
                }}
              >
                Kardinalität Constraint
              </Button>
            </Grid>
          </Grid>
        </Grid>
        <Grid item xs={12} md={8}>
          <Typography variant="subtitle1" gutterBottom>
            Hinzugefügte Constraints
          </Typography>
          <Card
            variant="outlined"
            style={{
              padding: '10px',
              backgroundColor: '#f5f5f5',
              minHeight: '100px'
            }}
          >
            {newStyle.constraints.length === 0 ? (
              <Typography color="textSecondary" align="center">
                Sie haben noch keine Constraints hinzugefügt.
              </Typography>
            ) : (
              newStyle.constraints.map((constraint, index) => (
                <Chip
                  key={index}
                  label={constraint}
                  style={{ margin: '5px' }}
                />
              ))
            )}
          </Card>
        </Grid>
        <Grid item xs={12} md={8}>
          <Button
            variant="contained"
            color="primary"
            fullWidth
            onClick={handleSaveStyle}
          >
            Style Speichern
          </Button>
        </Grid>
      </Grid>
      <Box mt={5}>
        <Typography variant="h5" gutterBottom>
          Vorhandene Styles
        </Typography>
        <Grid container spacing={2}>
          {styles.map((style, index) => (
            <Grid item xs={12} sm={6} md={4} key={index}>
              <Card elevation={3}>
                <CardContent>
                  <Typography variant="h6">{style.name}</Typography>
                  <Box display="flex" flexWrap="wrap" marginTop={1}>
                    {style.features.map((feature, i) => (
                      <Chip
                        key={i}
                        label={feature}
                        style={{
                          margin: '5px',
                          backgroundColor: '#e0e0e0'
                        }}
                      />
                    ))}
                  </Box>
                </CardContent>
                <CardActions>
                  <IconButton
                    color="primary"
                    onClick={() => console.log('Edit not yet implemented')}
                  >
                    <EditIcon />
                  </IconButton>
                  <IconButton
                    color="secondary"
                    onClick={() => {
                      const updated = styles.filter((_, i) => i !== index);
                      setStyles(updated);
                      localStorage.setItem('styles', JSON.stringify(updated));
                    }}
                  >
                    <DeleteIcon />
                  </IconButton>
                </CardActions>
              </Card>
            </Grid>
          ))}
        </Grid>
      </Box>
    </Container>
  );
};

export default Styles;
