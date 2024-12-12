// src/pages/OutfitPage.js
import React, { useState, useEffect } from 'react';
import { fetchOutfits } from '../services/api';
import Outfit from '../components/Outfit';

const OutfitPage = () => {
  const [outfits, setOutfits] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadOutfits = async () => {
      try {
        const data = await fetchOutfits();
        setOutfits(data);
      } catch (err) {
        setError('Fehler beim Laden der Outfits');
      } finally {
        setLoading(false);
      }
    };

    loadOutfits();
  }, []);

  return (
    <div>
      <h2>Meine Outfits</h2>
      {loading && <p>Lädt...</p>}
      {error && <p>{error}</p>}
      {!loading && !error && outfits.map((outfit) => (
        <Outfit key={outfit.id} name={outfit.name} kleidungsstuecke={outfit.kleidungsstuecke} />
      ))}
    </div>
  );
};

export default OutfitPage;