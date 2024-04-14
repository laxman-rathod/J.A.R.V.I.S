import React, { useEffect, useState } from "react";
import axios from "axios";

const FetchDataComp = () => {
  const [data, setData] = useState("");

  useEffect(() => {
    let isMounted = true;

    const fetchData = async () => {
      try {
        const response = await axios.get("http://localhost:5000/api/data");
        if (isMounted) {
          console.log(response.data);
          setData(response.data);
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();

    return () => {
      isMounted = false;
    };
  }, []);

  return (
    <div>
      <p>{data}</p>
    </div>
  );
};

export default FetchDataComp;
