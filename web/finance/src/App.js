import './App.scss';
import WebGLCanvas from './atoms/WebGlCanvas';
import Topbar from './molecules/topbar';


function App() {
  return (
    <div className="App">

      Kvantitativ Analys för vardagligt folk

      <Topbar></Topbar>
      <WebGLCanvas />

      <header>
        {/* <h1>Trading,<br />made easy</h1> */}
        <h1 className='test'>Quantitative Analysis<br />for everyday people</h1>
      </header>
    </div>
  );
}

export default App;
