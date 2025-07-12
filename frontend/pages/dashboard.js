import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Dashboard() {
  const [status, setStatus] = useState('loading');
  const [siteUrl, setSiteUrl] = useState('');

  useEffect(() => {
    // Simulated client ID for testing
    const clientId = "client123";

    axios.post("http://localhost:5000/generate", {
      client_id: clientId,
      prompt: "Create a website for a photography portfolio"
    }).then(res => {
      setSiteUrl(res.data.site_path);
      setStatus("active");
    }).catch(() => {
      setStatus("frozen");
    });
  }, []);

  if (status === "frozen") {
    return <div>Your account is frozen. Please check billing.</div>;
  }

  return (
    <div>
      <h1>Your AI Website Preview</h1>
      {siteUrl ? (
        <iframe
          src={siteUrl}
          style={{ width: '100%', height: '600px', border: '1px solid #ccc' }}
          title="Site Preview"
        />
      ) : (
        <p>Generating your website...</p>
      )}
    </div>
  );
}
