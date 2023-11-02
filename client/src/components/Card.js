// Card.js

import React from 'react';

const Card = ({ user }) => {
    return (
        <div className="user-card">
            <h2>{user.name}</h2>
            <img src={user.image} alt={user.name} />
            <p>Astrological Sign: {user.astrological_sign}</p>
            {/* Add more user information fields here */}
        </div>
    );
};

export default Card;
