import React from "react";

const Schuhe = () => {
  return (
    <div className="w-[250px] border rounded-lg shadow-md p-4">
      <h3 className="text-xl font-semibold mb-2">Schuh Name</h3>
      <img
        src="/api/placeholder/250/200"
        alt="Schuh"
        className="w-full h-auto mb-4"
      />
      <p className="text-gray-500">Beschreibung des Schuhs</p>
    </div>
  );
};

export default Schuhe;
