import React, { useEffect } from 'react'
import { useRecoilState } from 'recoil'
import { productState } from "../../App"
import { cartState } from "../../App"
import ProductCard from '../Products/ProductCard';
import './Cart.css'

export default function ProductCardInsideCart({setCart, product}) {

  const [allProducts, setAllProducts] = useRecoilState(productState)

  useEffect(() => {
    (async () => {
      const res = await fetch("/api/t-shirts");
      const parsedProducts = await res.json();
      setAllProducts(parsedProducts);
    })();
  }, []);

const removeCart = () => {
    setCart(previous => previous.filter(id => id !== product.id))
  }
  return (
    <div className="cart__container">
      <div className="cart">
      <ul>
          {allProducts.map(product => (
            <li key={product.id}>
              <div>
                <img src={product.img_url} alt={product.title}></img> - ${product.price}
                {/* {product.quantity}) */}
              </div>
              <div>
                <button
                  onClick={removeCart}>
                  Remove from Cart
                </button>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  )
}
