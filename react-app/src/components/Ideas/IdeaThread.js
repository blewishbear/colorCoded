import React from "react";
import DapButton from './DapButton'
import "./Idea.css";

const IdeaThread = ({ idea, setIdeas }) => {
  const deleteIdea = async () => {
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
      <p className="idea__title">
        Title:
        <span>{idea.title}</span>
      </p>
      <p className="idea__title">
        Description:
        <span>{idea.description}</span>

      </p>
      <p className="idea__title">
        By:
        <span>{idea.user.username}</span>

      </p>
      <div className="idea__btns">
        {/* <div>
          <button type="submit" className="fas fa-fist-raised"></button>
        </div> */}
          <DapButton idea={idea}/>
        {/* <div>
          <button type="submit" className="edit__btn"></button>
        </div> */}
        <div>
          <button id="trash__btn"
            type="submit"
            className="fas fa-trash-alt"
            onClick={deleteIdea}
          ></button>
        </div>
      </div>
    </div>
  );
};
export default IdeaThread;
