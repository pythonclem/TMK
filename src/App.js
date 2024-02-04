import './App.css';
import { GiHamburgerMenu } from 'react-icons/gi';
import Form from './components/Form';

function App() {
  return (
    <div className='app'>
      <nav className='navbar'>
        <h4>The Morning Kickoff</h4>
        <GiHamburgerMenu />
      </nav>
      <div className='hero'>
        <h1 className='hero__heading'>Enter headline for hero</h1>
        <h4 className='hero__subheading'>
          Get all the next games! NFL, NBA, Champions League, and WAY more -
          straight to your inbox
        </h4>
      </div>
      <Form />
      <footer className='footer'>
        <p className='footer__text'>&copy; The Morning Kickoff 2024</p>
      </footer>
    </div>
  );
}

export default App;
