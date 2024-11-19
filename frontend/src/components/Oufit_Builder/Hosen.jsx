import React from "react";

const Hosen = () => {
  return (
    <div className="w-[250px] border rounded-lg shadow-md p-4">
      <h3 className="text-xl font-semibold mb-2">Hosen Name</h3>
      <img
        src="/api/placeholder/250/200"
        alt="Hosen"
        className="w-full h-auto mb-4"
      />
      <p className="text-gray-500">Beschreibung der Hosen</p>
    </div>
  );
};

export default Hosen;
