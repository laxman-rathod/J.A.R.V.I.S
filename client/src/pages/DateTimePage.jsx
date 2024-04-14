import { useEffect, useState } from "react";
import "../styles/dateTime.css";

const DateTimePage = () => {
  const [date, setDate] = useState("");
  const [month, setMonth] = useState("");
  const [dayName, setDayName] = useState("");
  const [time, setTime] = useState("");

  useEffect(() => {
    const updateDateTime = () => {
      const now = new Date();
      const day = now.getDate();
      const monthNames = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
      ];
      const month = monthNames[now.getMonth()];
      const days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
      ];
      const dayName = days[now.getDay()];
      const hr = now.getHours();
      const min = now.getMinutes();
      const sec = now.getSeconds();
      const formattedHr = hr % 12 || 12; // Convert hours to 12-hour format

      const formattedTime = `${formattedHr < 10 ? "0" : ""}${formattedHr}:${
        min < 10 ? "0" : ""
      }${min}:${sec < 10 ? "0" : ""}${sec}`;

      setDate(day);
      setMonth(month);
      setDayName(dayName);
      setTime(formattedTime);

      setTimeout(updateDateTime, 1000); // Call this function again in 1000ms
    };

    updateDateTime(); // Initial call

    return () => clearTimeout(); // Clean up the timeout
  }, []);

  return (
    <div className="date-time-container">
      <div className="date_time">
        <div className="date semi_arc e4">
          <div className="semi_arc_2 e4_1">
            <div className="counterspin4"></div>
          </div>
          <div id="day" style={{ fontSize: "40px", marginTop: "5px" }}>
            {date}
          </div>
          <div id="month" style={{ fontSize: "25px", marginTop: "-65px" }}>
            {month}
          </div>
        </div>
        <div className="time arc e1">
          <div
            id="hrMin"
            style={{ fontSize: "18px", marginLeft: "-6px", marginTop: "55px" }}
          >
            {time}
          </div>
          <div id="dayName" style={{ fontSize: "17px", marginTop: "-22px" }}>
            {dayName}
          </div>
        </div>
      </div>
    </div>
  );
};

export default DateTimePage;
