import React, { useEffect, useState } from "react";
import { useRecoilState } from "recoil";
import { ideaState, dapState } from "../../Atoms";
import { useUser } from "../../context/UserContext";
import "./Idea.css";
export default function DapButton({ idea }) {
  const [ideas, setIdeas] = useRecoilState(ideaState);
  const [dapsByIdea, setDapsByIdea] = useState([]);
  const [daps, setDaps] = useRecoilState(dapState);
  const [loaded, setLoaded] = useState(false);
  const [dapped, setDapped] = useState(false);

  const { user } = useUser();

  const dapIdea = async (e) => {
    e.preventDefault();
    console.log("these are daps", dapsByIdea);

    try {
      const response = await fetch(`/api/ideas/${idea.id}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_id: user.id,
          idea_id: idea.id,
        }),
      });
      const parsedDaps = await response.json()
      await setDapsByIdea(parsedDaps)
    } catch (e) {
      console.log(e);
    }
  };

  const deleteDap = async () => {
    console.log(idea);
    const response = await fetch(`/api/daps/${idea.id}`, {
      method: "DELETE",
    });

    if (response.ok) {
      setIdeas((ideas) => {
        return ideas.filter((i) => i.id !== idea.id);
      });
    }
  };


  useEffect(() => {
    (async () => {
      const filteredDaps = daps.filter((dap) => {
        return dap.idea_id === idea.id;
      });
      await setDapsByIdea(filteredDaps);

      console.log("daps by idea", filteredDaps);
      filteredDaps.map((dap) => {
        if (dap.user_id === user.id) {
          return setDapped(true);
        }
      });
      return setLoaded(true);
    })();
  }, []);




  return (
    loaded && (
      <div >
        <div className="dap__btn-container">
          {dapped ? (
            <button id="dapped__btn" type="submit" className="fas fa-fist-raised" >

              <div className="dap-count">{dapsByIdea.length}</div>
            </button>
          ) : (
            <button id="undapped__btn"
              type="submit"
              className="fas fa-fist-raised"
              onClick={dapIdea}
            >
               <div className="dap-count">{dapsByIdea.length}</div>
            </button>
          )}
        </div>
      </div>
    )
  );
}
