import { useState } from "react";

const Search = ({ searchQuery }) => {
  return (
    <>
      <input
        className="search"
        type="text"
        placeholder="search..."
        onChange={(e) => {
          searchQuery(e.target.value);
        }}
      />
    </>
  );
};

export default Search;
