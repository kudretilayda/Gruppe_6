import React, { useState } from 'react';
import './Wardrobe.css';

const Wardrobe = () => {
  const [items, setItems] = useState([]);
  const [newItem, setNewItem] = useState({
    name: '',
    type: 'Oberteil', // Default Wert
  });

  const clothingTypes = [
    'Oberteil',
    'Hose',
    'Kleid',
    'Rock',
    'Jacke',
    'Schuhe',
    'Accessoire'
  ];

  const handleAddItem = (e) => {
    e.preventDefault();
    if (newItem.name.trim()) {
      setItems([...items, { ...newItem, id: Date.now() }]);
      setNewItem({ ...newItem, name: '' });
    }
  };

  const handleDeleteItem = (itemId) => {
    setItems(items.filter(item => item.id !== itemId));
  };

  return (
    <div className="wardrobe">
      <div className="wardrobe-header">
        <h2>Mein Kleiderschrank</h2>
        <form className="add-item-form" onSubmit={handleAddItem}>
          <input
            type="text"
            value={newItem.name}
            onChange={(e) => setNewItem({ ...newItem, name: e.target.value })}
            placeholder="Kleidungsstück hinzufügen"
            className="item-input"
          />
