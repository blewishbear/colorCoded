import React, { useState, useEffect } from "react";
import { useUser } from "../../context/UserContext";
import LoginForm from "../SplashPage/auth/LoginFormModal/LoginForm";
import "./Idea.css";

const CreateIdeaForm = ({ setIdeas, onClose }) => {
  // const history = useHistory()
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const { user } = useUser();

  useEffect(() => {}, []);

  const createIdea = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("/api/ideas/create", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_id: user.id,
          title,
          description,
        }),
      });
      const newIdea = await response.json();
      setIdeas((prevIdeas) => [newIdea, ...prevIdeas]);
    } catch (e) {
      console.log(e);
    }
    // history.push("/ideas")
  };

  const updateTitle = (e) => {
    setTitle(e.target.value);
  };
  const updateDescription = (e) => {
    setDescription(e.target.value);
  };
  console.log("is there a user?", user);
  if (!user || user.errors) {
    return (
      <>
        <LoginForm onClose={onClose}/>
      </>
    );
  } else {
    return (
      <form className="create-idea-container" onSubmit={createIdea}>
        <div className="idea__form-input">
          <input
            name="title"
            placeholder="Title"
            type="text"
            value={title}
            onChange={updateTitle}
          />
        </div>
        <div className="idea__form-input">
          <textarea
            placeholder="Description"
            name="description"
            value={description}
            onChange={updateDescription}
          />
        </div>
        <button type="submit" onClick={onClose}>
          Post idea
        </button>
      </form>
    );
  }
};

export default CreateIdeaForm;

// })()
// },[])
// }
