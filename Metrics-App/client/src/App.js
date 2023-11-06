import React from "react";
import "./App.css";
import Header from "./components/Header";
import SelectComponent from "../src/components/Select/index";

const App = () => {
  
  return (
    <div className="App">
      <Header />
      <SelectComponent/>
    </div>

  )
};

export default App;