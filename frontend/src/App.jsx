import { useState } from "react";
import WebcamCapture from "./components/WebCamCapture";
import EmotionDisplay from "./components/EmotionDisplay";
import MusicList from "./components/MusicList";
import { detectEmotion } from "./services/api";

function App() {
  const [emotion, setEmotion] = useState("");
  const [songs, setSongs] = useState([]);

  const handleCapture = async (formData) => {
    const res = await detectEmotion(formData);
    setEmotion(res.data.emotion);
    setSongs(res.data.songs);
  };

  return (
    <div>
      <h1>Emotion-Based Music Recommender</h1>

      <WebcamCapture onCapture={handleCapture} />

      <EmotionDisplay emotion={emotion} />

      <MusicList songs={songs} />
    </div>
  );
}

export default App;