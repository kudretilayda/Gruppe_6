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

// 2. version
// src/components/ClothingItem.js
import React from 'react';

const ClothingItem = ({ type, description }) => {
  return (
    <div className="clothing-item" style={{ border: '1px solid #ccc', padding: '1rem', borderRadius: '8px' }}>
      <h3>{description}</h3>
      <p>Type: {type}</p>
    </div>
  );
};