import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import axios from 'axios';

const UserProfile = () => {
    const [user, setUser] = useState({});
    const [editing, setEditing] = useState(false);
    const history = useHistory();

    useEffect(() => {
        axios.get('http://localhost:5555/profile')
            .then(response => {
                setUser(response.data);
            })
            .catch(error => {
                console.error('Error fetching user data:', error);
            });
    }, []);

    const handleEdit = () => {
        setEditing(true);
    };

    const handleSave = () => {
        axios.patch('http://localhost:5555/profile', user)
            .then(response => {
                setEditing(false);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    };

    const handleDelete = () => {
        axios.delete('http://localhost:5555/profile')
            .then(response => {
                history.push('/login');
            })
            .catch(error => {
                console.error('Error:', error);
            });
    };

    return (
        <div>
            {editing ? (
                <form>
                    <input
                        type="text"
                        placeholder="Name"
                        value={user.name}
                        onChange={(e) => setUser({ ...user, name: e.target.value })}
                    />
                    <input
                        type="text"
                        placeholder="Username"
                        value={user.username}
                        onChange={(e) => setUser({ ...user, username: e.target.value })}
                    />
                    <input
                        type="password"
                        placeholder="Password"
                        value={user.password}
                        onChange={(e) => setUser({ ...user, password: e.target.value })}
                    />
                    <input
                        type="date"
                        placeholder="Birthday"
                        value={user.birthday}
                        onChange={(e) => setUser({ ...user, birthday: e.target.value })}
                    />
                    {/* Add other necessary form fields */}
                    <button onClick={handleSave}>Save Changes</button>
                    <button onClick={handleDelete}>Delete Account</button>
                </form>
            ) : (
                <div>
                    <p>Name: {user.name}</p>
                    <p>Username: {user.username}</p>
                    <p>Birthday: {user.birthday}</p>
                    <p>Astrological Sign: {user.astrological_sign}</p> {/* New line added */}
                    <button onClick={handleEdit}>Edit Profile</button>
                    <button onClick={handleDelete}>Delete Account</button>
                </div>
            )}
        </div>
    );
};

export default UserProfile;