import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Card from './Card';
import FavoritesBar from './FavoritesBar';
import '../index.css';


const MatchPage = () => {
    const [users, setUsers] = useState([]);
    const [favorites, setFavorites] = useState([]);
    const [matches, setMatches] = useState([]);
    const userId = localStorage.getItem('userId');

    useEffect(() => {
        const fetchMatchesAndFavorites = async () => {
            if (userId) {
                try {
                    const matchesResponse = await axios.get(`http://localhost:5555/users_by_best_match/${userId}`);
                    setUsers(matchesResponse.data || []);
                } catch (error) {
                    console.error('Error fetching matches:', error);
                }
                try {
                    const favoritesResponse = await axios.get(`http://localhost:5555/favorites/${userId}`);
                    setFavorites(favoritesResponse.data || []);
                } catch (error) {
                    console.error('Error fetching favorites:', error);
                }
            }
        };

        fetchMatchesAndFavorites();
    }, [userId]);

    const fetchFavorites = async () => {
        if (userId) {
            try {
                const response = await axios.get(`http://localhost:5555/favorites/${userId}`);
                setFavorites(response.data || []);
            } catch (error) {
                console.error('Error fetching favorites:', error);
            }
            }
        };

    const handleAddToFavorites = async (userToAdd) => {
        try {
            const response = await axios.post('http://localhost:5555/favorites', {
                user_id: userId,
                fav_user_id: userToAdd.id
            });
    
            if (response.status === 201) {
                setFavorites((prevFavorites) => {
                    if (!prevFavorites.some((fav) => fav.id === userToAdd.id)) {
                        return [...prevFavorites, userToAdd];
                    } else {
                        alert('User is already in favorites.');
                        return prevFavorites; // No change to the favorites list
                    }
                });
                if (response.data.is_match) {
                    alert("It's a match!");
                }
            }
        } catch (error) {
            console.error('Error adding to favorites:', error);
            if (error.response && error.response.status === 409) {
                alert('User is already in favorites.');
            }
        }
    };

    const handleRemoveFromFavorites = async (userToRemove) => {
        try {
            const response = await axios.delete(`http://localhost:5555/favorites/${userId}/${userToRemove.id}`);

            if (response.status === 200) {
                // Update the state with the new list of favorites
                setFavorites(prevFavorites => prevFavorites.filter(user => user.id !== userToRemove.id));
            }
        } catch (error) {
            console.error('Error removing from favorites:', error);
        }
    };

    const addMatch = (matchedUser) => {
        setMatches(prevMatches => [...prevMatches, matchedUser]);
    };

    return (
        <div className="match-page">
            <FavoritesBar 
                favorites={favorites}
                removeFromFavorites={handleRemoveFromFavorites}
                fetchFavorites={fetchFavorites}
                userId={userId}
            />
            <div className="cards-container">
                <h2 className="gradient-text match-heading">Find Your Astrological Match</h2>
                <div className="card-grid">
                    {users.map((user) => (
                        <Card
                            key={user.id}
                            user={user}
                            onAddToFavorites={() => handleAddToFavorites(user)}
                        />
                    ))}
                </div>
            </div>
        </div>
    );
};

export default MatchPage;