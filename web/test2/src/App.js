import './App.scss';
import Navbar from './molecules/navbar';

function App() {
  return (
    <div className="App">
      <Navbar></Navbar>

      <section className="hero">
      {/* <div className='bigblur'></div> */}

        <div className='box-container'>
          {/* <h1>Trading made easy</h1> */}
          <div className='herotitle'>
            <span className='title-news'>
              Promo 'ilovelean' for 15% off first purchase!
            </span>
            <h1>Quantitative Analysis for<br/> everyday people</h1>
            <div className='cta-button'>
              <a href='/plans'>
                <span>
                  Get started with Stocklighter
                </span>
              </a>
            </div>
          </div>
          <div className='box'>
            <h1>Place graph here</h1>
          </div>
        </div>
      </section>
      
      <section className=''>

      </section>
      
    </div>
  );
}

export default App;