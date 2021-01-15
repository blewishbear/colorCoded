import React, { useState } from 'react';
import {Link, useHistory } from 'react-router-dom';
import "./Idea.css"


const IdeaThread = ({ idea }) => {
  console.log(idea)
  const history = useHistory();

  return (
    <div className="idea__container">
      <h2>{idea.title}</h2>
      <h3>{idea.description}</h3>
      <h4>By: {idea.owner.username}</h4>
      <div className="idea__btns"></div>
        <div><button type="submit" className="dap__btn" ></button></div>
        <div><button type="submit" className="edit__btn"></button></div>
        <div><button type="submit" className="delete__btn"></button></div>
    </div>
  )
}
export default IdeaThread
