import axios from "axios";

// const API = "http://localhost:7860";
// const API = "https://ai-emotion-based-music-content-1fha.onrender.com";
// const API = "https://Budhadev-emotion-based-music-recomendor.hf.space";
const API = window.location.origin;

export const detectEmotion = async (formData) => {
  return await axios.post(`${API}/detect`, formData);
};