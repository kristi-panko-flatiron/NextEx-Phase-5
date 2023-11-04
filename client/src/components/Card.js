// Card.js

import React from 'react';

const Card = ({ user, onAddToFavorites }) => {
    return (
        <div className="user-card">
            <h2>{user.name}</h2>
            <img src={user.image} alt={user.name} />
            <p>Astrological Sign: {user.astrological_sign ? user.astrological_sign.sign_name : 'Loading...'}</p>
            {/* Add more user information fields here */}
            <button onClick={() => onAddToFavorites(user)}>Add to Favorites</button>
        </div>
    );
};

export default Card;
