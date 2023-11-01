import React from 'react';

const LibraryTable = ({ libraries }) => {
  if (libraries.length === 0) {
    return <div>Nenhuma biblioteca selecionada.</div>;
  }

  return (
    <div className="library-table">
      <table>
        <thead>
          <tr>
            <th>Nomes</th>
            <th>Popularidade</th>
            <th>Downloads</th>
            <th>Frequência média de releases</th>
            <th>Issues abertos</th>
            <th>Qtde de perguntas</th>
            <th>Estrelas</th>
            <th>Última modificação</th>
            <th>Penúltima modificação</th>
          </tr>
        </thead>
        <tbody>
          {libraries.map((library, index) => (
            <tr key={index}>
              <td>{library.Nomes}</td>
              <td>{library.Popularidade}</td>
              <td>{library.Downloads}</td>
              <td>{library['Frequência média de releases']}</td>
              <td>{library['Issues abertos']}</td>
              <td>{library['Qtde de perguntas']}</td>
              <td>{library.Estrelas}</td>
              <td>{library['Última modificação']}</td>
              <td>{library['Penúltima modificação']}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default LibraryTable;
