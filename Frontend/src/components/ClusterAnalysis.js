import React, { useState } from "react";
import { analyzeCluster } from "../api";

const ClusterAnalysis = () => {
  const [consumo, setConsumo] = useState("");
  const [residentes, setResidentes] = useState("");
  const [potencia, setPotencia] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleAnalyze = async () => {
    try {
      const data = await analyzeCluster(
        parseFloat(consumo),
        parseFloat(residentes),
        parseFloat(potencia)
      );
      setResult(data);
      setError("");
    } catch (err) {
      setError("Error al analizar el cluster.");
    }
  };

  return (
    <div>
      <h2>Análisis de Clustering</h2>
      <input
        type="number"
        placeholder="Consumo energético (kWh/m²)"
        value={consumo}
        onChange={(e) => setConsumo(e.target.value)}
      />
      <input
        type="number"
        placeholder="Media de residentes"
        value={residentes}
        onChange={(e) => setResidentes(e.target.value)}
      />
      <input
        type="number"
        placeholder="Potencia contratada (kW)"
        value={potencia}
        onChange={(e) => setPotencia(e.target.value)}
      />
      <button onClick={handleAnalyze}>Analizar</button>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {result && (
        <div>
          <p><strong>Cluster:</strong> {result.cluster}</p>
          <p><strong>Recomendación:</strong> {result.recomendacion}</p>
        </div>
      )}
    </div>
  );
};

export default ClusterAnalysis;
