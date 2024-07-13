// Modal.js (Example)

import React from 'react';
import '../styles/Modal.css'; // Example CSS for modal styles

const Modal = ({ children }) => {
  return (
    <div className="modal">
      <div className="modal-content">
        {children}
      </div>
    </div>
  );
};

export default Modal;
