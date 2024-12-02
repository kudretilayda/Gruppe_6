import React from "react";

const Oberteile = () => {
  return (
    <div className="w-[250px] border rounded-lg shadow-md p-4">
      <h3 className="text-xl font-semibold mb-2">Oberteil Name</h3>
      <img
        src="/api/placeholder/250/200"
        alt="Oberteil"
        className="w-full h-auto mb-4"
      />
      <p className="text-gray-500">Beschreibung des Oberteils</p>
    </div>
  );
};

export default Oberteile;
