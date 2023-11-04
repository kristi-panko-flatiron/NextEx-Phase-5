import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import axios from 'axios';

const UserProfile = () => {
    const [user, setUser] = useState({});
    const [editing, setEditing] = useState(false);
    const history = useHistory();

    useEffect(() => {
        const userId = localStorage.getItem('userId');
        if (userId) {
            axios.get(`http://localhost:5555/profile/${userId}`)
                .then(response => {
                    setUser(response.data);
                })
                .catch(error => {
                    console.error('Error fetching user data:', error);
                });
        } else {
            console.error('User ID not found');
        }
    }, [history]);

    const handleEdit = () => {
        setEditing(true);
    };

    const handleSave = (e) => {
        e.preventDefault(); 
        const userId = localStorage.getItem('userId');
        axios.patch(`http://localhost:5555/profile/${userId}`, user)
            .then(response => {
                setEditing(false);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    };

    const handleDelete = () => {
        const userId = localStorage.getItem('userId');
        axios.delete(`http://localhost:5555/profile/${userId}`)
            .then(response => {
                localStorage.removeItem('userId');
                history.push('/login');
            })
            .catch(error => {
                console.error('Error:', error);
            });
    };

    return (
        <div>
            {editing ? (
                <form onSubmit={handleSave}>
                    <input
                        type="text"
                        placeholder="Name"
                        value={user.name || ''}
                        onChange={(e) => setUser({ ...user, name: e.target.value })}
                    />
                    <input
                        type="text"
                        placeholder="Username"
                        value={user.username || ''}
                        onChange={(e) => setUser({ ...user, username: e.target.value })}
                    />
                    <input
                        type="date"
                        placeholder="Birthday"
                        value={user.birthday || ''}
                        onChange={(e) => setUser({ ...user, birthday: e.target.value })}
                    />
                    <button type="submit">Save Changes</button>
                </form>
            ) : (
                <div>
                    <p>Name: {user.name}</p>
                    <p>Username: {user.username}</p>
                    <p>Birthday: {user.birthday}</p>
                    <p>Astrological Sign: {user.astrological_sign?.sign_name}</p>
                    <p>Sign Description: {user.astrological_sign?.sign_description}</p>
                    <button onClick={handleEdit}>Edit Profile</button>
                    <button onClick={handleDelete}>Delete Account</button>
                </div>
            )}
        </div>
    );
};

export default UserProfile;
