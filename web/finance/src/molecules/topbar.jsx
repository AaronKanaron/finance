import React from 'react'
import "./topbar.scss"

const Topbar = () => {
    return (
        <div className='topbar'>
            <div className="link-container">
                <div className="logo-border">
                    <div className="logo">
                        N
                    </div>
                </div>
                <ul className="links">
                    <li className="link">
                        <a href="/">
                            How it works
                        </a>
                    </li>
                    <li className="link">
                        <a href="/">
                            Our services
                        </a>
                    </li>
                    <li className="link">
                        <a href="/">
                            About us
                        </a>
                    </li>
                </ul>
            </div>
            <div className="actions">
                <div className="signin">
                    Sign In
                </div>
                <div className="login">
                    Log In
                </div>
            </div>
        </div>
    );
}
 
export default Topbar;