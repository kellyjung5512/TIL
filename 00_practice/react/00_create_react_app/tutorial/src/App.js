import logo from './logo.svg';
import './App.css';
import Button from "@material-ui/core/Button";
import Card from "./Card.js"

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <Button variant="text">Text</Button>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <Card></Card>
      </header>
    </div>
  );
}

export default App;
