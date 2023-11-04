import React, { useState, useEffect } from 'react';
import axios from 'axios';

const FavoritesBar = ({userId}) => {
    const [favorites, setFavorites] = useState([]);
    useEffect(() => {
        axios.get('http://localhost:5555/favorites')
        .then((response) => {
            setFavorites(response.data);
        })
        .catch((error) => {
        });
    }, []);


    const removeFromFavorites = async (user) => {
        try {
            await axios.delete('http://localhost:5555/favorites', { data: { user_id: userId, best_match_id: user.id } });
            const updatedFavorites = favorites.filter((fav) => fav.id !== user.id);
            setFavorites(updatedFavorites);
        } catch (error) {
            console.error('Error removing from favorites:', error);
        }
    };
    

    return (
        <div>
            <h3>Favorites</h3>
            {favorites.map((favorite) => (
                <div key={favorite.id}>
                    {/* Display favorite user information */}
                    <p>{favorite.name}</p>
                    <p>{favorite.astrologicalSign}</p>
                    {/* Add a button to remove from favorites */}
                    <button onClick={() => removeFromFavorites(favorite)}>Remove</button>
                </div>
            ))}
        </div>
    );
};

export default FavoritesBar;
