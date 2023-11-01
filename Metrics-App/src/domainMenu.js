import React from 'react';

const DomainMenu = ({ domains, onDomainSelect }) => {
  return (
    <div className="domain-menu">
      <h2>Domínios</h2>
      <ul>
        {domains.map((domain, index) => (
          <li key={index} onClick={() => onDomainSelect(domain)}>
            {domain}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DomainMenu;
