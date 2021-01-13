import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import Ideas from "./Ideas"
export default function IdeasFeed() {
  const [allIdeas, setIdeas] = useState([])
  useEffect(() => {

    (async () => {
      const res = await fetch('/api/ideas');
      const parsedIdeas = await res.json();
      setIdeas(parsedIdeas);
      console.log(parsedIdeas)
    })()
  }, [])
  return (
    <div>
      <div className="title"><h1>Ever Have an idea for a t-shirt, but all you had to write on was a pizza box?</h1></div>
      {allIdeas.map(idea => {
        return <Ideas key={idea.id} idea={idea} />
      })}
    </div>
  )
}
