import React, { useState, useEffect } from "react";
import { Link, useHistory } from "react-router-dom";
import "./Product.css";
const ProductCard = ({ product, cart, setCart, setCartCount }) => {
  const history = useHistory();


  const handleClick = (e) => {
    // history.push(`/t-shirts/${product.id}`);
  };
  const addToCart = (e) => {
    if (cart[product.id]){
      setCart({...cart, [product.id]: cart[product.id] + 1})

    } else {
      setCart({...cart, [product.id] : 1})
    }
    setCartCount((cartCount) => cartCount + 1)
  };


  return (
    <div className="product__container" onClick={handleClick}>
      <img src={product.img_url} alt={`${product.title}`} />
      <h2>{product.title}</h2>
      <h3>
        <strong>${product.price}</strong>
      </h3>
      <button onClick={addToCart} className="add__cart-btn">
        Add to Cart
      </button>
    </div>
  );
};

export default ProductCard;
