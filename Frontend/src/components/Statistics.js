import React, { useState } from "react";
import { getStatistics } from "../api";

const Statistics = () => {
  const [provincia, setProvincia] = useState("");
  const [statistics, setStatistics] = useState(null);
  const [error, setError] = useState("");

  const fetchStatistics = async () => {
    try {
      const data = await getStatistics(provincia);
      setStatistics(data);
      setError("");
    } catch (err) {
      setError("Error al obtener las estadísticas.");
    }
  };

  return (
    <div>
      <h2>Estadísticas Generales</h2>
      <input
        type="text"
        placeholder="Provincia"
        value={provincia}
        onChange={(e) => setProvincia(e.target.value)}
      />
      <button onClick={fetchStatistics}>Obtener Estadísticas</button>
      {error && <p>{error}</p>}
      {statistics && (
        <div>
          <p>Media: {statistics.media}</p>
          <p>Moda: {statistics.moda}</p>
          <p>Varianza: {statistics.varianza}</p>
        </div>
      )}
    </div>
  );
};

export default Statistics;
