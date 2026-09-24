import { NavLink } from "react-router-dom"; //Import Navbar link from react router dom
import "../styles/Navbar.css";//Import navbar css

function Navbar() {// Navbar function declaration
  return (
    <nav className="navbar">

      <div className="logo">
        Richfield Connect
      </div>

      <ul className="nav-links"> {/*List of navigatonal links*/}

        <li>
          <NavLink to="/">Home</NavLink>{/*Link to Home page*/}
        </li>

        <li>
          <NavLink to="/about">About</NavLink>{/*Link to About page section*/}
        </li>

        <li>
          <NavLink to="/signup">Sign Up</NavLink>{/*Link to Signup section page*/}
        </li>

        <li>
          <NavLink to="/profile">Profile</NavLink>{/*Link tp profile page section */}
        </li>

        <li>
          <NavLink to="/feed">Feed</NavLink>{/*Link to feed paeg section*/}
        </li>

      </ul>

    </nav>
  );
}

export default Navbar;