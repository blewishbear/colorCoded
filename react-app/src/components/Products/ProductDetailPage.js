import React, { useState, useEffect } from 'react';
import { useHistory, useParams } from 'react-router-dom';


const ProductDetailPage = () => {
    const { color_id, size_id } = useParams();
    const history = useHistory();

    const [isLoaded, setIsLoaded] = useState(false);
    const [product, setProduct] = useState(null)
    const [setImages, setImages] =useState('')

    useEffect(() => {
        const getProduct = async () => {
            const response = await fetch(`/api/t-shirts/${color_id}/${size_id}`)
            const body = await response.json()
            console.log(body)

            setProduct(body.product)
            isLoaded(true)
        }
        getProduct()
    }, [id])

    const handleRedirect = () => {
        history.push('/t-shirts')
    }

    return (
            <div className="product__design container">
                <div className="product__design-content">


                </div>

            </div>

    )
}
