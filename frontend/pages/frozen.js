import { useState } from "react";

export default function FrozenControl() {
  const [isFrozen, setIsFrozen] = useState(false);

  const toggleFreeze = () => {
    // This is UI logic; actual backend logic can be added later
    setIsFrozen((prev) => !prev);
  };

  return (
    <div>
      <h1>Freeze/Unfreeze Site</h1>
      <p>Status: {isFrozen ? "❄️ Frozen" : "🔥 Active"}</p>
      <button onClick={toggleFreeze}>
        {isFrozen ? "Unfreeze Site" : "Freeze Site"}
      </button>
    </div>
  );
}
