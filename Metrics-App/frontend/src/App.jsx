import {useState, useEffect} from 'react';

function App() {
  const [metrics, setMetrics] = useState(false);

  function getMetrics() {
    fetch('http://localhost:5173')
      .then(response => {
        return response.text();
      })
      .then(data => {
        setMetrics(data);
      });
  }

  useEffect(() => {
    getMetrics();
  }, []);
  return (
    <div>
      {metrics ? metrics : 'There is no metric data available'}
    </div>
  );
}
export default App;