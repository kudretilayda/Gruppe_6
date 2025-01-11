import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div>
      <h1>Willkommen zu deinem digitalen Kleiderschrank</h1>
      <p>Verwalte deine Kleidung, Styles und Outfits einfach und effizient.</p>
      <nav>
        <ul>
          <li><Link to="/wardrobe">Kleiderschrank</Link></li>
          <li><Link to="/styles">Styles</Link></li>
          <li><Link to="/outfits">Outfits</Link></li>
        </ul>
      </nav>
    </div>
  );
};

export default Home;