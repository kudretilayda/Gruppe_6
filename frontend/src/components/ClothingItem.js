// src/components/Kleidungsstueck.js
import React from 'react';

const Kleidungsstueck = ({ typ, bezeichnung }) => {
  return (
    <div className="kleidungsstueck">
      <h3>{bezeichnung}</h3>
      <p>Typ: {typ}</p>
    </div>
  );
};

export default Kleidungsstueck;