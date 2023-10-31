// BestMatches.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const BestMatches = () => {
    const [bestMatches, setBestMatches] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5555/best_matches')
            .then(response => {
                setBestMatches(response.data);
            })
            .catch(error => {
                console.error('Error fetching best matches:', error);
            });
    }, []);

    return (
        <div>
            <h2>Best Matches</h2>
            {Object.keys(bestMatches).map(sign => (
                <div key={sign}>
                    <h3>{sign}</h3>
                    <ul>
                        {bestMatches[sign].map(match => (
                            <li key={match.id}>{match.name}</li>
                        ))}
                    </ul>
                </div>
            ))}
        </div>
    );
};

export default BestMatches;
