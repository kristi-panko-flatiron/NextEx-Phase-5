import React, { useState } from 'react';

const FavoritesBar = () => {
    const [favorites, setFavorites] = useState([]);

    // Function to remove a user from favorites
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
