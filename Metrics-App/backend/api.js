import { Pool } from "pg";

const pool = new Pool({
  user: "postgres",
  host: "localhost",
  database: "metrics",
  password: "root",
  port: 5432,
});

const getMetrics = async () => {
  try {
    return await new Promise(function (resolve, reject) {
      pool.query("SELECT * FROM results", (error, results) => {
        console.log("results", results);
        if (error) {
          reject(error);
        }
        if (results && results.rows) {
          resolve(results.rows);
        } else {
          reject(new Error("No results found"));
        }
      });
    });
  } catch (error_1) {
    console.error(error_1);
    throw new Error("Internal server error");
  }
};

export default {
  getMetrics,
};