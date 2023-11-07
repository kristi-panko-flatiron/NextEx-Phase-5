import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../index.css'


const FavoritesBar = ({ favorites, removeFromFavorites }) => {
    return (
        <aside className="favorites-bar">
            <h3 className="gradient-text">Favorites</h3>
            <div className="favorite-list">
                {favorites.map((favorite) => (
                    <div key={favorite.id} className="favorite-item">
                        <img src={favorite.image_url} alt={favorite.name} className="favorite-image" />
                        <p>{favorite.name}</p>
                        <p>{favorite.astrologicalSign}</p>
                        <button onClick={() => removeFromFavorites(favorite)}>💔</button>
                    </div>
                ))}
            </div>
        </aside>
    );
};

export default FavoritesBar;// HomePage.js