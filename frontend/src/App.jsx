import { useState, useEffect } from "react";
import WebcamCapture from "./components/WebCamCapture";
import EmotionDisplay from "./components/EmotionDisplay";
import MusicList from "./components/MusicList";
import { detectEmotion } from "./services/api";
import Login from "./pages/Login";   // 👈 add this
import "./App.css"
import "./index.css"

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false); // 👈 new
  const [emotion, setEmotion] = useState("");
  const [songs, setSongs] = useState([]);

  // 👇 check login on refresh
  useEffect(() => {
    const user = localStorage.getItem("isLoggedIn");
    if (user === "true") setIsLoggedIn(true);
  }, []);

  const handleCapture = async (formData) => {
    const res = await detectEmotion(formData);
    setEmotion(res.data.emotion);
    setSongs(res.data.songs);
  };

  // 👇 if NOT logged in → show login page
  if (!isLoggedIn) {
    return <Login setIsLoggedIn={setIsLoggedIn} />;
  }

  // 👇 your original UI (unchanged)
  return (
    <div>
      <h1>Emotion-Based Music Recommender</h1>

      {/* optional logout */}
      <button
        className="logout-btn"
        onClick={() => {
          localStorage.removeItem("isLoggedIn");
          setIsLoggedIn(false);
        }}
      >
        Logout
      </button>

      <WebcamCapture onCapture={handleCapture} />

      <EmotionDisplay emotion={emotion} />

      <MusicList songs={songs} />
    </div>
  );
}

export default App;