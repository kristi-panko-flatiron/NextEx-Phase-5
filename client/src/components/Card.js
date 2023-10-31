// Card.js
import React from 'react';

const Card = ({ user, onAddToFavorites }) => {
    return (
        <div>
            <h2>{user.name}</h2>
            <img src={user.image} alt={user.name} />
            <p>Astrological Sign: {user.astrologicalSign}</p>
            <button onClick={() => onAddToFavorites(user)}>Add to Favorites</button>
        </div>
    );
};

export default Card;
