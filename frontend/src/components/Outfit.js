// src/components/Outfit.js
import React from 'react';

const Outfit = ({ name, clothingItems }) => {
  return (
    <div className="outfit">
      <h3>{name}</h3>
      <ul>
        {clothingItems.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
};

export default Outfit;
