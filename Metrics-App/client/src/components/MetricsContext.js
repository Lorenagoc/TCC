import React, { useState } from "react";

const defaultValue = {
    domain: '',
};

export const MetricsContext = React.createContext({});

export const MetricsProvider = (props) => {
    const [domain, setDomain] = useState(defaultValue.domain);
  
    return (
      <MetricsContext.Provider value={{
        domain,
        setDomain,
      }}>
        {props.children}
      </MetricsContext.Provider>
    );
  };
  

export const MetricsConsumer = MetricsContext.Consumer;