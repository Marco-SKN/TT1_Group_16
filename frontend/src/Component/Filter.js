import React from "react";

const Filter = () => {
  return (
    <>
      <select>
        <option>Filter by category</option>
        <option value="1">Electronics</option>
        <option value="2">Jewelery</option>
        <option value="3">Men's clothing</option>
        <option value="4">Women's clothing</option>
      </select>
    </>
  );
};

export default Filter;
