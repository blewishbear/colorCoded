import React from "react";
import "./SplashPage.css";
import curlyBoyz from "./Navbar"
export default function HomePage() {
  return (
    <div
      style={{
        backgroundImage:`url("https://via.placeholder.com/500")`,
        width: "100vw",
        height: "100vh",
        margin: "0px",
        padding: "0px",
        display: "flex"
      }}
    >
      <div className="splash-page">
       Welcome to ColorCodeTees
        <img src={curlyBoyz} alt="CurlyBoys" />
        <div>
          Please Sign in
        </div>
      </div>
      Content
    </div>
  );
}
