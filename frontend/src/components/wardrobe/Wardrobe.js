import React, { useState } from 'react';
import WardrobeList from './WardrobeList'; // Komponente für die Liste der Kleidungsstücke
import ClothingItemForm from './ClothingItemForm'; // Formular für das Hinzufügen neuer Kleidungsstücke

const Wardrobe = () => {
  // Zustand, der die Liste der Kleidungsstücke speichert
  const [items, setItems] = useState([
    { type: 'T-Shirt', usage: 'Freizeit' },
    { type: 'Anzug', usage: 'Arbeit' },
    { type: 'Laufschuhe', usage: 'Sport' },
  ]);

  // Funktion zum Hinzufügen eines neuen Kleidungsstücks
  const handleAddItem = (newItem) => {
    setItems([...items, newItem]);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Meine Garderobe</h1>

      {/* Formular zum Hinzufügen eines neuen Kleidungsstücks */}
      <ClothingItemForm onAddItem={handleAddItem} />

      {/* Liste der Kleidungsstücke */}
      <WardrobeList items={items} />
    </div>
  );
};

export default Wardrobe;
