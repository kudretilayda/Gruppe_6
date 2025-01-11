// src/pages/StylePage.js
import React, { useState, useEffect } from 'react';
import { fetchStyles } from '../services/api';
import Style from '../components/Style';

const StylePage = () => {
  const [styles, setStyles] = useState([]);

  useEffect(() => {
    const loadStyles = async () => {
      const data = await fetchStyles();
      setStyles(data);
    };

    loadStyles();
  }, []);

  return (
    <div>
      <h2>Meine Styles</h2>
      {styles.map((style) => (
        <Style key={style.id} name={style.name} />
      ))}
    </div>
  );
};

export default StylePage;