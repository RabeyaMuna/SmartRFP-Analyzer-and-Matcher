import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { AiOutlineUser } from 'react-icons/ai';
import { ImUser } from 'react-icons/im';
import '../styles/header.css';

export default function Header({ isLoggedIn, onLogout }) {
    const navigate = useNavigate();
    const [showDropdown, setShowDropdown] = useState(false);

    const handleLoginClick = () => {
        if (!isLoggedIn) {
            navigate('/signin'); // Navigate to login page if not logged in
        } else {
            // Toggle dropdown menu visibility
            setShowDropdown(!showDropdown);
        }
    };

    const handleLogout = () => {
        if (onLogout) {
            onLogout(); // Call the logout function
        }
        setShowDropdown(false);
    };

    return (
        <div className="header">
            {isLoggedIn ? (
                <div className="profile-dropdown">
                    <AiOutlineUser className="icon" onClick={handleLoginClick} />
                    {showDropdown && (
                        <div className="dropdown-content">
                            <a href="/profile">Profile</a>
                            <button onClick={handleLogout}>Logout</button>
                        </div>
                    )}
                </div>
            ) : (
                <a className="login-button" onClick={handleLoginClick}>
                    <ImUser className="icon" />
                </a>
            )}
        </div>
    );
}
