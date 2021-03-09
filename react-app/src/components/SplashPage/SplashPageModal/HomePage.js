import React from "react";
import "./HomePage.css";
import LoginFormDialog from "../SplashPageModal/index";
import SignUpFormDialog from "../SplashPageModal/SignUpIndex";
const cb = require("../../../assets/curlyBoyz.JPG");
const rn = require("../../../assets/reactNative.png");
const mern = require("../../../assets/jpg.jpg");
const cg = require("../../../assets/CurlyGirls4.png");
export default function HomePage() {
  return (
    <div className="splash-page">
      <div className="splash-buttons">
        <LoginFormDialog />
      <SignUpFormDialog />
      </div>


    <div className="mern home-image" />
    <div className="curlyG home-image" />
    <div className="native home-image" />
    </div>
  );
}
