import React, { useState } from 'react';
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  TextField,
  Select,
  MenuItem,
  FormControl,
  InputLabel
} from '@material-ui/core';
import { kleiderschrankService } from '../api/kleiderschrankService';

export default function KleidungAddDialog({ open, onClose, onSave }) {
  const [formData, setFormData] = useState({
    bezeichnung: '',
    typ_id: '',
  });

  const handleSave = async () => {
    try {
      await kleiderschrankService.addKleidungsstueck(formData);
      onSave();
      onClose();
    } catch (error) {
      console.error('Fehler beim Speichern:', error);
    }
  };

  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>Neues Kleidungsstück hinzufügen</DialogTitle>
      <DialogContent>
        <TextField
          autoFocus
          margin="dense"
          label="Bezeichnung"
          fullWidth
          value={formData.bezeichnung}
          onChange={(e) => setFormData({...formData, bezeichnung: e.target.value})}
        />
        {/* Weitere Formularfelder */}
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} color="primary">
          Abbrechen
        </Button>
        <Button onClick={handleSave} color="primary">
          Speichern
        </Button>
      </DialogActions>
    </Dialog>
  );
}