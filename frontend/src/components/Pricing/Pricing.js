import React from 'react';
import './PricingTable.css'; // Stelle sicher, dass du die CSS-Datei importierst

const PricingTable = () => {
  return (
    <div className="pricing-container">
      <h2 className="pricing-title">Benutzer Dashboard</h2>
      <p className="pricing-description">Wählen Sie den Plan, der am besten zu Ihnen passt.</p>
      
      <div className="pricing-cards">
        {/* Free Plan */}
        <div className="pricing-card">
          <h3 className="plan-title">Outfit erstellen</h3>
          <p className="plan-description">Schön, dass du hier bist! Passe dein Dashboard an und starte direkt durch. Viel Spaß beim Entdecken!</p>
          
         
          <button className="buy-button">Jetzt starten</button>
        </div>

        {/* Basic Plan */}
        <div className="pricing-card">
          <h3 className="plan-title">Outfit anzeigen</h3>
          <p className="plan-description">Perfekt, um deine Outfits zu präsentieren und mit anderen zu teilen – ideal für Modeblogger, Stylisten oder alle, die ihre Outfit-Inspirationen zeigen möchten.</p>
          
          <button className="buy-button">Jetzt starten</button>
        </div>

        {/* Premium Plan */}
        <div className="pricing-card">
          <h3 className="plan-title">Outfit bearbeiten</h3>
          <p className="plan-description">Ideal für Designer und Modestudenten, die ihre Outfits kreativ anpassen und mit verschiedenen Stilen experimentieren möchten. Erstelle, bearbeite und optimiere deine Outfits nach deinen Wünschen.</p>
          
          <button className="buy-button">Jetzt starten</button>
        </div>
      </div>
    </div>
  );
};

export default PricingTable;
