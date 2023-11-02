import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Card from './Card';
import FavoritesBar from './FavoritesBar';

const MatchPage = () => {
    const [users, setUsers] = useState([]);
    const [favorites, setFavorites] = useState([]);
    const userId = localStorage.getItem('userId'); 

    useEffect(() => {
        // Get the user's profile to find their astrological sign
        axios.get(`http://localhost:5555/profile/${userId}`)
            .then(response => {
                // Get the users by sign ID
                const signId = response.data.astrological_sign_id;
                return axios.get(`http://localhost:5555/users_by_sign/${signId}`);
            })
            .then(response => {
                setUsers(response.data); 
            })
            .catch(error => {
                console.error('Error fetching matches:', error);
            });
    }, [userId]);

    const handleAddToFavorites = (user) => {
        // Add a user to the favorites list
        setFavorites(prevFavorites => [...prevFavorites, user]);
    };

    const handleRemoveFromFavorites = (user) => {
        // Remove a user from the favorites list
        setFavorites(prevFavorites => prevFavorites.filter(fav => fav.id !== user.id));
    };

    return (
        <div>
            <h2>Find Your Astrological Match</h2>
            {users.map((user) => (
                <Card 
                    key={user.id} 
                    user={user} 
                    onAddToFavorites={() => handleAddToFavorites(user)} 
                />
            ))}
            <div>
                <FavoritesBar 
                    favorites={favorites} 
                    removeFromFavorites={handleRemoveFromFavorites} 
                />
            </div>
        </div>
    );
};

export default MatchPage;
