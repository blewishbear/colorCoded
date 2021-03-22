import React, { useState, useEffect } from "react";
import {useRecoilState} from "recoil"
import { productsState } from "../../Atoms";

import ProductCard from "./ProductCard";

const ProductListing = ({setCartCount}) => {
  const [products, setProducts ]= useRecoilState(productsState)


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
