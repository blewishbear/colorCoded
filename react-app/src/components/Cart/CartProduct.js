import React, { useEffect } from "react";
import { useRecoilState } from "recoil";
import { productsState } from "../../App";
import { cartState } from "../../App";
import ProductCard from "../Products/ProductCard";
import "./Cart.css";

export default function CartProduct({ product }) {
  const [cart, setCart] = useRecoilState(cartState);
  console.log(product);
  // const [products, setProducts] = useRecoilState(productsState)

  const removeCart = () => {
    const newCart = cart.filter((id) => id !== product.id);
    setCart(newCart);
    localStorage.setItem("cart", JSON.stringify(newCart));
  };
  if (!product) return null;
  return (
    <div className="cart__product-container">
      <div className="cart__item">
        <img src={product.img_url} alt={product.title}></img> - ${product.price}
        {/* {product.quantity}) */}
      </div>
      <div className="cart__btn">
        <button onClick={removeCart}>Remove from Cart</button>
      </div>
    </div>
  );
}
