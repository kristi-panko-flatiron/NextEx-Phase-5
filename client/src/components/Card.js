import React from 'react';
import '../index.css';
import { useHistory } from 'react-router-dom';

const Card = ({ user, onAddToFavorites }) => {
    const history = useHistory();
    const placeholderImage = 'https://www.rd.com/wp-content/uploads/2021/04/GettyImages-514622028-e1617288074638.jpg'; 

    // Function to handle the navigation
    const navigateToUserDetail = () => {
        history.push(`/users/${user.id}`);
    };

    // Determine which image to use
    const imageUrl = user.image_url || placeholderImage;

    return (
        <div className="card" onClick={navigateToUserDetail}>
            <div className="card-content">
                <h2>{user.name}</h2>
                {/* Use the imageUrl which could be the user's image or the placeholder */}
                <img src={imageUrl} alt={user.name} />
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
