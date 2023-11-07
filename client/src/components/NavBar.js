import React, { useContext } from 'react';
import { Link, useHistory } from 'react-router-dom';
import { AuthContext } from './AuthContext'; 
import '../index.css';

const NavBar = () => {
    const history = useHistory();
    const { isLoggedIn, setIsLoggedIn } = useContext(AuthContext);

    const handleLogout = () => {
        localStorage.removeItem('userId');
        setIsLoggedIn(false); 
        history.push('/login');
    };

    return (
        <nav className="nav-bar">
            <ul className="nav-links">
                <li><Link to="/">Home</Link></li>
                <li><Link to="/profile">Profile</Link></li>
                {!isLoggedIn && <li><Link to="/login">Login</Link></li>}
                <li><Link to="/signup">Sign Up</Link></li>
                <li><Link to="/matches">Match Now</Link></li>
                <li><Link to="/my-matches">My Matches</Link></li>
                {isLoggedIn && (
                    <li>
                        <button onClick={handleLogout} className="nav-button-link">Logout</button>
                    </li>
                )}
            </ul>
        </nav>
    );
};

export default NavBar;
