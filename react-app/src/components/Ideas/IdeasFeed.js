import React, { useState, useEffect, } from "react";
import IdeaThread from "./IdeaThread";
import IdeaFormModal from "./IdeaFormModal";
import "./Idea.css";
import { useRecoilState } from "recoil"
import { ideaState } from '../../Atoms';

export default function IdeasFeed() {
  const [allIdeas, setIdeas] = useRecoilState(ideaState);
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

        <div className="idea__container-title">
          <h1>
            Ideas Feed
          </h1>
        </div>
        {allIdeas.map((idea) => {
          return <IdeaThread key={idea.id} idea={idea} ideas={allIdeas} setIdeas={setIdeas} />;
        })}
      </div>
    </div>
  );
}
