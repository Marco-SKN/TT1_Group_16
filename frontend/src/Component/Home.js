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

  let config = {
    headers: {
      Authorization:
        "Bearer " +
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MzMwNzEwNTgsImlhdCI6MTYzMjk4NDY1OCwic3ViIjoxfQ.owyVsgNDQSx-ipbnMr98lHLTVMpbLoIKOcKt7c9Hmhc",
    },
  };

  useEffect(() => {
    getProduct();
  }, []);

  const getProduct = async () => {
    const products = await axios.get(
      "https://cors-anywhere.herokuapp.com/https://api.danieltan.org/api/products",
      config
    );
    setProductList(products.data);

    console.log(products.data);
  };

  const searchQuery = (text) => {
    const query = new RegExp(text, "i");
    setSearchList(productList.filter((item) => item.title.match(query)));
    if (text == "") {
      setSearchList("");
    }
  };

  const setFilter = (category) => {
    setFilterList(productList.filter((item) => item.category_id == category));
    if (category === "none") {
      setFilterList("");
    }
  };

  const onAdd = (item, quantity) => {
    console.log(item, quantity);
  };
  return (
    <section className="home">
      <Link to="/cart">Cart</Link>
      <div className="search-container">
        <Search searchQuery={searchQuery} />
        <Filter setFilter={setFilter} />
      </div>

      <ProductTable
        productList={filterList || searchList || productList}
        onAdd={onAdd}
      />
    </section>
  );
};

export default Home;
