import React, { useState, useEffect } from 'react';
import Card from './Card';
import axios from 'axios';
import '../index.css';

const MatchesPage = ({ userId, handleAddToFavorites }) => {
    const [matches, setMatches] = useState([]);

    useEffect(() => {
        const fetchMatches = async () => {
            try {
                const response = await axios.get(`http://localhost:5555/matches/${userId}`);
                setMatches(response.data);
            } catch (error) {
                console.error('Error fetching matches:', error);
            }
        };

        fetchMatches();
    }, [userId]);

    // Render your matches...


    return (
        <div className="matches-page">
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
