import './App.scss';
import WebGLCanvas from './atoms/WebGlCanvas';
import Topbar from './molecules/topbar';


function App() {
  return (
    <div className="App">

      Kvantitativ Analys för vardagligt folk
      <Topbar></Topbar>
      <WebGLCanvas />
    </div>
  );
}

export default App;
