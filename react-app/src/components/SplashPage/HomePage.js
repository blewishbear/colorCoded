import React from "react";
import "./SplashPage.css";

export default function HomePage() {
  return (
    <div
      style={{
        backgroundColor: "white",
        width: "100vw",
        height: "100vh",
        margin: "0px",
        padding: "0px",
        display: "flex"
      }}
    >
      <div className="splash-page">
       Welcome to ColorCodeTees
        <img src="./curlyBoyz.JPG" alt="CurlyBoys" />
        <div>
          Please Sign in
        </div>
      </div>
      Content
    </div>
  );
}
