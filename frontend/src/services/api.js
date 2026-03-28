import axios from "axios";

const API = "http://localhost:5000";
// const API = "https://ai-emotion-based-music-content-1fha.onrender.com";

export const detectEmotion = async (formData) => {
  return await axios.post(`${API}/detect`, formData);
};