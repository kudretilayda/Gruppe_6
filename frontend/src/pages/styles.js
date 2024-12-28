// src/pages/StylesPage.js
import React, { useState } from 'react';
import {
  Typography,
  Grid,
  Card,
  CardContent,
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  Chip
} from '@mui/material';

const StylesPage = () => {
  const [styles, setStyles] = useState([]);
  const [openDialog, setOpenDialog] = useState(false);
  const [newStyle, setNewStyle] = useState({
    name: '',
    description: '',
    features: []
  });

  const handleAddStyle = () => {
    setStyles([...styles, newStyle]);
    setOpenDialog(false);
    setNewStyle({ name: '', description: '', features: [] });
  };

  return (
    <div className="p-4">
      <Grid container spacing={3} alignItems="center" className="mb-4">
        <Grid item xs>
          <Typography variant="h4">Meine Styles</Typography>
        </Grid>
        <Grid item>
          <Button
            variant="contained"
            color="primary"
            onClick={() => setOpenDialog(true)}
          >
            Style erstellen
          </Button>
        </Grid>
      </Grid>

      <Grid container spacing={3}>
        {styles.map((style, index) => (
          <Grid item xs={12} sm={6} md={4} key={index}>
            <Card>
              <CardContent>
                <Typography variant="h6">{style.name}</Typography>
                <Typography color="textSecondary" paragraph>
                  {style.description}
                </Typography>
                {style.features.map((feature, i) => (
                  <Chip
                    key={i}
                    label={feature}
                    style={{ margin: '0.25rem' }}
                  />
                ))}
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>

      <Dialog open={openDialog} onClose={() => setOpenDialog(false)}>
        <DialogTitle>Neuen Style erstellen</DialogTitle>
        <DialogContent>
          <TextField
            fullWidth
            margin="normal"
            label="Name"
            value={newStyle.name}
            onChange={(e) => setNewStyle({...newStyle, name: e.target.value})}
          />
          <TextField
            fullWidth
            margin="normal"
            label="Beschreibung"
            multiline
            rows={3}
            value={newStyle.description}
            onChange={(e) => setNewStyle({...newStyle, description: e.target.value})}
          />
          <TextField
            fullWidth
            margin="normal"
            label="Features (kommagetrennt)"
            value={newStyle.features.join(', ')}
            onChange={(e) => setNewStyle({
              ...newStyle,
              features: e.target.value.split(',').map(f => f.trim())
            })}
            helperText="z.B.: casual, business, sportlich"
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenDialog(false)}>Abbrechen</Button>
          <Button onClick={handleAddStyle} color="primary">Erstellen</Button>
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default StylesPage;