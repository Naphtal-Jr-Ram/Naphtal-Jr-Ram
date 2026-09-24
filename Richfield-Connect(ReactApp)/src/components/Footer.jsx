import { Link } from "react-router-dom"; //Import link to navigate different pages from react-router-dom
import "../styles/Footer.css";//Import fotter css code from the styles file.

function Footer() { //footer function declaration
  return (
    <footer className="footer"> {/*opening footer declaration*/}

      <div className="footer-content">

        <h3>Richfield Connect</h3>

        <p>
          Empowering academic collaboration and
          professional student networking.
        </p>

        <div className="footer-links"> {/*Division for footer links*/}

          <Link to="/">Home</Link>{/*Link to home page*/}

          <Link to="/about">About</Link>{/*Link to About page*/}

          <Link to="/signup">Register</Link>{/*Link to signup page*/}

        </div>

        <p className="copyright">
          <span>{'\u00A9'} 2026| Created by Ramawa Naphtal Junior</span>{/*WebApp copyright notice*/}
        </p>

      </div>

    </footer>
  );
}

export default Footer;