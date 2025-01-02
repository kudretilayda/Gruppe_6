import React, { useState } from 'react';

// Beispiel für Style-Constraints
const initialConstraints = {
  color: ["Rot", "Blau", "Grün"], // erlaubte Farben
  fabric: ["Baumwolle", "Leinen"], // erlaubte Stoffe
  occasion: ["Business", "Casual"], // erlaubte Anlässe
  season: ["Sommer", "Winter"], // erlaubte Jahreszeiten
  balance: {
    maxColors: 3, // maximale Anzahl an Farben im Outfit
    minClothingItems: 2, // mindestanzahl an Kleidungsstücken
  },
};

const StyleConstraints = () => {
  const [constraints, setConstraints] = useState(initialConstraints);
  const [outfit, setOutfit] = useState([]); // Hier könnte das aktuelle Outfit gespeichert werden

  // Bewertungsfunktion für Outfits basierend auf den Constraints
  const evaluateOutfit = (outfit) => {
    let score = 0;

    // Bewertung der Farben im Outfit
    const colorsInOutfit = outfit.map(item => item.color);
    const matchingColors = colorsInOutfit.filter(color => constraints.color.includes(color)).length;
    score += matchingColors * 10;

    // Bewertung der Stoffe im Outfit
    const fabricsInOutfit = outfit.map(item => item.fabric);
    const matchingFabrics = fabricsInOutfit.filter(fabric => constraints.fabric.includes(fabric)).length;
    score += matchingFabrics * 5;

    // Bewertung des Anlasses
    const validOccasion = constraints.occasion.includes(outfit[0]?.occasion); // Annahme: Der Anlass wird für das gesamte Outfit gesetzt
    score += validOccasion ? 10 : 0;

    // Bewertung der Jahreszeit
    const validSeason = constraints.season.includes(outfit[0]?.season); // Annahme: Das Outfit gilt für eine Jahreszeit
    score += validSeason ? 5 : 0;

    // Balance Bewertung: Überprüfe, ob die Balancebedingungen erfüllt sind
    if (outfit.length >= constraints.balance.minClothingItems) score += 10;
    if (colorsInOutfit.length <= constraints.balance.maxColors) score += 10;

    return score; // Gibt die Punktzahl des Outfits zurück
  };

  // Funktion zum Hinzufügen eines Outfits
  const addOutfit = (newOutfit) => {
    setOutfit([...outfit, newOutfit]);
  };

  return (
    <div>
      <h2>Style Constraints</h2>

      {/* Beispiel eines Outfits hinzufügen */}
      <button onClick={() => addOutfit({ color: "Blau", fabric: "Baumwolle", occasion: "Casual", season: "Sommer" })}>
        Outfit Hinzufügen
      </button>

      <h3>Aktuelles Outfit Bewertung:</h3>
      <p>Punktzahl: {evaluateOutfit(outfit)}</p>

      <div>
        <h3>Aktuelle Constraints</h3>
        <ul>
          <li>Farben: {constraints.color.join(', ')}</li>
          <li>Stoffe: {constraints.fabric.join(', ')}</li>
          <li>Anlässe: {constraints.occasion.join(', ')}</li>
          <li>Jahreszeiten: {constraints.season.join(', ')}</li>
          <li>Balance: Max Farben {constraints.balance.maxColors}, Min Kleidungsstücke {constraints.balance.minClothingItems}</li>
        </ul>
      </div>
    </div>
  );
};

export default StyleConstraints;
