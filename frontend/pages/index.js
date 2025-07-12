import { useState } from "react";

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const [clientId, setClientId] = useState("user123");
  const [siteURL, setSiteURL] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateWebsite = async () => {
    setLoading(true);
    try {
      const res = await fetch("http://localhost:5000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ client_id: clientId, prompt }),
      });

      const data = await res.json();
      setSiteURL(data.url);
    } catch (err) {
      console.error("Failed to generate site", err);
    }
    setLoading(false);
  };

  return (
    <div>
      <h1>Ai-Web+App Builder</h1>
      <input
        type="text"
        placeholder="Enter prompt"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <button onClick={generateWebsite} disabled={loading}>
        {loading ? "Generating..." : "Generate Site"}
      </button>

      {siteURL && (
        <div>
          <h2>Preview:</h2>
          <iframe
            src={`http://localhost:5000${siteURL}`}
            style={{ width: "100%", height: "500px", border: "1px solid black" }}
            title="Generated Site"
          ></iframe>
        </div>
      )}
    </div>
  );
}
