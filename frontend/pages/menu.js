export default function Menu() {
  return (
    <div style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <h1>🌐 Ai-Web+App Builder: Client Portal</h1>
      <p>Welcome! Choose what you'd like to do:</p>

      <ul style={{ listStyle: "none", padding: 0 }}>
        <li style={{ marginBottom: "1rem" }}>
          <a href="/index" style={{ fontSize: "1.2rem" }}>🧠 Generate a New Site from AI Prompt</a>
        </li>
        <li style={{ marginBottom: "1rem" }}>
          <a href="/dashboard" style={{ fontSize: "1.2rem" }}>📸 View Your AI Website (Live Preview)</a>
        </li>
        <li style={{ marginBottom: "1rem" }}>
          <a href="/frozen" style={{ fontSize: "1.2rem" }}>❄️ Freeze / 🔓 Unfreeze Your Website</a>
        </li>
      </ul>
    </div>
  );
}
