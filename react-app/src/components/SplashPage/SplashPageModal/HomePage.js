import React from "react";
import "./HomePage.css";
const cb = require("../../../assets/curlyBoyz.JPG");
const rn = require("../../../assets/reactNative.png");
const mern = require("../../../assets/jpg.jpg");
const cg = require("../../../assets/CurlyGirls4.png");
export default function HomePage() {
  return (
    <div>
      <div className="splash-page">
        <div>
          <img id="mern" src="https://i.imgur.com/nVmqbdM.png" alt="CurlyBoys" /></div>
        <div>
        <div>
          <img id="curlyB" src={cb} alt="CurlyBoys" /></div>
        <div>
          <img id="native" src={rn} alt="CurlyBoys" /></div>
          <img id="curlyG" src={cg} alt="CurlyBoys" /></div>
      </div>
    </div>
  );
}
