import React, { useState } from 'react';
import { Grid, Button } from '@material-ui/core';
import OutfitCreateDialog from '../dialogs/OutfitCreateDialog';

export default function OutfitPage() {
  const [isCreateDialogOpen, setCreateDialogOpen] = useState(false);

  return (
    <div>
      <Button
        variant="contained"
        color="primary"
        onClick={() => setCreateDialogOpen(true)}
      >
        Neues Outfit erstellen
      </Button>

      <OutfitCreateDialog
        open={isCreateDialogOpen}
        onClose={() => setCreateDialogOpen(false)}
      />
    </div>
  );
}
