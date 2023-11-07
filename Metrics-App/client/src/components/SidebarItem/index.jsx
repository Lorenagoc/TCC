import React from 'react'
import { Container } from './styles'

const SidebarItem = ({ Icon, Text }) => {

  const handleClick = (_Text) => {
    console.log("value -> ", _Text);
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