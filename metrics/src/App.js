import React from 'react';
import Menu from './menu/Menu';
import Home from './home/Home';
import Rodape from './rodape/Rodape';

const App = () => {

    return (
      <div className="container-fluid">
        <Menu />
        <Home />
        <Rodape />
      </div>
    );
  }

export default App;
