import React from 'react';
import { Link } from 'react-router-dom';

import UserMenu from './UserMenu'

import './NavBar.css'

const NavBar = ({ authenticated, setAuthenticated }) => {
  return (
    <nav>
      <div className="navbar__left">
        <Link to="/"> {<h1 className="logo">{`<ColorCodedTees />`}</h1>} </Link>

      </div>
      {/* <div className="navbar__center">
        <div style={{ width: "300px", height: "40px", borderRadius: "20px", border: "1px solid black", textAlign: "center" }}> Search Bar Placeholder</div>

      </div> */}

      <div className="navbar__right">
        {/* add user auth to this component when made */}
         <Link className="nav-btn" to="/idea/create"><h1>Have an Idea?</h1> </Link>
         <Link className="nav-btn" to="/t-shirt"><h1>T-Shirt Shop</h1> </Link>
         <Link className="nav-btn" to="/idea"><h1>The Pizza Box</h1> </Link>
        <Link className="navbar__link" to="/cart">
        <i class="fas fa-cart-plus"></i>
        </Link>

        <UserMenu authenticated={authenticated} setAuthenticated={setAuthenticated} />
      </div>
    </nav>
  );
}

export default NavBar;
