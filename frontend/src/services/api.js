import axios from "axios";

const API = "http://ai-emotion-based-music-content-recommender.onrender.com";

export const detectEmotion = async (formData) => {
  return await axios.post(`${API}/detect`, formData);
};