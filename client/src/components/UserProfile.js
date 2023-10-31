import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';

const UserProfile = () => {
    const [user, setUser] = useState({});
    const [editing, setEditing] = useState(false);
    const history = useHistory();

    useEffect(() => {
        fetch('/api/userData')
            .then(response => response.json())
            .then(data => {
                setUser(data);
            })
            .catch(error => {
                console.error('Error fetching user data:', error);
            });
    }, []);

    const handleEdit = () => {
        setEditing(true);
    };

    const handleSave = () => {
        fetch(`/api/users/${user.id}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(user)
        })
            .then(response => response.json())
            .then(data => {
                setEditing(false);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    };

    const handleDelete = () => {
        fetch(`/api/users/${user.id}`, {
            method: 'DELETE'
        })
            .then(response => response.json())
            .then(data => {
                // Handle successful deletion
                // You might want to redirect the user to the login page or perform any other necessary actions
                history.push('/login'); // Redirect to the login page
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
                    <button onClick={handleEdit}>Edit Profile</button>
                    <button onClick={handleDelete}>Delete Account</button>
                </div>
            )}
        </div>
    );
};

export default UserProfile;
