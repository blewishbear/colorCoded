import { responsiveFontSizes } from '@material-ui/core';
import React, { Fragment, useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

import ProductCard from './ProductCard'

const ProductListing = () => {
    const { id } = useParams()
    const [allProducts, setAllProducts] = useState([])
  useEffect(() => {

    (async () => {
      const res = await fetch('/api/t-shirts');
      const parsedProducts = await res.json();
      console.log(parsedProducts)
      setAllProducts(parsedProducts)
    })()
  }, [])

  return (
    <div className='product_listing_container'>
      <div className="title"><h1> Check out these cool Tees</h1></div>
      {allProducts.map(product => {
        return <ProductCard key={product.id} product={product} />
      })}
    </div>
  )
}

 export default ProductListing
