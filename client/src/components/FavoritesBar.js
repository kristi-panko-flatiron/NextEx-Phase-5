import React from 'react';
import '../index.css';
import { useHistory } from 'react-router-dom';


const FavoritesBar = ({ favorites, removeFromFavorites }) => {
    const placeholderImage = 'https://www.rd.com/wp-content/uploads/2021/04/GettyImages-514622028-e1617288074638.jpg';  

    return (
        <aside className="favorites-bar">
            <h3 className="gradient-text">Favorites</h3>
            <div className="favorite-list">
                {favorites.map((favorite) => (
                    <div key={favorite.id} className="favorite-item">
                        {/* Use either the favorite's image or the placeholder image */}
                        <img src={favorite.image_url || placeholderImage} alt={favorite.name} className="favorite-image" />
                        <p>{favorite.name}</p>
                        <p>{favorite.astrologicalSign}</p>
                        <button onClick={() => removeFromFavorites(favorite)}>💔</button>
                    </div>
                ))}
            </div>
        </aside>
    );
};

export default FavoritesBar;
