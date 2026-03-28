import React, { useRef } from "react";
import Webcam from "react-webcam";

const WebcamCapture = ({ onCapture }) => {
  const webcamRef = useRef(null);

  const capture = async () => {
    // 1. Safety check: Ensure the webcam is mounted and ready
    if (!webcamRef.current) return;

    const imageSrc = webcamRef.current.getScreenshot();
    
    // 2. Check if the screenshot was actually taken (can be null if camera is off)
    if (!imageSrc) {
      console.error("Camera stream not available yet.");
      return;
    }

    const blob = await fetch(imageSrc).then(res => res.blob());
    const formData = new FormData();
    formData.append("image", blob, "capture.jpg");

    onCapture(formData);
  };

  return (
    <div className="webcam-container">
      {/* ADDED: ref={webcamRef} and screenshotFormat */}
      <Webcam 
        audio={false}
        ref={webcamRef} 
        className="webcam" 
        screenshotFormat="image/jpeg"
      />
      <div>
        <button onClick={capture} className="btn btn-light">
          Detect Emotion
        </button>
      </div>
    </div>
  );
};

export default WebcamCapture;
