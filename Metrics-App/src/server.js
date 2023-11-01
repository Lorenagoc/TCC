const express = require('express');
const app = express();
const port = 3000;

const { Pool } = require('pg');

// Configuração da conexão com o banco de dados PostgreSQL
const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'metrics',
  password: 'root',
  port: 5432,
});

app.get('/', (req, res) => {
  res.send('Bem-vindo à minha aplicação!');
});

// Rota para buscar dados da tabela
app.get('/libraries/:domain', async (req, res) => {
  const { domain } = req.params;

  try {
    const query = `
      SELECT *
      FROM results
      WHERE dominio = $1
    `;

    const { rows } = await pool.query(query, [domain]);
    res.json(rows);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Erro ao buscar os dados.' });
  }
});

app.listen(port, () => {
  console.log(`Servidor está em execução na porta ${port}`);
});
