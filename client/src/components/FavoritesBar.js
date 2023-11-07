import React from 'react';
import '../index.css';
import { useHistory } from 'react-router-dom';

const FavoritesBar = ({ favorites, removeFromFavorites }) => {
    const history = useHistory();
    const navigateToUserDetail = (userId) => {
        history.push(`/users/${userId}`);
    };

    return (
        <aside className="favorites-bar">
            <h3 className="gradient-text">Favorites</h3>
            <div className="favorite-list">
                {favorites.map((favorite) => (
                    <div
                        key={favorite.id}
                        className="favorite-item"
                        onClick={() => navigateToUserDetail(favorite.id)} // Add the onClick handler here
                    >
                        <img src={favorite.image_url || 'path/to/your/default-placeholder.jpg'} alt={favorite.name} className="favorite-image" />
                        <p>{favorite.name}</p>
                        <p>{favorite.astrologicalSign}</p>
                        <button onClick={(e) => {
                            e.stopPropagation(); // Prevent the click from triggering the navigation
                            removeFromFavorites(favorite);
                        }}>💔</button>
                    </div>
                ))}
            </div>
        </aside>
    );
};

export default FavoritesBar;
