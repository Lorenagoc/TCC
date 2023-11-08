import React, { useContext, useEffect } from 'react';
import axios from 'axios';
import "./App.css";
import Header from "./components/Header";
import SelectComponent from "../src/components/Select/index";
import { MetricsProvider, MetricsContext } from './components/MetricsContext';

const App = () => {
  const baseURL = 'http://localhost:4000/libraries';
  const { setData } = useContext(MetricsContext);
  const { domain } = useContext(MetricsContext);

  useEffect(() => {
    if (domain !== '') {
      axios.get(`${baseURL}/${domain}`)
        .then(response => {
          setData(response?.data);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }, [domain, setData]);

  return (
    <div className="App">
      <Header />
      <SelectComponent />
    </div>

  )
};

const AppContainer = () => (
  <MetricsProvider>
    <App />
  </MetricsProvider>
);


export default AppContainer;