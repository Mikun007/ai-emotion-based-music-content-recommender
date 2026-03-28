import axios from "axios";

// const API = "https://ai-emotion-based-music-content-1fha.onrender.com";
const API = "https://ai-emotion-based-music-content-1fha.onrender.com";

export const detectEmotion = async (formData) => {
  return await axios.post(`${API}/detect`, formData);
};