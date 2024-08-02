import React from 'react'
import "./navbar.scss"

const Navbar = () => {
    return (
        <div className="navbar-aligner">
            <div className="navbar-blur"></div>
            <div className="navbar-container">
                <div className="navbar">
                    <div className="logo">
                        <div className="logo-placeholder">
                            <img alt=""/>
                        </div>
                        <p>Stocklighter</p>
                    </div>
                    <div className="links">
                        <ul className="link-container">
                            <li className="link">
                                <a href="/">
                                    <p>How it works</p>
                                </a>
                            </li>
                            <li className="link">
                                <a href="/">
                                    <p>Our services</p>
                                </a>
                            </li>
                            <li className="link">
                                <a href="/">
                                    <p>About us</p>
                                </a>
                            </li>
                            <li className="link">
                                <a href="/">
                                    <p>Contact</p>
                                </a>
                            </li>
                        </ul>
                    </div>
                    <div className="action">
                        <div className="login">
                            <a href='/'>Sign in</a>
                        </div>
                        <div className="signin">
                            <a href='/'>Sign up</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
 
export default Navbar;