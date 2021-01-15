import React, { useState } from "react";
import { Link, useHistory } from "react-router-dom";
import "./Idea.css";

const IdeaThread = ({ idea }) => {
  console.log(idea);
  const history = useHistory();

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
          <button type="submit" className="fas fa-dumpster"></button>
        </div>
      </div>
    </div>
  );
};
export default IdeaThread;
