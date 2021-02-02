import React from "react";
import "./Idea.css";

const IdeaThread = ({ idea, setIdeas }) => {
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
        <span>{idea.owner.username}</span>

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
