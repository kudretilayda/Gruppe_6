import React, { useState, useEffect } from 'react';
import { fetchClothingItems } from '../services/api';
import ClothingItem from '../components/ClothingItem';

const WardrobePage = () => {
  const [clothingItems, setClothingItems] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadClothingItems = async () => {
      try {
        const data = await fetchClothingItems();
        setClothingItems(data);
      } catch (err) {
        setError('Error loading clothing items');
      }
    };

    loadClothingItems();
  }, []);

  return (
    <div>
      <h2>My Wardrobe</h2>
      {error && <p>{error}</p>}
      {clothingItems.map((item) => (
        <ClothingItem key={item.id} type={item.type} description={item.description} />
      ))}
    </div>
  );
};

export default WardrobePage;

// 2. version
// src/pages/WardrobePage.js
import React from 'react';
import Wardrobe from '../components/Wardrobe';

const WardrobePage = () => {
  return (
    <div>
      <h1>Welcome to Your Digital Wardrobe</h1>
      <Wardrobe />
    </div>
  );
};

export default WardrobePage;