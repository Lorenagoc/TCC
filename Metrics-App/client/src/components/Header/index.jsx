import React, { useContext } from 'react';
import { Container, TitleContainer, Title } from './styles';
import { FaBars } from 'react-icons/fa';
import Sidebar from '../Sidebar';
import { MetricsContext } from '../MetricsContext';
import { Chip } from '@mui/material';

const Header = () => {
  const { sidebar, setSidebar, domain } = useContext(MetricsContext);

  const showSidebar = () => setSidebar(!sidebar);

  return (
    <Container>
      <TitleContainer>
        <FaBars onClick={showSidebar} style={{ color: 'white', width: '30px', height: '30px', cursor: 'pointer' }} />
        <Title sidebar={sidebar}>Metrics App</Title>
      </TitleContainer>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'flex-end' }}>
        <Chip label={domain || 'Nenhum domínio foi selecionado ainda'} variant="outlined" color="warning" />
      </div>
      {sidebar && <Sidebar />}
    </Container>
  );
};

export default Header;
