import React from 'react';
import { Link, useHistory } from 'react-router-dom';
import '../index.css';

const NavBar = () => {
    const history = useHistory();

    const handleLogout = () => {
        // Remove the user's ID from localStorage
        localStorage.removeItem('userId');

        // Redirect to the home page
        history.push('/');
    };

    return (
        <nav className="nav-bar">
            <ul className="nav-links">
                <li><Link to="/">Home</Link></li>
                <li><Link to="/profile">Profile</Link></li>
                <li><Link to="/login">Login</Link></li>
                <li><Link to="/signup">Sign Up</Link></li>
                <li><Link to="/matches">Match Now</Link></li>
                <li><Link to="/my-matches">My Matches</Link></li>
                <li>
                    <button onClick={handleLogout} className="nav-button-link">Logout</button>
                </li>
            </ul>
        </nav>
    );
};

export default NavBar;