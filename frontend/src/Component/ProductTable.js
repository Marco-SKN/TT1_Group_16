import { useState, useEffect } from "react";
import axios from "axios";
import Product from "./Product";

const ProductTable = () => {
  const [productList, setProductList] = useState([]);
  useEffect(() => {
    getProduct();
  }, []);

  const getProduct = async () => {
    const products = await axios.get("https://fakestoreapi.com/products");
    setProductList(products.data);
    console.log(products.data);
  };

  return (
    <div className="product-container">
      {productList.map((product) => {
        return (
          <Product
            key={product.id}
            image={product.image}
            price={product.price}
            title={product.title}
          />
        );
      })}
    </div>
  );
};

export default ProductTable;
