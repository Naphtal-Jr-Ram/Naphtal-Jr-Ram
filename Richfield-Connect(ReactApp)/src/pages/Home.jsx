import { Link } from "react-router-dom";
import "../styles/Home.css";

function Home() {
  return (
    <div className="home-page">

      <section className="hero">

        <h1>Richfield Connect</h1>

        <p>
          Connect. Collaborate. Grow.
        </p>

        <p>
          A professional academic networking
          platform built exclusively for Richfield students.
        </p>

        <Link
          to="/signup"
          className="register-btn"
        >
          Register Now
        </Link>

      </section>

      <section className="features">

        <div className="feature-card">
          <h3>Connect With Peers</h3>
          <p>
            Build meaningful academic connections.
          </p>
        </div>

        <div className="feature-card">
          <h3>Share Ideas</h3>
          <p>
            Post insights, questions and academic content.
          </p>
        </div>

        <div className="feature-card">
          <h3>Build Your Profile</h3>
          <p>
            Showcase your interests and achievements.
          </p>
        </div>

      </section>

    </div>
  );
}

export default Home;