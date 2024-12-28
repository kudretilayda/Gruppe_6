import React, { useState } from 'react';
import { Box, Typography } from '@mui/material';
import WardrobeList from './WardrobeList'; // Komponente für die Liste der Kleidungsstücke
import ClothingItemForm from './ClothingItemForm'; // Formular für das Hinzufügen neuer Kleidungsstücke
import StyleList from "../styles/StyleList";
import OutfitList from "../outfits/OutfitList";
import OutfitCreator from "../outfits/OutfitCreator";

const Wardrobe = () => {
  // Zustand, der die Liste der Kleidungsstücke speichert
  const [items, setItems] = useState([
    { type: 'T-Shirt', usage: 'Freizeit' },
    { type: 'Anzug', usage: 'Arbeit' },
    { type: 'Laufschuhe', usage: 'Sport' },
  ]);

  // Funktion zum Hinzufügen eines neuen Kleidungsstücks
  const handleAddItem = (newItem) => {
    setItems ((prevItems) => [...prevItems, item]);
  };

  return (
    <Box p={3}>
      <Typography variant="h4" gutterBottom>
        Mein Kleiderschrank
      </Typography>
      <ClothingItemForm onAddItem={handleAddItem} />
      <WardrobeList items={items} />
    </Box>
  );
};

export default Wardrobe;