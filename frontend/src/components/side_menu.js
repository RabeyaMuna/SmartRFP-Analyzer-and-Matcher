import React from 'react';
import { List, ListItem, ListItemIcon, ListItemText } from '@mui/material';
import { NavLink } from 'react-router-dom';
import homeIcon from '../images/home-icon.png';
import rfpIcon from '../images/rfp-icon.png';
import '../styles/sidebar.css';
import FileUpload from './file_upload';
import fileIcon from '../images/file-icon.gif';

const sidemenu = [
  { name: 'Home', path: '/', icon: homeIcon },
  { name: 'RFP Analysis', path: '/rfp-analysis', icon: rfpIcon },
  { name: 'Uploaded Files', path: '/uploaded-files', icon: fileIcon },
];

const logoUrl = 'https://dexian.com/wp-content/themes/dexian/images/dexian-logo.svg';
const description = 'IT solution for RFP Analysis';

function SideMenuComponent() {
  const handleFileUploaded = (data) => {
    console.log('File uploaded:', data);
    // Handle any other actions you want to perform after file upload
  };

  return (
    <div className="sidebar-container">
      <div className="side-menu">
        <div className="logo-container">
          <img src={logoUrl} alt="Dexian" className="logo" />
          <p className="description">{description}</p>
        </div>
        <List component="nav" aria-labelledby="nested-list-subheader">
          {sidemenu.map((menu, index) => (
            <NavLink exact className="menu-item" activeClassName="active-menu" to={menu.path} key={index}>
              <ListItem button>
                <ListItemIcon>
                  <img src={menu.icon} alt={menu.name} />
                </ListItemIcon>
                <ListItemText primary={menu.name} />
              </ListItem>
            </NavLink>
          ))}
        </List>
      </div>
      <FileUpload onFileUploaded={handleFileUploaded} />
    </div>
  );
}

export default SideMenuComponent;
