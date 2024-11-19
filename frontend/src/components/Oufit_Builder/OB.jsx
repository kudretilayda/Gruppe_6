// src/components/OB.jsx
import React from "react";
import { useNavigate } from "react-router-dom";

const OutfitBuilder = () => {
  const navigate = useNavigate();

  const categories = [
    {
      id: 2,
      title: "Oberteile",
      description: "T-Shirts, Pullover und mehr",
      image:
        "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&h=300&fit=crop",
      styles: "border-2 border-blue-400 mb-6",
      path: "/oberteile",
    },
    {
      id: 3,
      title: "Schuhe",
      description: "Passende Schuhe für dein Outfit",
      image:
        "https://images.unsplash.com/photo-1549298916-b41d501d3772?w=400&h=300&fit=crop",
      styles: "border-2 border-red-400 mb-6",
      path: "/schuhe",
    },
    {
      id: 4,
      title: "Hosen",
      description: "Komfortable Hosen in verschiedenen Styles",
      image:
        "https://images.unsplash.com/photo-1542272604-787c3835535d?w=400&h=300&fit=crop",
      styles: "border-2 border-green-400 mb-6",
      path: "/hosen",
    },
  ];

  const handleClick = (path) => {
    navigate(path);
  };

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-3xl font-bold mb-8 text-center">
          Kleiderstücke verwalten
        </h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {categories.map((category) => (
            <div
              key={category.id}
              className={`bg-white rounded-lg shadow-lg overflow-hidden transform transition-transform duration-300 hover:scale-105 cursor-pointer ${category.styles}`}
            >
              <img
                src={category.image}
                alt={category.title}
                className="w-full h-48 object-cover"
              />
              <div className="p-4">
                <h2 className="text-xl font-semibold mb-2">{category.title}</h2>
                <p className="text-gray-600">{category.description}</p>
                <div className="mt-4">
                  <button
                    onClick={() => handleClick(category.path)}
                    className="inline-block bg-blue-100 text-blue-800 text-sm font-semibold px-3 py-1 rounded-full hover:bg-blue-200"
                  >
                    {`${category.title} ansehen`}
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default OutfitBuilder;
