// src/components/Wardrobe.js
import React, { useState, useEffect } from 'react';
import { fetchClothingItems } from '../services/api';
import ClothingItem from './ClothingItem';

const Wardrobe = () => {
  const [clothingItems, setClothingItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadClothingItems = async () => {
      try {
        const data = await fetchClothingItems();
        setClothingItems(data);
      } catch (err) {
        setError('Error loading clothing items');
      } finally {
        setLoading(false);
      }
    };

    loadClothingItems();
  }, []);

  return (
    <div>
      <h2>My Wardrobe</h2>
      {loading && <p>Loading...</p>}
      {error && <p>{error}</p>}
      {!loading && !error && clothingItems.map((item) => (
        <ClothingItem key={item.id} type={item.type} name={item.name} />
      ))}
    </div>
  );
};

export default Wardrobe;

//2. version

// src/components/Wardrobe.js
import React, { useState, useEffect } from 'react';
import ClothingItem from './ClothingItem';
import Outfit from './Outfit';

const Wardrobe = () => {
  const [clothingItems, setClothingItems] = useState([]);
  const [outfits, setOutfits] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch data from API (mocked for now)
    const fetchWardrobeData = async () => {
      try {
        // Replace with actual API calls
        const clothingData = [
          { id: 1, type: 'Shirt', description: 'Blue Shirt' },
          { id: 2, type: 'Pants', description: 'Black Jeans' },
        ];
        const outfitData = [
          { id: 1, name: 'Casual Outfit', items: ['Blue Shirt', 'Black Jeans'] },
        ];

        setClothingItems(clothingData);
        setOutfits(outfitData);
      } catch (err) {
        setError('Error fetching wardrobe data.');
      }
    };

    fetchWardrobeData();
  }, []);

  return (
    <div>
      <h1>My Wardrobe</h1>
      {error && <p>{error}</p>}

      <section>
        <h2>Clothing Items</h2>
        <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
          {clothingItems.map((item) => (
            <ClothingItem
              key={item.id}
              type={item.type}
              description={item.description}
            />
          ))}
        </div>
      </section>

      <section>
        <h2>Outfits</h2>
        {outfits.map((outfit) => (
          <Outfit key={outfit.id} name={outfit.name} clothingItems={outfit.items} />
        ))}
      </section>
    </div>
  );
};

export default Wardrobe;
