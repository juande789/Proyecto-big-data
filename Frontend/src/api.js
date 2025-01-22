import axios from "axios";

const BASE_URL = "http://localhost:8000"; // Asegúrate de que el backend está corriendo en este puerto

export const getStatistics = async (provincia) => {
  try {
      const response = await axios.get(`${BASE_URL}/estadisticas`, {
          params: { provincia },
      });
      return response.data;
  } catch (error) {
      console.error("Error fetching statistics:", error);
      throw error;
  }
};

export const predict = async (provincia, periods) => {
  try {
      const response = await axios.post(`${BASE_URL}/predict`, {
          provincia,
          periods,
      });
      return response.data;
  } catch (error) {
      console.error("Error predicting energy:", error);
      throw error;
  }
};


export const analyzeCluster = async (consumo, residentes, potencia) => {
  try {
    const response = await axios.post(`${BASE_URL}/analyze-cluster`, {
      consumo,
      residentes,
      potencia,
    });
    return response.data;
  } catch (error) {
    console.error("Error analyzing cluster:", error);
    throw error;
  }
};

