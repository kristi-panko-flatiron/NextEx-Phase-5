import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Card from './Card';
import FavoritesBar from './FavoritesBar';
import '../index.css'

// const bestMatchesData = [
//     {'astrological_sign_id': 1, 'best_match_name': 'Leo'},
//     {'astrological_sign_id': 1, 'best_match_name': 'Sagittarius'},
//     {'astrological_sign_id': 2, 'best_match_name': 'Virgo'},
//     {'astrological_sign_id': 2, 'best_match_name': 'Capricorn'},
//     {'astrological_sign_id': 3, 'best_match_name': 'Libra'},
//     {'astrological_sign_id': 3, 'best_match_name': 'Aquarius'},
//     {'astrological_sign_id': 4, 'best_match_name': 'Scorpio'},
//     {'astrological_sign_id': 4, 'best_match_name': 'Pisces'},
//     {'astrological_sign_id': 5, 'best_match_name': 'Aries'},
//     {'astrological_sign_id': 5, 'best_match_name': 'Sagittarius'},
//     {'astrological_sign_id': 6, 'best_match_name': 'Taurus'},
//     {'astrological_sign_id': 6, 'best_match_name': 'Capricorn'},
//     {'astrological_sign_id': 7, 'best_match_name': 'Gemini'},
//     {'astrological_sign_id': 7, 'best_match_name': 'Aquarius'},
//     {'astrological_sign_id': 8, 'best_match_name': 'Cancer'},
//     {'astrological_sign_id': 8, 'best_match_name': 'Pisces'},
//     {'astrological_sign_id': 9, 'best_match_name': 'Aries'},
//     {'astrological_sign_id': 9, 'best_match_name': 'Leo'},
//     {'astrological_sign_id': 10, 'best_match_name': 'Scorpio'},
//     {'astrological_sign_id': 10, 'best_match_name': 'Pisces'},
//     {'astrological_sign_id': 11, 'best_match_name': 'Gemini'},
//     {'astrological_sign_id': 11, 'best_match_name': 'Libra'},
//     {'astrological_sign_id': 12, 'best_match_name': 'Cancer'},
//     {'astrological_sign_id': 12, 'best_match_name': 'Scorpio'}
// ]

const MatchPage = () => {
    const [users, setUsers] = useState([]);
    const [favorites, setFavorites] = useState([]);
    const userId = localStorage.getItem('userId'); 
    // const [matches, setMatches] = useState([]);

    useEffect(() => {
    const fetchMatches = async () => {
        try {
            const userId = localStorage.getItem('userId');
            if (userId) {
              // Fetch the logged-in user's astrological sign
            const profileResponse = await axios.get(`http://localhost:5555/profile/${userId}`);
            const userSignId = profileResponse.data.astrological_sign.id;
            
              // Fetch the best matches for the user's sign
            const matchesResponse = await axios.get(`http://localhost:5555/bestmatches/${userSignId}`);
            const bestMatchesSignIds = matchesResponse.data.map(match => match.astrological_sign_id);
            
              // Fetch all users
            const usersResponse = await axios.get('http://localhost:5555/users');
            
              // Filter users by the best matching signs
            const filteredUsers = usersResponse.data.filter(user => 
                bestMatchesSignIds.includes(user.astrological_sign_id)
            );
            
            setUsers(filteredUsers);
            }
        } catch (error) {
            console.error('Error fetching matches:', error);
        }
        };
        
        fetchMatches();
    }, []);

    // useEffect(() => {
    // const fetchMatches = async () => {
    //     try {
    //         const userId = localStorage.getItem('userId');
    //         if (userId) {
    //           // Fetch the logged-in user's astrological sign
    //         const profileResponse = await axios.get(`http://localhost:5555/profile/${userId}`);
    //         const userSignId = profileResponse.data.astrological_sign.id;
            
    //           // Fetch the best matches for the user's sign
    //         const matchesResponse = await axios.get(`http://localhost:5555/best_matches/${userSignId}`);
    //         const bestMatches = matchesResponse.data;
            
    //           // Get the IDs of the best matched signs
    //         const bestMatchesSignIds = bestMatches.map(match => match.astrological_sign_id);
            
    //           // Fetch all users
    //         const usersResponse = await axios.get('http://localhost:5555/users');
    //         let allUsers = usersResponse.data;
            
    //           // Filter users by the best matching signs
    //         const filteredUsers = allUsers.filter(user =>
    //             bestMatchesSignIds.includes(user.astrological_sign_id)
    //         );
            
    //           // Update state with filtered users
    //         setUsers(filteredUsers);
    //         }
    //     } catch (error) {
    //         console.error('Error fetching matches:', error);
    //     }
    //     };

    //     // Call fetchMatches when the component mounts
    //     fetchMatches();
    //   }, []); // Empty dependency array means this effect runs once on mount


    const handleAddToFavorites = async (user) => { 
        try {
            const response = await axios.post('http://localhost:5555/favorites', {
                user_id: userId,
                best_match_id: user.id
            });
            setFavorites((prevFavorites) => [...prevFavorites, response.data]);
        } catch (error) {
            console.error('Error adding to favorites:', error);
        }
    };

    const handleRemoveFromFavorites = (user) => {
        // Remove a user from the favorites list
        setFavorites(prevFavorites => prevFavorites.filter(fav => fav.id !== user.id));
    };

    return (
        <div className="match-page">
            <FavoritesBar 
                favorites={favorites} 
                removeFromFavorites={handleRemoveFromFavorites}
                userId={userId} 
            />
            <div className="cards-container">
                <h2 className="match-heading">Find Your Astrological Match</h2>
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
