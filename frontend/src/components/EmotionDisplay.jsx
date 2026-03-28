const EmotionDisplay = ({ emotion }) => {
  return <div className={`emotion-box ${emotion}`}>
            <h2>🧠 {emotion.toUpperCase()}</h2>
            <p>Music based on your mood</p>
          </div>
};

export default EmotionDisplay;