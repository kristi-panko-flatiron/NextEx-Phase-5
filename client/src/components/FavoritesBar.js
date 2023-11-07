import React from 'react';
import '../index.css';
import { useHistory } from 'react-router-dom';

// Define the placeholder image URL at the top of your file
const placeholderImage = 'https://www.rd.com/wp-content/uploads/2021/04/GettyImages-514622028-e1617288074638.jpg';

const FavoritesBar = ({ favorites, removeFromFavorites }) => {
    const history = useHistory();

    // Function to handle navigation
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
                        onClick={() => navigateToUserDetail(favorite.id)}
                    >
                        {/* Use the placeholder image if favorite.image_url is not available */}
                        <img src={favorite.image_url || placeholderImage} alt={favorite.name} className="favorite-image" />
                        <p>{favorite.name}</p>
                        <p>{favorite.astrologicalSign}</p>
                        <button onClick={(e) => {
                            e.stopPropagation();
                            removeFromFavorites(favorite);
                        }}>💔</button>
                    </div>
                ))}
            </div>
        </aside>
    );
};

export default FavoritesBar;
