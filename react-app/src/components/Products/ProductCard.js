import React from 'react';
import { useHistory } from 'react-router-dom';


const ProductCard = ({ product }) => {
  const history = useHistory();

  const handleClick = (e) => {
    history.push(`t-shirts/${product.id}`)
  }
  return (
    <div className='listings__listing-card' onClick={handleClick}>
      <img src={product.img_url} alt={`${product.title}`} />
      <h2>{product.title}</h2>
      <h3><strong>${product.price}</strong></h3>
    </div>
  )
}

export default ProductCard
