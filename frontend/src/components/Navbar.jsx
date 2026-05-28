import "./Navbar.css";

function Navbar() {
  return (
    <div className="navbar">

      <h2>
      ESG EmissionHub
      </h2>

      <div className="nav-links">

        <a href="/dashboard">
          Dashboard
        </a>

        <a href="/upload">
          Upload
        </a>

        <a href="/review">
          Review
        </a>

      </div>

    </div>
  );
}

export default Navbar;