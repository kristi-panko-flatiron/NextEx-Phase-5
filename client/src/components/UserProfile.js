import React, { useState, useEffect } from 'react';

const UserProfile = () => {
    const [user, setUser] = useState({});
    const [editing, setEditing] = useState(false);

    useEffect(() => {
        // Fetch user data from the backend API
        fetch('/api/userData')
            .then(response => response.json())
            .then(data => {
                setUser(data); // Set the fetched user data to the state
            })
            .catch(error => {
                console.error('Error fetching user data:', error);
            });
    }, []);

    const handleEdit = () => {
        setEditing(true);
    };

    const handleSave = () => {
        // Add logic to save the user's updated information using the PATCH method
        // Example code to make a PATCH request
        fetch(`/api/users/${user.id}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(user) // Send the updated user data
        })
            .then(response => response.json())
            .then(data => {
                // Handle the response data accordingly
                setEditing(false);
            })
            .catch(error => {
                // Handle any errors
                console.error('Error:', error);
            });
    };

    return (
        <div>
            {editing ? (
                <form>
                    {/* Render form fields for editing the user's information */}
                    {/* Ensure you populate the form fields with the current user data */}
                    <input
                        type="text"
                        value={user.name}
                        onChange={(e) => setUser({ ...user, name: e.target.value })}
                    />
                    {/* Add other necessary form fields */}
                    <button onClick={handleSave}>Save Changes</button>
                </form>
            ) : (
                <div>
                    {/* Display user's profile information */}
                    <p>Name: {user.name}</p>
                    {/* Add other necessary user data fields */}
                    <button onClick={handleEdit}>Edit Profile</button>
                </div>
            )}
        </div>
    );
};

export default UserProfile;
