import React from "react";
import "./HomePage.css";
const cb = require("../../../assets/curlyBoyz.JPG");
const rn = require("../../../assets/reactNative.png");
const mern = require("../../../assets/mern.png");
export default function HomePage() {
  return (
    <div>
      <div className="splash-page">
       Welcome to ColorCodeTees
        <div><img src={cb} alt="CurlyBoys" /></div>
        <div><img src={rn} alt="CurlyBoys" /></div>
        <div><img src={mern} alt="CurlyBoys" /></div>
        
      </div>
    </div>
  );
}
