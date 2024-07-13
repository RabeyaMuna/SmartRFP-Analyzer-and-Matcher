import React from 'react';
import Header from './header';
import SideMenuComponent from './side_menu';
import '../styles/homepage.css'; // Import CSS file for styling

export default function HomePage() {
    return (
        <div className="homepage-container">
            <Header />
            <div className="content-container">
                <div className="side-menu-container">
                    <SideMenuComponent />
                </div>
                <div className="main-content">
                    <div className="content-wrapper">
                        <p>This is the main content area. It will be scrollable if content exceeds the available space.</p>
                        {/* Add more content here */}
                    </div>
                </div>
            </div>
        </div>
    );
}
