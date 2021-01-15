import React, {useState} from "react";
import { Link, useHistory } from "react-router-dom";
import "./Product.css"
const ProductCard = ({ product }) => {
  const history = useHistory();
  const [cartNumber, setCartNumber] = useState(0);


  const handleClick = (e) => {
    // history.push(`/t-shirts/${product.id}`);
  };
  const addToCart = () => {
    setCartNumber(cartNumber + 1);
  }
  return (
      <div className="product__container" onClick={handleClick}>
        <img src={product.img_url} alt={`${product.title}`} />
        <h2>{product.title}</h2>
        <h3>
          <strong>${product.price}</strong>
        </h3>
        <Link onClick={addToCart} className="add__cart-btn" to="/t-shirts">Add to Cart</Link>
      </div>
  );
};

export default ProductCard;
