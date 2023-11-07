import React, { useState, useEffect } from 'react';
import Card from './Card';
import axios from 'axios';
import '../index.css';

const MatchesPage = ({ userId, handleAddToFavorites }) => {
    const [matches, setMatches] = useState([]);

    useEffect(() => {
        const userId = localStorage.getItem('userId'); // Assuming the user ID is stored in localStorage
        if (userId) {
            axios.get(`http://localhost:5555/matches/${userId}`)
                .then(response => {
                    setMatches(response.data);
                })
                .catch(error => {
                    console.error('Error fetching matches:', error);
                });
        }
    }, []);
    
    
    // Render your matches...


    return (
        <div className="matches-page">
            <h1 className = "matches-title gradient-text">Your Matches</h1>
            {/* Render matched user cards */}
            {matches.map((match) => (
                <Card
                    key={match.id}
                    user={match}
                    onAddToFavorites={() => handleAddToFavorites(match)}
                />
            ))}
        </div>
    );
};

export default MatchesPage;