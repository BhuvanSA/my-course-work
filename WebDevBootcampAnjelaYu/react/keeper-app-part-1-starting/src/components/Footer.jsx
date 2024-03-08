import React from "react";

function Header() {
  const d = new Date();
  const year = d.getFullYear();
  return (
    <footer>
      <p> C Copyright {year}</p>
    </footer>
  );
}

export default Header;
