import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Card from './Card';
import FavoritesBar from './FavoritesBar';
import '../index.css'

const MatchPage = () => {
    const [users, setUsers] = useState([]);
    const [favorites, setFavorites] = useState([]);
    const userId = localStorage.getItem('userId'); 
    // const [matches, setMatches] = useState([]);

    // useEffect(() => {
    // const fetchMatches = async () => {
    //     try {
    //         const userId = localStorage.getItem('userId');
    //         if (userId) {
    //           // Fetch the logged-in user's astrological sign
    //         const profileResponse = await axios.get(`http://localhost:5555/profile/${userId}`);
    //         const userSignId = profileResponse.data.astrological_sign.id;
            
    //           // Fetch the best matches for the user's sign
    //         const matchesResponse = await axios.get(`http://localhost:5555/bestmatches/${userSignId}`);
    //         const bestMatchesSignIds = matchesResponse.data.map(match => match.astrological_sign_id);
            
    //           // Fetch all users
    //         const usersResponse = await axios.get('http://localhost:5555/users');
            
    //           // Filter users by the best matching signs
    //         const filteredUsers = usersResponse.data.filter(user => 
    //             bestMatchesSignIds.includes(user.astrological_sign_id)
    //         );
            
    //         setUsers(filteredUsers);
    //         }
    //     } catch (error) {
    //         console.error('Error fetching matches:', error);
    //     }
    //     };
        
    //     fetchMatches();
    // }, []);

    // useEffect(() => {
    //     const fetchMatches = async () => {
    //         try {
    //             const userId = localStorage.getItem('userId');
    //             if (userId) {
    //                 // Fetch the logged-in user's astrological sign
    //                 const profileResponse = await axios.get(`http://localhost:5555/profile/${userId}`);
    //                 const userSignId = profileResponse.data.astrological_sign.id;
                    
    //                 // Fetch the best matches for the user's sign
    //                 const matchesResponse = await axios.get(`http://localhost:5555/bestmatches/${userSignId}`);
    //                 const bestMatchesSignIds = matchesResponse.data.map(match => match.astrological_sign_id);
                    
    //                 // Fetch all users with a sign that's in the best matches
    //                 const usersResponse = await axios.get('http://localhost:5555/users');
    //                 const filteredUsers = usersResponse.data.filter(user => 
    //                     bestMatchesSignIds.includes(user.astrological_sign_id)
    //                 );
                    
    //                 setUsers(filteredUsers);
    //             }
    //         } catch (error) {
    //             console.error('Error fetching matches:', error);
    //         }
    //     };
        
    //     fetchMatches();
    // }, []);
    // useEffect(() => {
    //     const fetchMatches = async () => {
    //         try {
    //             const userId = localStorage.getItem('userId');
    //             if (userId) {
    //                 // Fetch the best matches for the user's sign
    //                 const response = await axios.get(`http://localhost:5555/users_by_best_match/${userId}`);
    //                 setUsers(response.data); // Assumes the API returns an array of user objects
    //             }
    //         } catch (error) {
    //             console.error('Error fetching matches:', error);
    //         }
    //     };
        
    //     fetchMatches();
    // }, []);
    
    // useEffect(() => {
    //     const fetchMatches = async () => {
    //         try {
    //             const userId = localStorage.getItem('userId');
    //             if (userId) {
    //                 const profileResponse = await axios.get(`http://localhost:5555/profile/${userId}`);
    //                 if (profileResponse.status === 200 && profileResponse.data.astrological_sign) {
    //                     const userSignId = profileResponse.data.astrological_sign.id;
    //                     const bestMatchesResponse = await axios.get(`http://localhost:5555/bestmatches/${userSignId}`);
    //                     if (bestMatchesResponse.status === 200) {
    //                         const bestMatchSignIds = bestMatchesResponse.data.map(match => match.astrological_sign_id);
    //                         console.log(bestMatchSignIds)
    //                         const usersResponse = await axios.get('http://localhost:5555/users');
    //                         if (usersResponse.status === 200) {
    //                             const filteredUsers = usersResponse.data.filter(user =>
    //                                 bestMatchSignIds.includes(user.astrological_sign_id)
    //                             );
    //                             console.log(filteredUsers) 
    //                             setUsers(filteredUsers);
    //                         }
    //                     }
    //                 }
    //             }
    //         } catch (error) {
    //             console.error('Error fetching matches:', error);
    //         }
    //     };
    
    //     fetchMatches();
    // }, []);
    useEffect(() => {
        const fetchMatches = async () => {
            try {
                const userId = localStorage.getItem('userId');
                if (userId) {
                    const response = await axios.get(`http://localhost:5555/users_by_best_match/${userId}`);
                    if (response.status === 200) {
                        setUsers(response.data); 
                    }
                }
            } catch (error) {
                console.error('Error fetching matches:', error);
            }
        };
    
        fetchMatches();
    }, []);
    
    



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
