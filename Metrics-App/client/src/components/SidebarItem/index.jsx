import React, { useContext } from 'react'
import { Container } from './styles'
import { MetricsContext } from '../MetricsContext';

const SidebarItem = ({ Icon, Text }) => {
  const { setDomain } = useContext(MetricsContext);
  const { setSidebar } = useContext(MetricsContext);

  const handleClick = (_Text) => {
    setDomain(_Text);
    setSidebar(false);
  };

  return (
    <div onClick={(_) => handleClick(Text)}>
      <Container>
        <Icon />
        {Text}
      </Container>
    </div>
  );
}

export default SidebarItem