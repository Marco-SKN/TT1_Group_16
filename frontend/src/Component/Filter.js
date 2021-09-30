import React from "react";

const Filter = ({ setFilter }) => {
  return (
    <>
      <select onChange={(e) => setFilter(e.target.value)}>
        <option value="none">Filter by category</option>
        <option value="electronics">Electronics</option>
        <option value="jewelery">Jewelery</option>
        <option value="men's clothing">Men's clothing</option>
        <option value="women's clothing">Women's clothing</option>
      </select>
    </>
  );
};

export default Filter;
