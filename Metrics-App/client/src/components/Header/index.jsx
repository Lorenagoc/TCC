import React, { useState } from 'react';
import { Container, TitleContainer, Title } from './styles';
import { FaBars } from 'react-icons/fa';
import Sidebar from '../Sidebar';

const Header = () => {
  const [sidebar, setSidebar] = useState(false);

  const showSidebar = () => setSidebar(!sidebar);

  return (
    <Container>
      <TitleContainer>
        <FaBars onClick={showSidebar} style={{ color: 'white', width: '30px', height: '30px', cursor: 'pointer' }} />
        <Title sidebar={sidebar}>Metrics App</Title>
      </TitleContainer>
      {sidebar && <Sidebar active={setSidebar} />}
    </Container>
  );
};

export default Header;
