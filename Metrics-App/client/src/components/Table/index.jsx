import React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { TableContainerStyles } from './styles';

export default function BasicTable({ selectedLibrary }) {

  return (
    <TableContainerStyles>
      <TableContainer component={Paper}>
        <Table aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell colSpan={8} style={{ fontWeight: 'bold', textAlign: 'center', backgroundColor: '#939699' }}>
                {selectedLibrary?.nomes}
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
              key={selectedLibrary?.nomes}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell align="right">{selectedLibrary?.popularidade}</TableCell>
              <TableCell align="right">{selectedLibrary?.downloads}</TableCell>
              <TableCell align="right">{selectedLibrary?.freq_media_releases}</TableCell>
              <TableCell align="right">{selectedLibrary?.issues_abertos}</TableCell>
              <TableCell align="right">{selectedLibrary?.qtde_perguntas}</TableCell>
              <TableCell align="right">{selectedLibrary?.estrelas}</TableCell>
              <TableCell align="right">{selectedLibrary?.ultima_modificacao}</TableCell>
              <TableCell align="right">{selectedLibrary?.penultima_modificacao}</TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </TableContainer>
    </TableContainerStyles>
  );
}