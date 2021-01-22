import React, { useState, useEffect, } from "react";
import { useParams, Link } from "react-router-dom";
import IdeaThread from "./IdeaThread";
import Ideas from "./IdeaThread";
import IdeaFormModal from "./IdeaFormModal";
import "./Idea.css";

export default function IdeasFeed() {
  const { id } = useParams()
  const [allIdeas, setIdeas] = useState([]);
  useEffect(() => {
    (async () => {
      const res = await fetch("/api/ideas");
      const parsedIdeas = await res.json();
      setIdeas(parsedIdeas);

      console.log(parsedIdeas);
    })();
  }, []);


  return (
    <div className="idea__feed-wrapper">

        <IdeaFormModal setIdeas={setIdeas} />
      <div className="idea__feed-container">

        <div className="title">
          <h1>
            News Feed
          </h1>
        </div>
        {allIdeas.map((idea) => {
          return <IdeaThread key={idea.id} idea={idea} ideas={allIdeas} setIdeas={setIdeas} />;
        })}
      </div>
    </div>
  );
}
