import React, { useState } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom'; // Import useHistory from react-router-dom

const SignUpForm = () => {
    const [name, setName] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [birthday, setBirthday] = useState('');
    let history = useHistory(); // Access the history object

    const handleSignUp = (e) => {
        e.preventDefault();
        axios
            .post('http://localhost:5555/register', {
                name: name,
                username: username,
                password: password,
                birthday: birthday
            })
            .then(response => {
                // Handle successful signup
                console.log(response.data); // Assuming the response contains the new user data
                history.push('/profile'); // Redirect to the profile page after successful signup
            })
            .catch(error => {
                // Handle signup failure
                console.error('Error signing up', error);
            });
    };

    return (
        <form onSubmit={handleSignUp}>
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
    );
};

export default SignUpForm;