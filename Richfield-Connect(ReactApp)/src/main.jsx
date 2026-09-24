import React from "react"; //Import react element from react library
import ReactDOM from "react-dom/client"; //Import ReactDom element from React=dom/client
import { BrowserRouter } from "react-router-dom";//Import BrowserRouter from react-router-dom

import App from "./App"; //import App from app file
import { AppProvider } from "./context/AppProvider"; //import appprovider from context folder


import "./index.css"; //import index stling file

ReactDOM.createRoot(document.getElementById("root")).render( //Rendering app with different functionalities included
  <React.StrictMode>
    <BrowserRouter>
      <AppProvider>
        <App />
      </AppProvider>
    </BrowserRouter>
  </React.StrictMode>
);