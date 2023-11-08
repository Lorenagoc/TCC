import React, { useState } from "react";

const defaultValue = {
    domain: '',
    sidebar: false,
    data: [],
    selectedLibrary1: {},
    selectedLibrary2: {}
};

export const MetricsContext = React.createContext({});

export const MetricsProvider = (props) => {
    const [domain, setDomain] = useState(defaultValue.domain);
    const [sidebar, setSidebar] = useState(defaultValue.sidebar);
    const [data, setData] = useState(defaultValue.data);
    const [selectedLibrary1, setSelectedLibrary1] = useState(defaultValue.selectedLibrary1);
    const [selectedLibrary2, setSelectedLibrary2] = useState(defaultValue.selectedLibrary2);
  
    return (
      <MetricsContext.Provider value={{
        domain,
        setDomain,
        sidebar,
        setSidebar,
        data,
        setData,
        selectedLibrary1,
        setSelectedLibrary1,
        selectedLibrary2,
        setSelectedLibrary2
      }}>
        {props.children}
      </MetricsContext.Provider>
    );
  };
  

export const MetricsConsumer = MetricsContext.Consumer;