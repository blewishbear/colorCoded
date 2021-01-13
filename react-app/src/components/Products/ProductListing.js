import { responsiveFontSizes } from "@material-ui/core";
import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

import ProductCard from "./ProductCard";

const ProductListing = () => {
  const [allProducts, setAllProducts] = useState([]);
  useEffect(() => {
    (async () => {
      const res = await fetch("/api/t-shirts");
      const parsedProducts = await res.json();
      setAllProducts(parsedProducts);
    })();
  }, []);

  return (
    <div className="product__listing-wrapper">

      <div className="product__listing-title">
        <h1> Check out these cool Tees</h1>
      </div>
      <div className="product__listing-container">
        {allProducts.map((product) => {
          return <ProductCard key={product.id} product={product} />;
        })}
      </div>
    </div>
  );
};

export default ProductListing;
