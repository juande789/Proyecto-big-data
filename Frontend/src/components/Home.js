import React from "react";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div>
      <h1>Bienvenido a EcoPenguin</h1>
      <p>Seleccione una de las opciones:</p>
      <ul>
        <li><Link to="/predict">Predicciones Energéticas</Link></li>
        <li><Link to="/statistics">Estadísticas Generales</Link></li>
        <li><Link to="/cluster-analysis">Análisis de Clustering</Link></li> {/* Nuevo enlace */}
      </ul>
    </div>
  );
};

export default Home;
