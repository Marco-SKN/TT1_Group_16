import React from "react";

const Footer = () => {
  const currentYear = new Date().getFullYear();
  return (
    <footer>
      <p className="footer-links">

        <a href="peiyuan97@gmail.com" target="_blank">
          Need any help?
        </a>
      </p>
      <p>
        &copy; {currentYear} <strong>Shopping</strong> - Online Shoping Store
      </p>
    </footer>
  );
};

export default Footer;
