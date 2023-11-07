import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import '../index.css'; 
import { Link } from 'react-router-dom';

const placeholderImage = 'https://www.rd.com/wp-content/uploads/2021/04/GettyImages-514622028-e1617288074638.jpg'; // URL for the placeholder image

const UserDetail = () => {
    const { userId } = useParams();
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios.get(`http://localhost:5555/user/${userId}`)
        .then(response => {
            setUser(response.data);
            setLoading(false);
        })
        .catch(error => {
            console.error('Error fetching user details:', error);
            setLoading(false);
        });
    }, [userId]);

    if (loading) {
        return (
            <div className="spinner-container">
                <div className="spinner"></div>
            </div>
        );
    }

    if (!user) {
        return <div>User not found.</div>;
    }

    const userImage = user.image_url || placeholderImage;

    return (
        <div className="user-detail-container">
            <img src={userImage} alt={user.name} className="user-detail-image" />
            <h1>{user.name}</h1>
            <p>Astrological Sign: {user.astrological_sign.sign_name}</p>
            <p>Sign Description: {user.astrological_sign.sign_description}</p>
            <Link to="/matches" className="back-to-matches">Back to Match Now</Link>
        </div>
    );
};

export default UserDetail;
