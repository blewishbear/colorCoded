import React from "react";
import { useRecoilState } from "recoil";
import { cartState } from "../../Atoms";
import "./Product.css";
const ProductCard = ({ product }) => {

const [cart, setCart] = useRecoilState(cartState)

  const handleClick = (e) => {
    // history.push(`/t-shirts/${product.id}`);
  };

  const addToCart = () =>{
    //previous is the current cart and we are adding a new product
    setCart(previous => [...previous, product.id])
    localStorage.setItem("cart", JSON.stringify(cart))
  }

  //=========================== adding to cart using local storage =======================>
  // const addToCart = (e) => {
  //   if (cart[product.id]){
  //     setCart({...cart, [product.id]: cart[product.id] + 1})

  //   } else {
  //     setCart({...cart, [product.id] : 1})
  //   }
  //   setCartCount((cartCount) => cartCount + 1)
  // };


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
