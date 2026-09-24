import { Routes, Route } from "react-router-dom"; //Import routes, and rout from react router dom

import Navbar from "./components/Navbar"; //Import Navbar link from components file
import Footer from "./components/Footer"; //Import footer link from components folder

import Home from "./pages/Home"; //import home link from pages folder
import About from "./pages/About";//import about from pages folder 
import Signup from "./pages/Signup"; //import signupcfrom pages folder
import Profile from "./pages/Profile"; //import profile link frpm pages folder
import Feed from "./pages/Feed";// import feed link from pages folder

function App() {

  return (
    <>
      <Navbar /> {/*Display info in navbar*/}

      <main className="main-container">

        <Routes>{/*link routing*/}

          <Route
            path="/"
            element={<Home />}
          />

          <Route
            path="/about"
            element={<About />}
          />

          <Route
            path="/signup"
            element={<Signup />}
          />

          <Route
            path="/profile"
            element={<Profile />}
          />

          <Route
            path="/feed"
            element={<Feed />}
          />

        </Routes>

      </main>

      <Footer /> {/*Footer insertion*/}
    </>
  );
}

export default App;
