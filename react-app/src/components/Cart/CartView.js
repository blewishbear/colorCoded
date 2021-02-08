import React from "react";
import { useRecoilState } from "recoil";
import { cartState, productsState } from "../../Atoms";
import CartProduct from "./CartProduct";

export default function CartView() {
  const [cart, setCart] = useRecoilState(cartState);
  const [products, setProducts] = useRecoilState(productsState);
  return (
    <div className="cart__container">
      {console.log(cart)}
      {!cart.length ? (
        <div className="empty__cart">
          <p>No Items in the cart</p>
        </div>
      ) : (
        cart.map((productId) => {
          return <CartProduct product={products[productId - 1]} />;
        })
      )}
    </div>
  );
}
