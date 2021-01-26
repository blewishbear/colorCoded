import { responsiveFontSizes } from "@material-ui/core";
import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

import ProductCard from "./ProductCard";

const ProductListing = ({setCartCount}) => {
  const [allProducts, setAllProducts] = useState([]);
  const [cart, setCart] = useState(
    localStorage.getItem("cart") ? JSON.parse(localStorage.getItem("cart")) : {}
  );

  useEffect(() => {
    (async () => {
      const res = await fetch("/api/t-shirts");
      const parsedProducts = await res.json();
      setAllProducts(parsedProducts);
    })();
  }, []);
  useEffect(() => {
    localStorage.setItem("cart", JSON.stringify(cart));

  }, [cart])

  return (
    <div className="product__listing-wrapper">

      <div className="product__listing-title">
        <h1> Check out these cool Tees</h1>
      </div>
      <div className="product__listing-container">
        {allProducts.map((product) => {
          return <ProductCard key={product.id} product={product} cart={cart} setCart={setCart} setCartCount={setCartCount} />;
        })}
      </div>
    </div>
  );
};

export default ProductListing;
