import React, { useState } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom';
import '../index.css'; 
import { useContext } from 'react';
import { AuthContext } from './AuthContext'; // adjust the import path as needed

const LoginForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const { setIsLoggedIn } = useContext(AuthContext);
    let history = useHistory();


    // const handleLogin = (e) => {
    //     e.preventDefault();
    //     axios.post('http://localhost:5555/login', { username, password })
    //         .then(response => {
    //             // Store the user ID in local storage
    //             localStorage.setItem('userId', response.data.user_id);
    //             history.push('/matches');
    //         })
    //         .catch(error => {
    //             console.error("Error logging in", error);
    //         });
    // };
    const handleLogin = (e) => {
        e.preventDefault();
        axios.post('http://localhost:5555/login', { username, password })
            .then(response => {
                // Store the user ID in local storage
                localStorage.setItem('userId', response.data.user_id);
                // Update the login state in context
                setIsLoggedIn(true); // This function should be provided by useContext(AuthContext)
                history.push('/matches');
            })
            .catch(error => {
                console.error("Error logging in", error);
            });
    };

    return (
        <div className="login-container">
            <h1 className="gradient-text">Login</h1>
            <h2>Log in to your account and start matching!</h2>
            <form onSubmit={handleLogin} className="login-form">
                <div>
                    <input
                        type="text"
                        placeholder="Username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                </div>
                <div>
                    <input
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </div>
                <div>
                    <button type="submit">Login</button>
                </div>
            </form>
        </div>
    );
};

export default LoginForm;
