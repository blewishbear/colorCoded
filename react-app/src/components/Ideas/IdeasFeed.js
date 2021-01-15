import React, { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import IdeaThread from "./IdeaThread";
import Ideas from "./IdeaThread";
import CreateIdeaForm from "./IdeaForm";
import "./Idea.css";

export default function IdeasFeed() {
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
      <Link className="idea__form-btn" exact to="/ideas/create"> Got a new Idea?</Link>
        <CreateIdeaForm setIdeas={setIdeas} />
      <div className="idea__feed-container">

        <div className="title">
          <h1>
            News Feed
          </h1>
        </div>
        {allIdeas.map((idea) => {
          return <IdeaThread key={idea.id} idea={idea} />;
        })}
      </div>
    </div>
  );
}
