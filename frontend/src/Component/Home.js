import { useState, useEffect } from "react";
import axios from "axios";
import ProductTable from "./ProductTable";
import Search from "./Search";
import Filter from "./Filter";
import { Link } from "react-router-dom";

const Home = () => {
  const [productList, setProductList] = useState([]);
  const [searchList, setSearchList] = useState("");
  const [filterList, setFilterList] = useState("");

  useEffect(() => {
    getProduct();
  }, []);

  const getProduct = async () => {
    const products = await axios.get("https://fakestoreapi.com/products");
    setProductList(products.data);
  };

  const searchQuery = (text) => {
    const query = new RegExp(text, "i");
    setSearchList(productList.filter((item) => item.title.match(query)));
    if (text == "") {
      setSearchList("");
    }
  };

  const setFilter = (category) => {
    setFilterList(productList.filter((item) => item.category === category));
    if (category === "none") {
      setFilterList("");
    }
  };

  return (
    <section className="home">
      <Link to="/cart">Cart</Link>
      <div className="search-container">
        <Search searchQuery={searchQuery} />
        <Filter setFilter={setFilter} />
      </div>

      <ProductTable productList={filterList || searchList || productList} />
    </section>
  );
};

export default Home;
