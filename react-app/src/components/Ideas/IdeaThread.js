import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import "./Idea.css";

const IdeaThread = ({ idea, setIdeas, handleDelete }) => {
  const { id } = useParams();
  const deleteIdea = async () => {
    console.log(idea);
    const response = await fetch(`/api/ideas/${idea.id}`, {
      method: "DELETE",
    });

    if (response.ok) {
      setIdeas((ideas) => {
        return ideas.filter((i) => i.id !== idea.id);
      });
    }
  };

  return (
    <div className="idea__container">
      <p>
        <span>Title: </span>
        {idea.title}
      </p>
      <p>
        Description: <span></span>
        {idea.description}
      </p>
      <p>
        By: <span></span>
        {idea.owner.username}
      </p>
      <div className="idea__btns">
        <div>
          <button type="submit" className="fas fa-fist-raised"></button>
        </div>
        {/* <div>
          <button type="submit" className="edit__btn"></button>
        </div> */}
        <div>
          <button
            type="submit"
            className="fas fa-dumpster"
            onClick={deleteIdea}
          ></button>
        </div>
      </div>
    </div>
  );
};
export default IdeaThread;
