import React from "react";
import { Link, useHistory } from "react-router-dom";
import "./Product.css"
const ProductCard = ({ product }) => {
  const history = useHistory();

  const handleClick = (e) => {
    // history.push(`/t-shirts/${product.id}`);
  };
  return (
      <div className="product__container" onClick={handleClick}>
        <img src={product.img_url} alt={`${product.title}`} />
        <h2>{product.title}</h2>
        <h3>
          <strong>${product.price}</strong>
        </h3>
        <Link className="add__cart-btn" to="/t-shirts">Add to Cart</Link>
      </div>
  );
};

export default ProductCard;
