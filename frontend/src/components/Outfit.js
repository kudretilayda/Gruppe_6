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

// 2. version

// src/components/Outfit.js
import React from 'react';

const Outfit = ({ name, clothingItems }) => {
  return (
    <div className="outfit" style={{ margin: '1rem 0', padding: '1rem', border: '1px solid #ddd', borderRadius: '8px' }}>
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