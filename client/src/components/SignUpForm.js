import React, { useState } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom';
import '../index.css'

const SignUpForm = () => {
    const [name, setName] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [birthday, setBirthday] = useState('');
    let history = useHistory();

    const handleSignUp = (e) => {
        e.preventDefault();

        const userData = {
            name: name,
            username: username,
            password: password,
            birthday: birthday
        };

        axios.post('http://localhost:5555/register', userData)
            .then(response => {
                console.log(response.data);
                history.push('/profile');
            })
            .catch(error => {
                console.error('Error signing up', error);
            });
    };

    return (
        <div className="signup-form-container">
            <h1 className="gradient-text">Sign Up</h1>
            <h2>Sign up for an account and start matching!</h2>
            <form onSubmit={handleSignUp} className="signup-form">
                <input
                    type="text"
                    placeholder="Name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <input
                    type="date"
                    placeholder="Birthday"
                    value={birthday}
                    onChange={(e) => setBirthday(e.target.value)}
                />
                <button type="submit">Sign Up</button>
            </form>
        </div>
    );
};

export default SignUpForm;
