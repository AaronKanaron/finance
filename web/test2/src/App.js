import './App.scss';
import Footer from './molecules/footer';
import Navbar from './molecules/navbar';

function App() {
  return (
    <div className="App">
      <Navbar></Navbar>

      <section className="hero">
      {/* <div className='bigblur'></div> */}

        <div className='section-container'>
          <div className='box-container'>
            {/* <h1>Trading made easy</h1> */}
            <div className='herotitle'>
              <span className='title-news'>
                Promo 'ilovelean' for 15% off first purchase!
              </span>
              <h1>Quantitative analysis for<br/> everyday people</h1>
              <div className='cta-button'>
                <a href='/plans'>
                  <span>
                    Get started with Stocklighter
                  </span>
                </a>
              </div>
            </div>
            <div className='box'>
              <h1>image of stocklighter in use</h1>
            </div>
          </div>
      </div>

      </section>
        
      <section className='testimonials default'>
        <div className='section-container'>
          <h2>Read our testimonials</h2>
        </div>
      </section>
      <Footer></Footer>
    </div>
  );
}

export default App;