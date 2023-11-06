// NavBar.js
import React from 'react';
import { Link } from 'react-router-dom';
import '../index.css'

const NavBar = () => {
    return (
        <nav className="nav-bar">
            <ul className="nav-links">
                <li>
                    <Link to="/">Home</Link>
                </li>
                <li>
                    <Link to="/profile">Profile</Link>
                </li>
                <li>
                    <Link to="/login">Login</Link>
                </li>
                <li>
                    <Link to="/signup">Sign Up</Link>
                </li>
                <li>
                    <Link to="/matches">Match Now</Link>
                </li>
            </ul>
        </nav>
    );
};

export default NavBar;