import React from "react";

const Product = ({ image, title, price }) => {
  return (
    <div className="product">
      <img src={image} alt="table" />
      <h3>{title}</h3>
      <span>${price}</span>
      <button>Add to cart</button>
    </div>
  );
};

export default Product;
