import React, { useContext, useEffect, useState } from 'react';
import axios from 'axios';
import "./App.css";
import Header from "./components/Header";
import SelectComponent from "../src/components/Select/index";
import { MetricsProvider, MetricsContext } from './components/MetricsContext';

const App = () => {
  const baseURL = 'http://localhost:4000/libraries';
  const [data, setData] = useState(null);
  const { domain, setDomain } = useContext(MetricsContext);

  useEffect(() => {
    axios.get(`${baseURL}/JSON`)
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);
  
  return (
    console.log("data -> ", data),
    <div className="App">
      <Header />
      <SelectComponent/>
    </div>

  )
};

const AppContainer = () => (
  <MetricsProvider>
    <App />
  </MetricsProvider>
);


export default AppContainer;