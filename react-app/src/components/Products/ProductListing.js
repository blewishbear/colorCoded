// import { responsiveFontSizes } from "@material-ui/core";
import React, { useState, useEffect } from "react";
import {useRecoilState} from "recoil"
import { productsState } from "../../Atoms";

import ProductCard from "./ProductCard";

const ProductListing = ({setCartCount}) => {
  const [products, setProducts ]= useRecoilState(productsState)
    // const [cart, setCart] = useState(
  //   localStorage.getItem("cart") ? JSON.parse(localStorage.getItem("cart")) : {}
  // );


  // useEffect(() => {
  //   localStorage.setItem("cart", JSON.stringify(cart));

  // }, [cart])

  return (
    <div className="product__listing-wrapper">

      <div className="product__listing-title">
        <h1>Check out these cool Tees</h1>
      </div>
      <div className="product__listing-container">
        {products.map((product) => {
          return <ProductCard key={product.id} product={product} />;
        })}
      </div>
    </div>
  );
};

export default ProductListing;
