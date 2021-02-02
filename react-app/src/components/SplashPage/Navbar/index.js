import React from "react";
import { Link } from "react-router-dom";

import UserMenu from "./UserMenu";

import "./NavBar.css";
const logo = require("../../../assets/colorCodedTeesLogo.png")

const NavBar = ({ authenticated, setAuthenticated, cartCount}) => {
  return (
    <header className="nav-overlay">
      <div className="">
        <nav className="nav-bar">
          <div className="navbar__left">
            <Link to="/t-shirts">
              <img src={logo} alt="color-coded-tees"/>
            </Link>
          </div>
          {/*-------searchbar---------*
        <div className="navbar__center">
          <div style={{ width: "300px", height: "40px", borderRadius: "20px", border: "1px solid black", textAlign: "center" }}> Search Bar Placeholder</div>

        </div> */}

          <div className="navbar__right">
            {/* add user auth to this component when made */}
            <Link className="nav-btn" to="/t-shirts">
              {/* <h1>Home</h1>{" "} */}
            </Link>
            <Link className="nav-btn" to="/t-shirts">
              <h1>T-Shirt Shop</h1>{" "}
            </Link>
            <Link className="nav-btn" to="/ideas">
              <h1>Idea Feed</h1>{" "}
            </Link>
            <Link className="navbar__link" to="/t-shirts">
              <i className="fas fa-cart-plus"></i>
              <span>{cartCount}</span>
            </Link>

            <UserMenu
              authenticated={authenticated}
              setAuthenticated={setAuthenticated}
            />
          </div>
        </nav>
      </div>
    </header>
  );
};

export default NavBar;
