import React, { useState } from "react";
import { predict } from "../api";

const Predict = () => {
  const [provincia, setProvincia] = useState("");
  const [periods, setPeriods] = useState(30);
  const [predictions, setPredictions] = useState([]);
  const [error, setError] = useState("");

  const fetchPredictions = async () => {
    try {
      const data = await predict(provincia, periods);
      setPredictions(data);
      setError("");
    } catch (err) {
      setError("Error al realizar predicciones.");
    }
  };

  return (
    <div>
      <h2>Predicciones Energéticas</h2>
      <input
        type="text"
        placeholder="Provincia"
        value={provincia}
        onChange={(e) => setProvincia(e.target.value)}
      />
      <input
        type="number"
        placeholder="Períodos (días)"
        value={periods}
        onChange={(e) => setPeriods(Number(e.target.value))}
      />
      <button onClick={fetchPredictions}>Predecir</button>
      {error && <p>{error}</p>}
      {predictions.length > 0 && (
        <ul>
          {predictions.map((item, index) => (
            <li key={index}>
              Fecha: {item.ds}, Predicción: {item.yhat.toFixed(2)} (Rango:{" "}
              {item.yhat_lower.toFixed(2)} - {item.yhat_upper.toFixed(2)})
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Predict;
