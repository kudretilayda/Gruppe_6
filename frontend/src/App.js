import React, { useState } from 'react';
import './App.css';

const App = () => {
  const [currentPage, setCurrentPage] = useState('home');

  const renderContent = () => {
    switch(currentPage) {
      case 'wardrobe':
        return (
          <div className="content-container">
            <h2>Mein Kleiderschrank</h2>
          </div>
        );
      case 'styles':
        return (
          <div className="content-container">
            <h2>Styles</h2>
          </div>
        );
      case 'outfits':
        return (
          <div className="content-container">
            <h2>Outfits</h2>
          </div>
        );
      default:
        return (
          <div className="content-container">
            <div className="welcome-message">
              <h2>Willkommen im Digitalen Kleiderschrank</h2>
              <p>
                Verwalten Sie Ihre Kleidung, erstellen Sie Styles und lassen Sie sich
                passende Outfits vorschlagen.
              </p>
            </div>
          </div>
        );
    }
  };
return (
    <div className="app">
      <header className="app-header">
        <nav className="nav-container">
          <h1 className="app-title">Digitaler Kleiderschrank</h1>
          <div className="nav-buttons">
            <button
              className={`nav-button ${currentPage === 'home' ? 'active' : ''}`}
              onClick={() => setCurrentPage('home')}
            >
              Home
            </button>
            <button
              className={`nav-button ${currentPage === 'wardrobe' ? 'active' : ''}`}
              onClick={() => setCurrentPage('wardrobe')}
            >
              Kleiderschrank
            </button>
            <button
              className={`nav-button ${currentPage === 'styles' ? 'active' : ''}`}
              onClick={() => setCurrentPage('styles')}
            >
              Styles
            </button>
            <button
              className={`nav-button ${currentPage === 'outfits' ? 'active' : ''}`}
              onClick={() => setCurrentPage('outfits')}
            >
              Outfits
            </button>
          </div>
        </nav>
      </header>

      <main className="main-content">
        {renderContent()}
      </main>
    </div>
  );
};

export default App;
