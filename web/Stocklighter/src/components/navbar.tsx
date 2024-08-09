import React, { useState, useEffect } from 'react'
import "./navbar.scss"

const Navbar: React.FC = () => {
    const [isTop, setIsTop] = useState<boolean>(true);

    useEffect(() => {
        const handleScroll = () => {
            const scrollTop = window.scrollY || document.documentElement.scrollTop;
            setIsTop(scrollTop === 0);
        };

        const throttle = (callback: () => void, limit: number) => {
            let inThrottle: boolean;
            return () => {
                if (!inThrottle) {
                    callback();
                    inThrottle = true;
                    setTimeout(() => inThrottle = false, limit);
                }
            };
        };

        const throttledHandleScroll = throttle(handleScroll, 200);

        window.addEventListener('scroll', throttledHandleScroll);

        handleScroll();

        return () => window.removeEventListener('scroll', throttledHandleScroll);
    }, []);
    
    return (
        <div className={`navbar-aligner ${isTop ? 'top' : ''}`}>
            <div className="navbar-blur nottop"></div>
            <div className="navbar-container">
                <div className="navbar">
                    <div className="logo">
                        {/* <div className="logo-placeholder">
                            <img alt=""/>
                        </div> */}
                        {/* <p>Stocklighter</p> */}
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