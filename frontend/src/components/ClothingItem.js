// src/components/ClothingItem.js
import React from 'react';

const ClothingItem = ({ type, description }) => {
  return (
    <div className="clothing-item">
      <h3>{description}</h3>
      <p>Type: {type}</p>
    </div>
  );
};

export default ClothingItem;
