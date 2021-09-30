import Product from "./Product";

const ProductTable = ({ productList }) => {
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
          />
        );
      })}
    </div>
  );
};

export default ProductTable;
