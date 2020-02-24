import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css';

function HomePage() {
  return (
    <div className="App">
      <header className="App-header">
        <p>Becas y convocatorias</p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="*" redirectTo="/" />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
