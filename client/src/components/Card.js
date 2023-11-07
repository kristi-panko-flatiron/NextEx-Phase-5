import React from 'react';
import '../index.css';

const Card = ({ user, onAddToFavorites }) => {
    return (
        <div className="card">
            <div className="card-content">
                <h2>{user.name}</h2>
                <img src={user.image_url} alt={user.name} />
                <p>Astrological Sign: {user.astrological_sign ? user.astrological_sign.sign_name : 'Loading...'}</p>
                <button onClick={() => onAddToFavorites(user)}>💖</button>
            </div>
        </div>
    );
};

export default Card;
