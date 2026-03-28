import axios from "axios";

const API = "https://ai-emotion-based-music-content-uqhq.onrender.com";

export const detectEmotion = async (formData) => {
  return await axios.post(`${API}/detect`, formData);
};