import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import Statistics from "./components/Statistics";
import Predict from "./components/Predict";
import ClusterAnalysis from "./components/ClusterAnalysis";
import "./App.css";
import logo from './ECOPENGUIN.png'; // Importa el logo

const App = () => {
  return (
    <Router>
      <div className="App">
        {/* Encabezado */}
        <header className="App-header">
          <img src={logo} alt="EcoPenguin Logo" className="App-logo" />
          <h1>EcoPenguin Dashboard</h1>
        </header>

        {/* Rutas */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/statistics" element={<Statistics />} />
          <Route path="/predict" element={<Predict />} />
          <Route path="/cluster-analysis" element={<ClusterAnalysis />} />
        </Routes>

        {/* Footer */}
        <footer>
          <p>© 2025 EcoPenguin. Todos los derechos reservados.</p>
        </footer>
      </div>
    </Router>
  );
};

export default App;
