import { useEffect, useState } from "react";
import "../styles/weather-temp.css";

const WeatherTemp = () => {
  const [weather, setWeather] = useState("27.🌤️");
  const [city, setCity] = useState("Jalna");

  //   useEffect(() => {}, []);

  return (
    <div className="wt-container">
      <div className="weather_temp">
        <div className="weather arc_1 e4-1">
          <div className="arc_2 e4-2">
            <div className="counterspin4"></div>
          </div>
          <div style={{ fontSize: "40px", marginTop: "5px" }}>{weather}</div>
          <div style={{ fontSize: "25px", marginTop: "-65px" }}>{weather}</div>
        </div>
        <div className="temp arcc e11">
          <div
            style={{
              fontSize: "18px",
              marginTop: "55px",
            }}
          >
            {city}
          </div>
          <div
            style={{
              fontSize: "17px",
              marginTop: "-22px",
            }}
          >
            {city}
          </div>
        </div>
      </div>
    </div>
  );
};

export default WeatherTemp;
