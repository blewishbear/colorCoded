import React from "react"
import { useRecoilState, } from "recoil";
import { cartState, productsState } from "../../App";
import CartProduct from "./CartProduct";


export default function CartView() {
  const [cart, setCart] = useRecoilState(cartState)
  const [products, setProducts] = useRecoilState(productsState)
  console.log(products)
  return (
    <div>
      {cart.map(productId => {
        return <CartProduct product={products[productId - 1]} />
      })}

    </div>
  )
}
