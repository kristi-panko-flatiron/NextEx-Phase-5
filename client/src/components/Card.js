import React from 'react';
import '../index.css';
import { useHistory } from 'react-router-dom';

const Card = ({ user, onAddToFavorites }) => {
    const history = useHistory();

    // Function to handle the navigation
    const navigateToUserDetail = () => {
        history.push(`/users/${user.id}`);
    };

    return (
        <div className="card" onClick={navigateToUserDetail}>
            <div className="card-content">
                <h2>{user.name}</h2>
                <img src={user.image_url} alt={user.name} />
                <p>Astrological Sign: {user.astrological_sign ? user.astrological_sign.sign_name : 'Loading...'}</p>
                <button onClick={(e) => {
                    e.stopPropagation(); 
                    onAddToFavorites(user);
                }}>💖</button>
            </div>
        </div>
    );
};

export default Card;
