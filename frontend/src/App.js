// React + hooks
import React, { useState } from "react";
//  HTTP client to talk to Flask backend
import axios from "axios";

//  Base URL of your Flask API – change here if needed
const API_URL = "http://127.0.0.1:5000";

export default function App() {
  const [userId, setUserId] = useState("");
  const [mode, setMode] = useState("save");      // "save" or "verify"
  const [result, setResult] = useState("");

  // Simulate EEG data for MVP demo
  const generateEEG = () => {
    // 256 samples × 8 channels random data
    return Array.from({ length: 256 }, () =>
      Array.from({ length: 8 }, () => Math.random())
    );
  };

  const handleSubmit = async () => {
    try {
      const eeg = generateEEG();

      if (mode === "save") {
        // POST to Flask route /save
        await axios.post(`${API_URL}/api/save`, {
          user_id: Number(userId),
          eeg
        });
        setResult("Neural key saved successfully ✅");
      } else {
        // POST to Flask route /verify
        const res = await axios.post(`${API_URL}/api/verify`, {
          user_id: Number(userId),
          eeg
        });
        // Expecting Flask to return JSON like { match: 1|0|-1 }
        const { match } = res.data;
        if (match === 1) setResult("Access Granted ✅");
        else if (match === 0) setResult("Access Denied ❌");
        else setResult("User Not Found ⚠️");
      }
    } catch (err) {
      console.error(err);
      setResult("Server error");
    }
  };

  return (
    <div style={{ fontFamily: "sans-serif", textAlign: "center", marginTop: 40 }}>
      <h1>NeuroShield MVP</h1>

      {/*  User ID input */}
      <div style={{ marginBottom: 20 }}>
        <label>User ID: </label>
        <input
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          type="number"
          style={{ padding: "4px 8px" }}
        />
      </div>

      {/*  Mode selector (save or verify) */}
      <div style={{ marginBottom: 20 }}>
        <label>
          <input
            type="radio"
            checked={mode === "save"}
            onChange={() => setMode("save")}
          />{" "}
          Save Key
        </label>
        <label style={{ marginLeft: 20 }}>
          <input
            type="radio"
            checked={mode === "verify"}
            onChange={() => setMode("verify")}
          />{" "}
          Verify Key
        </label>
      </div>

      {/*  Submit button triggers POST to Flask */}
      <button onClick={handleSubmit} style={{ padding: "8px 16px" }}>
        Submit
      </button>

      {/* Show result from backend */}
      {result && (
        <div style={{ marginTop: 30, fontSize: 20, fontWeight: "bold" }}>
          {result}
        </div>
      )}
    </div>
  );
}
