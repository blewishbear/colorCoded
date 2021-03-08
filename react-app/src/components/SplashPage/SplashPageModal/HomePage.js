import React from "react";
import "./HomePage.css";
import LoginFormDialog from "../SplashPageModal/index"
import SignUpFormDialog from "../SplashPageModal/SignUpIndex"
const cb = require("../../../assets/curlyBoyz.JPG");
const rn = require("../../../assets/reactNative.png");
const mern = require("../../../assets/jpg.jpg");
const cg = require("../../../assets/CurlyGirls4.png");
export default function HomePage() {
  return (
      <div className="splash-page">
        <div className="splash-left">
          <LoginFormDialog />
          {/* <div className="mern">
            <img
              src="https://i.imgur.com/nVmqbdM.png"
              alt="CurlyBoys"
            />
          </div>
            <div className="left-bottom">
              <div className="curlyB">
                <img src={cb} alt="CurlyBoys" />
              </div>
            </div> */}
            <div className="native">
              {/* <img src={rn} alt="CurlyBoys" /> */}
            </div>
            <div className="curlyG">
              {/* <img src={cg} alt="CurlyBoys" /> */}
            </div>
        </div>
         <div className="splash-right">
            <div className="mern">
              <SignUpFormDialog />
            {/* <img
              src="https://i.imgur.com/nVmqbdM.png"
              alt="CurlyBoys"
            /> */}
          </div>
        </div>
      </div>
  );
}
