import React, { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [usage, setUsage] = useState(null);
  const [location, setLocation] = useState(null); // ✅ Step 1: Track location

  // Fetch electricity usage
  const fetchUsage = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:5000/api/usage");
      setUsage(res.data);
    } catch (error) {
      console.error("Error fetching usage data:", error);
    }
  };

  // Get location and fetch usage
  useEffect(() => {
    fetchUsage();

    // ✅ Step 2: Get user location
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const coords = {
            lat: position.coords.latitude.toFixed(4),
            lon: position.coords.longitude.toFixed(4),
          };
          setLocation(coords);
        },
        (error) => {
          console.error("Error getting location:", error);
        }
      );
    }

    const interval = setInterval(fetchUsage, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="App">
      <h1>Smart Home Electricity Monitoring</h1>

      {/* ✅ Step 3: Display Location */}
      {location && (
        <p>
          <strong>Your Location:</strong> {location.lat}, {location.lon}
        </p>
      )}

      {/* ✅ Step 4: Display Usage */}
      {usage ? (
        <div className="dashboard">
          <p>
            <strong>Living Room:</strong> {usage.living_room} kWh
          </p>
          <p>
            <strong>Bedroom:</strong> {usage.bedroom} kWh
          </p>
          <p>
            <strong>Kitchen:</strong> {usage.kitchen} kWh
          </p>
          <h3>Total Usage: {usage.total} kWh</h3>
        </div>
      ) : (
        <p>Loading usage data...</p>
      )}
    </div>
  );
}

export default App;
