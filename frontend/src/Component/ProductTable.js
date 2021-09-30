import { useState } from "react";
import Product from "./Product";
import React from "react";

const ProductTable = ({ productList, onAdd }) => {
  const [quantity, setQuantity] = useState("1");

  return (
    <div className="product-container">
      {productList.map((product) => {
        return (
          <Product
            key={product.id}
            image={product.image}
            description={product.description}
            price={product.price}
            title={product.title}
            onAdd={onAdd.bind(this, product, quantity)}
          />
        );
      })}
    </div>
  );
};

export default ProductTable;
