import React from 'react';

const OutfitList = ({ outfits }) => {
  return (
    <div>
      {outfits.map((outfit, index) => (
        <div key={index}>
          <h3>{outfit.type}</h3>
          <p>Größe: {outfit.size}</p>
          <p>Farbe: {outfit.color}</p>
          {outfit.shoeSize && <p>Schuhgröße: {outfit.shoeSize}</p>}
          {outfit.cupSize && <p>Körbchengröße: {outfit.cupSize}</p>}
          {outfit.bandSize && <p>Bandgröße: {outfit.bandSize}</p>}
        </div>
      ))}
    </div>
  );
};

export default OutfitList;
