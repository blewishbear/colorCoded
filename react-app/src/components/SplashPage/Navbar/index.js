import React from "react";
import { Link } from "react-router-dom";
import { useRecoilValue } from "recoil";
import UserMenu from "./UserMenu";

import { useUser } from "../../../context/UserContext";
import "./NavBar.css";
import { cartState } from "../../../Atoms";
import CartView from "../../Cart/CartView";
const logo = require("../../../assets/colorCodedTeesLogo.png");

const NavBar = ({ authenticated, setAuthenticated }) => {
  const cart = useRecoilValue(cartState);

  return (
    <header className="nav-overlay">
      <div className="">
        <nav className="nav-bar">
          <div className="navbar__left">
            <Link to="/t-shirts">
              <img src={logo} alt="color-coded-tees" />
            </Link>
          </div>

          <div className="navbar__center">
            <a href="https://github.com/blewishbear">
              <i className="fab fa-github-square"></i>
            </a>
            <a href="https://www.linkedin.com/in/mathias-anderson-42167b137/">
              <i className="fab fa-linkedin"></i>
            </a>
            <a href="https://angel.co/u/mathias-anderson">
              <i className="fab fa-angellist"></i>
            </a>
          </div>

          <div className="navbar__right">

            <Link className="nav-btn" to="/t-shirts">
             
            </Link>
            <Link className="nav-btn" to="/t-shirts">
              <h1>T-Shirt Shop</h1>{" "}
            </Link>
            <Link className="nav-btn" to="/ideas">
              <h1>Idea Feed</h1>{" "}
            </Link>
            <Link className="navbar__link" to="/cart">
              <i className="fas fa-cart-plus"></i>
              <span>{cart.length}</span>
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
