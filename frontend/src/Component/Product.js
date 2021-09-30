import { useState } from "react";

const Product = ({ image, title, description, price, onAdd }) => {
  const [quantity, setQuantity] = useState("1");

  return (
    <div className="product">
      <img src={image} alt="table" />
      <h3>{title}</h3>
      <p>{description}</p>
      <span>${price}</span>
      <button onClick={onAdd}>Add to cart</button>
      <input
        type="text"
        className="qty"
        value={quantity}
        onChange={(e) => setQuantity(e.target.value)}
      />
    </div>
  );
};

export default Product;
