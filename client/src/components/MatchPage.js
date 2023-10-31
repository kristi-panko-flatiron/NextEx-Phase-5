import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Card from './Card';
import FavoritesBar from './FavoritesBar';

const MatchPage = () => {
    const [users, setUsers] = useState([]);
    const [favorites, setFavorites] = useState([]);

    // Fetch users based on astrological sign
    useEffect(() => {
        axios.get('http://localhost:5555/users_by_sign/<sign_id>')  // Replace <sign_id> with the appropriate sign ID
            .then(response => {
                setUsers(response.data);
            })
            .catch(error => {
                console.error('Error fetching users:', error);
            });
    }, []);

    const handleAddToFavorites = (user) => {
        setFavorites([...favorites, user]);
    };

    const handleRemoveFromFavorites = (user) => {
        const updatedFavorites = favorites.filter((fav) => fav.id !== user.id);
        setFavorites(updatedFavorites);
    };

    return (
        <div>
            <h2>Find Your Astrological Match</h2>
            {users.map((user) => (
                <Card key={user.id} user={user} onAddToFavorites={handleAddToFavorites} />
            ))}
            {/* Match Now Button */}
            <div>
                <FavoritesBar favorites={favorites} removeFromFavorites={handleRemoveFromFavorites} />
            </div>
        </div>
    );
};

export default MatchPage;
