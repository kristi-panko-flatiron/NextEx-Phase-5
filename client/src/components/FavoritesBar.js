import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../index.css'

const FavoritesBar = ({ userId, fetchFavorites }) => {
    const [favorites, setFavorites] = useState([]);

    useEffect(() => {
        if (userId) {
            axios.get(`http://localhost:5555/favorites/${userId}`)
            .then((response) => {
                setFavorites(response.data);
            })
            .catch((error) => {
                console.error('Error fetching favorites:', error);
            });
        }
    }, [userId]);

    const removeFromFavorites = async (favUser) => {
        try {
            await axios.delete(`http://localhost:5555/favorites/${userId}/${favUser.id}`);
            const updatedFavorites = favorites.filter((favorite) => favorite.id !== favUser.id);
            setFavorites(updatedFavorites); 
        } catch (error) {
            console.error('Error removing from favorites:', error);
        }
    };


    return (
        <aside className="favorites-bar">
            <h3>Favorites</h3>
            <div className="favorite-list">
                {favorites.map((favorite) => (
                    <div key={favorite.id} className="favorite-item">
                        {/* Display favorite user information */}
                        <p>{favorite.name}</p>
                        <p>{favorite.astrologicalSign}</p>
                        {/* Add a button to remove from favorites */}
                        <button onClick={() => removeFromFavorites(favorite)}>Remove</button>
                    </div>
                ))}
            </div>
        </aside>
    );
};

export default FavoritesBar;
