import React from "react";

const Product = ({ image, title, description, price }) => {
  return (
    <div className="product">
      <img src={image} alt="table" />
      <h3>{title}</h3>
      <p>{description}</p>
      <span>${price}</span>
      <button>Add to cart</button>
    </div>
  );
};

export default Product;
