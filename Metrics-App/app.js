import React, { useState, useEffect } from 'react';
import './app.css';
import DomainMenu from './src/domainMenu';
import LibraryTable from './src/libraryTable';

function App() {
    const [selectedDomain, setSelectedDomain] = useState('');
    const [selectedLibraries, setSelectedLibraries] = useState([]);

    const domains = ['Testing', 'Logging', 'Utilities', 'Mocking', 'Cryptography', 'JSON', 'Databases', 'Security', 'Object-relational Mapping', 'XML Processing', 'Mail Client', 'Collections', 'Machine Learning'];

    const handleDomainSelect = (domain) => {
        setSelectedDomain(domain);

        fetch(`http://localhost:3000/libraries/${domain}`)
            .then((response) => response.json())
            .then((data) => {
                setSelectedLibraries(data);
            })
            .catch((error) => console.error(error));
    };

    return (
        <div className="App">
            <DomainMenu domains={domains} onDomainSelect={handleDomainSelect} />
            <LibraryTable libraries={selectedLibraries} />
        </div>
    );
}

export default App;
