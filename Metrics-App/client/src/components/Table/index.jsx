import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { TableContainerStyles } from './styles';

function createData(name, popularity, downloads, releases, issues, questions, stars, lastModification, penultimateModification) {
  return { name, popularity, downloads, releases, issues, questions, stars, lastModification, penultimateModification };
}

const row = createData('JUnit', 159, 6.0, 24, 4.0, 5.0, 7.52, 9.52, 11);


export default function BasicTable() {
  return (
    <TableContainerStyles>
      <TableContainer component={Paper}>
        <Table aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell colSpan={8} style={{ fontWeight: 'bold', textAlign: 'center' }}>
                {row.name}
              </TableCell>
            </TableRow>
            <TableRow>
              <TableCell>Popularidade</TableCell>
              <TableCell align="right">Downloads</TableCell>
              <TableCell align="right">Frequência média de releases</TableCell>
              <TableCell align="right">Issues abertos</TableCell>
              <TableCell align="right">Perguntas</TableCell>
              <TableCell align="right">Estrelas</TableCell>
              <TableCell align="right">Última modificação</TableCell>
              <TableCell align="right">Penúltima modificação</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell align="right">{row.popularity}</TableCell>
              <TableCell align="right">{row.downloads}</TableCell>
              <TableCell align="right">{row.releases}</TableCell>
              <TableCell align="right">{row.issues}</TableCell>
              <TableCell align="right">{row.questions}</TableCell>
              <TableCell align="right">{row.stars}</TableCell>
              <TableCell align="right">{row.lastModification}</TableCell>
              <TableCell align="right">{row.penultimateModification}</TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </TableContainer>
    </TableContainerStyles>
  );
}