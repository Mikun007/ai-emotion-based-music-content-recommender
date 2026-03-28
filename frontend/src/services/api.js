import axios from "axios";

const API = "http://localhost:5000";

export const detectEmotion = async (formData) => {
  return await axios.post(`${API}/detect`, formData);
};