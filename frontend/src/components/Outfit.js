// src/components/Outfit.js
import React from 'react';

const Outfit = ({ name, kleidungsstuecke }) => {
  return (
    <div className="outfit">
      <h3>{name}</h3>
      <ul>
        {kleidungsstuecke.map((ks, index) => (
          <li key={index}>{ks}</li>
        ))}
      </ul>
    </div>
  );
};

export default Outfit;