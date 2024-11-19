import React, { useState, useEffect } from 'react';
import { Grid, Button } from '@material-ui/core';
import { kleiderschrankService } from '../api/kleiderschrankService';
import KleidungAddDialog from '../dialogs/KleidungAddDialog';

export default function KleiderschrankPage() {
  const [kleidung, setKleidung] = useState([]);
  const [isAddDialogOpen, setAddDialogOpen] = useState(false);

  useEffect(() => {
    loadKleidung();
  }, []);

  const loadKleidung = async () => {
    try {
      const data = await kleiderschrankService.getKleidungsstuecke();
      setKleidung(data);
    } catch (error) {
      console.error('Fehler beim Laden der Kleidungsstücke:', error);
    }
  };

  return (
    <div>
      <Button
        variant="contained"
        color="primary"
        onClick={() => setAddDialogOpen(true)}
      >
        Kleidungsstück hinzufügen
      </Button>

      <Grid container spacing={3}>
        {kleidung.map((item) => (
          <Grid item xs={12} sm={6} md={4} key={item.id}>
            <KleidungCard kleidungsstueck={item} />
          </Grid>
        ))}
      </Grid>

      <KleidungAddDialog
        open={isAddDialogOpen}
        onClose={() => setAddDialogOpen(false)}
        onSave={loadKleidung}
      />
    </div>
  );
}