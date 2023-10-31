// HomePage.js
import React from 'react';
import { Link } from 'react-router-dom'; 
import LoginForm from './LoginForm'; 
import SignUpForm from './SignUpForm'; 

const HomePage = () => {
    return (
        <div>
            <h1>Welcome to NextEx!</h1>
            <div>
                <h2>Login</h2>
                <LoginForm />
            </div>
            <div>
                <h2>Sign Up</h2>
                <SignUpForm />
            </div>
            <div>
                <Link to="/profile">Go to Profile</Link>
            </div>
        </div>
    );
};

export default HomePage;
