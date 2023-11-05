import styled from 'styled-components';

export const Container = styled.div`
  height: 100px;
  display: flex;
  background-color: #1A202C;
  box-shadow: 0 0 20px 3px;
`;

export const TitleContainer = styled.div`
  display: flex;
  align-items: center;
  margin-left: 20px;
`;

export const Title = styled.span`
  color: white;
  font-size: 4rem;
  margin-left: ${props => props.sidebar ? '250px' : '8px'};
  padding: 20px;
  animation: showTitle .4s;
`;
