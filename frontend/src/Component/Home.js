import { useState, useEffect } from "react";
import axios from "axios";
import ProductTable from "./ProductTable";
import Search from "./Search";

const Home = () => {
  const [productList, setProductList] = useState([]);
  const [searchList, setSearchList] = useState("");

  useEffect(() => {
    getProduct();
  }, []);

  const getProduct = async () => {
    const products = await axios.get("https://fakestoreapi.com/products");
    setProductList(products.data);
  };

  const searchQuery = (text) => {
    const query = new RegExp(text, "i");
    console.log(text);
    setSearchList(productList.filter((item) => item.title.match(query)));
    console.log(searchList);
  };

  return (
    <section className="home">
      <Search searchQuery={searchQuery} />
      <ProductTable
        productList={searchList.length ? searchList : productList}
      />
    </section>
  );
};

export default Home;
