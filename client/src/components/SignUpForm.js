// SignUpForm.js
import React, { useState } from 'react';

const SignUpForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [birthday, setBirthday] = useState('');

    const handleSignUp = (e) => {
        e.preventDefault();
        // Add logic to make a POST request to register a new user
    };

    return (
        <form onSubmit={handleSignUp}>
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
    );
};

export default SignUpForm;

