import React from 'react';
import { Link } from 'react-router-dom'; 
import LoginForm from './LoginForm'; 
import SignUpForm from './SignUpForm'; 

const HomePage = () => {
    return (
        <div className="home-container">
            <h1 className="app-title gradient-text">NextEx</h1> {/* Add a class name to the h1 tag */}
            <br></br>
            <br></br>
            <br></br>
            <br></br>
            <br></br>
            <br></br>
            <br></br>
            <br></br>
            <br></br>
            <br></br>            <br></br>
            <br></br>
            <h2>NextEx is a dating app designed for daters who are ready to put it all on the line. With our unique matching technology, you will either find your soulmate, or your next ex.</h2>
            <br></br>
            <br></br>
            <br></br>
            <br></br>
            <br></br>
            <br></br>         <br></br>
            <br></br>
            <br></br>         <br></br>
            <br></br>
            <br></br>
            {/* <div className="form-container">
                <h2>Login</h2>
                <LoginForm />
            </div>
            <div className="form-container">
                <h2>Sign Up</h2>
                <SignUpForm />
    </div>*/}
            {/* <div className="login-link-container">
                <Link to="/login">Log In</Link>
            </div>  */}
        </div>
    );
};

export default HomePage;
