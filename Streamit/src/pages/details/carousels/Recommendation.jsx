import React, { useEffect, useState } from "react";
import Carousel from "../../../components/carousel/Carousel";

const Recommendation = ({ mediaType, id }) => {
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchRecommendations = async () => {
      try {
        const response = await fetch(`http://localhost:5000/recommendations?mediaType=${mediaType}&id=${id}`);
        const data = await response.json();
        setRecommendations(data.results);
        setLoading(false);
      } catch (error) {
        console.error("Error fetching recommendations:", error);
        setLoading(false);
      }
    };

    fetchRecommendations();
  }, [mediaType, id]);

  return (
    <div>
      <Carousel title="Recommendations" data={recommendations} loading={loading} />
    </div>
  );
};

export default Recommendation;
