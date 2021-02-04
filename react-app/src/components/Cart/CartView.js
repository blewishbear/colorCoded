import React from "react"
import { useRecoilState } from "recoil";
import { cartState } from "../../App";
import ProductCardInsideCart from "./ProductCardInsideCart";


export default function CartView() {
  //how you subscribe to states from other components
  const [cart, setCart] = useRecoilState(cartState)
  return (
    <div>
      <ProductCardInsideCart />
    </div>
  )
}
