import React, { useState, useRef, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);
  const chatEndRef = useRef(null);

  const sendMessage = async () => {
    if (!message.trim()) return;

    const userMsg = { sender: "user", text: message };
    setChat((prev) => [...prev, userMsg]);

    setMessage("");

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", {
        text: message,
      });

      const botMsg = { sender: "bot", text: res.data.response };
      setChat((prev) => [...prev, botMsg]);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chat]);

  return (
    <div className="app">
      <div className="chat-window">
        {chat.map((msg, index) => (
          <div key={index} className={`chat-row ${msg.sender}`}>
            <div className="bubble">{msg.text}</div>
          </div>
        ))}
        <div ref={chatEndRef}></div>
      </div>

      <div className="input-bar">
        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Message Chatbot..."
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />
        <button onClick={sendMessage}>➤</button>
      </div>
    </div>
  );
}

export default App;