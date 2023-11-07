// import React, { useState, useEffect } from 'react';
// import axios from 'axios';
// import Card from './Card';
// import FavoritesBar from './FavoritesBar';
// import '../index.css';

// const MatchPage = () => {
//     const [users, setUsers] = useState([]);
//     const [favorites, setFavorites] = useState([]);
//     const userId = localStorage.getItem('userId');

//     useEffect(() => {
//         const fetchMatches = async () => {
//             try {
//                 if (userId) {
//                     const response = await axios.get(`http://localhost:5555/users_by_best_match/${userId}`);
//                     if (response.status === 200) {
//                         setUsers(response.data);
//                     }
//                 }
//             } catch (error) {
//                 console.error('Error fetching matches:', error);
//             }
//         };

//         const fetchFavorites = async () => {
//             try {
//                 if (userId) {
//                     const response = await axios.get(`http://localhost:5555/favorites/${userId}`);
//                     if (response.status === 200) {
//                         setFavorites(response.data);
//                     }
//                 }
//             } catch (error) {
//                 console.error('Error fetching favorites:', error);
//             }
//         };

//         fetchMatches();
//         fetchFavorites();
//     }, [userId]);


//     // const handleAddToFavorites = async (user) => {
//     //     try {
//     //         const response = await axios.post('http://localhost:5555/favorites', {
//     //             user_id: userId,
//     //             fav_user_id: user.id
//     //         });
//     //         if (response.status === 201) {
//     //             setFavorites(prevFavorites => [...prevFavorites, response.data]);
//     //         }
//     //         } catch (error) {
//     //         if (error.response && error.response.status === 409) {
//     //             console.error('User is already in favorites.');
//     //         } else {
//     //             console.error('Error adding to favorites:', error);
//     //         }
//     //         }
//     //     };

//     // const handleAddToFavorites = async (user) => {
//     //     try {
//     //         const response = await axios.post('http://localhost:5555/favorites', {
//     //             user_id: userId,
//     //             fav_user_id: user.id
//     //         });
//     //         if (response.status === 201) {
//     //             setFavorites(prevFavorites => [...prevFavorites, user]);
//     //             // Check the response for a match and alert the user if there is one
//     //             if (response.data.is_match) {
//     //                 alert("It's a match!");
//     //             }
//     //         }
//     //     } catch (error) {
//     //         console.error('Error adding to favorites:', error);
//     //     }
//     // };

//     const handleAddToFavorites = async (userToAdd) => {
//         try {
//             const response = await axios.post('http://localhost:5555/favorites', {
//                 user_id: userId,
//                 fav_user_id: userToAdd.id
//             });
//             if (response.status === 201) {
//                 setFavorites(prevFavorites => {
//                     if (!prevFavorites.some(user => user.id === userToAdd.id)) {
//                         return [...prevFavorites, userToAdd];
//                     }
//                     return prevFavorites;
//                 });
//                 if (response.data.is_match) {
//                     alert("It's a match!");
//                 }
//             }
//         } catch (error) {
//             console.error('Error adding to favorites:', error);
//             setFavorites(prevFavorites => prevFavorites.filter(user => user.id !== userToAdd.id));
//         }
//     };
    

//     const handleRemoveFromFavorites = async (user) => {
//         try {
//             const response = await axios.delete(`http://localhost:5555/favorites/${userId}/${user.id}`); // Update the URL to include both user_id and fav_user_id
//             if (response.status === 200) {
//                 setFavorites(prevFavorites => prevFavorites.filter(fav => fav.id !== user.id));
//             }
//         } catch (error) {
//             console.error('Error removing from favorites:', error);
//         }
//     };




//     return (
//         <div className="match-page">
//             <FavoritesBar 
//                 favorites={favorites}
//                 removeFromFavorites={handleRemoveFromFavorites}
//                 userId={userId}
//             />
//             <div className="cards-container">
//                 <h2 className="match-heading">Find Your Astrological Match</h2>
//                 <div className="card-grid">
//                     {users.map((user) => (
//                         <Card
//                             key={user.id}
//                             user={user}
//                             onAddToFavorites={() => handleAddToFavorites(user)}
//                         />
//                     ))}
//                 </div>
//             </div>
//         </div>
//     );
// };

// export default MatchPage;

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Card from './Card';
import FavoritesBar from './FavoritesBar';
import '../index.css';

const MatchPage = () => {
    const [users, setUsers] = useState([]);
    const [favorites, setFavorites] = useState([]);
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

    const handleAddToFavorites = async (userToAdd) => {
        try {
            const response = await axios.post('http://localhost:5555/favorites', {
                user_id: userId,
                fav_user_id: userToAdd.id
            });

            if (response.status === 201) {
                // Update the state with the new list of favorites
                setFavorites(prevFavorites => {
                    // If the userToAdd is not already in favorites, add it
                    const updatedFavorites = prevFavorites.find(fav => fav.id === userToAdd.id)
                        ? prevFavorites
                        : [...prevFavorites, userToAdd];
                    console.log('Updated favorites:', updatedFavorites);
                    return updatedFavorites;
                });
                console.log('Current favorites after update:', favorites);
                // alert user for match
                if (response.data.is_match) {
                    alert("It's a match!");
                }
            }
        } catch (error) {
            console.error('Error adding to favorites:', error);
            if (error.response && error.response.status === 409) {
                console.error('User is already in favorites.');
            } else {
                console.error('Error adding to favorites:', error);
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
