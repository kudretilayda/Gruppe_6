// src/pages/WardrobePage.js
import React, { useState, useEffect } from 'react';
import {
  Typography,
  Button,
  Grid,
  Card,
  CardContent,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  Select,
  MenuItem,
  FormControl,
  InputLabel
} from '@mui/material';

const WardrobePage = () => {
  const [items, setItems] = useState([]);
  const [openDialog, setOpenDialog] = useState(false);
  const [newItem, setNewItem] = useState({
    type: '',
    description: '',
    usage: ''
  });

  const handleAddItem = () => {
    setItems([...items, newItem]);
    setOpenDialog(false);
    setNewItem({ type: '', description: '', usage: '' });
  };

  return (
    <div className="p-4">
      <Grid container spacing={3} alignItems="center" className="mb-4">
        <Grid item xs>
          <Typography variant="h4">Mein Kleiderschrank</Typography>
        </Grid>
        <Grid item>
          <Button
            variant="contained"
            color="primary"
            onClick={() => setOpenDialog(true)}
          >
            Kleidungsstück hinzufügen
          </Button>
        </Grid>
      </Grid>

      <Grid container spacing={3}>
        {items.map((item, index) => (
          <Grid item xs={12} sm={6} md={4} key={index}>
            <Card>
              <CardContent>
                <Typography variant="h6">{item.type}</Typography>
                <Typography color="textSecondary">{item.description}</Typography>
                <Typography>Verwendung: {item.usage}</Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>

      <Dialog open={openDialog} onClose={() => setOpenDialog(false)}>
        <DialogTitle>Neues Kleidungsstück hinzufügen</DialogTitle>
        <DialogContent>
          <FormControl fullWidth margin="normal">
            <InputLabel>Typ</InputLabel>
            <Select
              value={newItem.type}
              onChange={(e) => setNewItem({...newItem, type: e.target.value})}
            >
              <MenuItem value="Hose">Hose</MenuItem>
              <MenuItem value="Shirt">Shirt</MenuItem>
              <MenuItem value="Jacke">Jacke</MenuItem>
              <MenuItem value="Schuhe">Schuhe</MenuItem>
            </Select>
          </FormControl>
          <TextField
            fullWidth
            margin="normal"
            label="Beschreibung"
            value={newItem.description}
            onChange={(e) => setNewItem({...newItem, description: e.target.value})}
          />
          <TextField
            fullWidth
            margin="normal"
            label="Verwendung"
            value={newItem.usage}
            onChange={(e) => setNewItem({...newItem, usage: e.target.value})}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenDialog(false)}>Abbrechen</Button>
          <Button onClick={handleAddItem} color="primary">Hinzufügen</Button>
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default WardrobePage;