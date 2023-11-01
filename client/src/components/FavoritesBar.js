import React, { useState, useEffect } from 'react';
import axios from 'axios';

const FavoritesBar = () => {
    const [favorites, setFavorites] = useState([]);
    useEffect(() => {
        axios.get('http://localhost:5555/favorites')
        .then((response) => {
            setFavorites(response.data);
        })
        .catch((error) => {
        });
    }, []);
    // remove
    const removeFromFavorites = (user) => {
        const updatedFavorites = favorites.filter((fav) => fav.id !== user.id);
        setFavorites(updatedFavorites);
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
