import "../styles/About.css";

function About() {

  const guidelines = [
    "Respect fellow students.",
    "Share academic content responsibly.",
    "Maintain professionalism.",
    "Protect personal information.",
    "Support collaborative learning."
  ];

  return (
    <div className="about-page">

      <h1>About Richfield Connect</h1>

      <p className="purpose">
        Richfield Connect is an academic
        networking platform designed to help
        Richfield students collaborate, learn,
        and build professional relationships.
      </p>

      <h2>Community Guidelines</h2>

      <ul className="guidelines">

        {guidelines.map((item, index) => (
          <li key={index}>{item}</li>
        ))}

      </ul>

      <div className="contact">

        <h2>Contact Information</h2>

        <p>
          Email:
          402604793@richfieldconnect.ac.za
        </p>

        <p>
          Location:
          Richfield Graduate Institute of Technology
        </p>

      </div>

    </div>
  );
}

export default About;
