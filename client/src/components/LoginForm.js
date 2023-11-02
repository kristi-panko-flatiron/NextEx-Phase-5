import React, { useState } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom';

const LoginForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    let history = useHistory();

    const handleLogin = (e) => {
        e.preventDefault();
        axios.post('http://localhost:5555/login', { username, password })
            .then(response => {
                // Store the user ID in local storage
                localStorage.setItem('userId', response.data.user_id);
                history.push('/matches');
            })
            .catch(error => {
                console.error("Error logging in", error);
            });
    };


    return (
        <form onSubmit={handleLogin}>
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
            <button type="submit">Login</button>
        </form>
    );
};

export default LoginForm;
