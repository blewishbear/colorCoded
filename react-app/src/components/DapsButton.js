import React from 'react'
import { useRecoilState } from "recoil"

export default function DapsButton() {
  const [ dapped, setDapped ] = useRcoileState(false)

  const addDaps = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(`api/ideas/${idea.idea}`)

    } catch(e){
      console.log(e)
    }
  }
  return (
    <div>

    </div>
  )
}
