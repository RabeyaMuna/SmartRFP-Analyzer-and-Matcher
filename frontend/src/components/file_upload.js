import React, { useState } from 'react';
import axios from 'axios';
import uploadIcon from '../images/upload-icon.png';
import '../styles/Modal.css';

const API_URL = process.env.REACT_APP_BACKEND_URL;

const FileUpload = ({ onFileUploaded }) => {
  const [file, setFile] = useState(null);
  const [fileName, setFileName] = useState('');
  const [uploadStatus, setUploadStatus] = useState('');
  const [error, setError] = useState(null);

  const handleFileUpload = async () => {
    if (!file) {
      setError('File is not found');
      setUploadStatus('Failed to upload file.');
      return;
    }

    setUploadStatus('Uploading file...');

    try {
      const formData = new FormData();
      formData.append('file', file);

      const response = await axios.post(`${API_URL}/uploadfile_single`, formData, {
        withCredentials: true,
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      if (response.status === 200) {
        setUploadStatus('File uploaded successfully!');
        onFileUploaded(response.data);
      } else {
        setUploadStatus('Failed to upload file.');
      }
    } catch (error) {
      console.error('Error uploading file:', error);
      if (error.response) {
        if (error.response.status === 409) {
          setUploadStatus('Failed to upload file: Blob with the same name already exists...');
        } else {
          setUploadStatus('Failed to upload file: Something went terribly wrong...');
        }
      } else {
        setUploadStatus('Failed to upload file: Network Error');
      }
    }
  };

  const handleFileInputChange = async (event) => {
    event.preventDefault();
    setFileName('');
    await handleFileUpload();
  };

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);
    if (selectedFile) {
      setFileName(selectedFile.name);
    } else {
      setFileName('');
    }
  };

  return (
    <div className="upload-button-container">
      <form onSubmit={handleFileInputChange}>
        <input 
          type="file" 
          id="file-upload" 
          style={{ display: 'none' }} 
          onChange={handleFileChange} 
        />
        <label htmlFor="file-upload" className="upload-button" tabIndex="0">
          <img src={uploadIcon} alt="Upload" className="upload-icon" />
        </label>
        <br />
        <div className="file-name-container">
          {fileName && <p className="file-name">{fileName}</p>}
        </div>
        <button type="submit">UPLOAD FILE</button>
      </form>
      {uploadStatus && <p className="upload-status">{uploadStatus}</p>}
    </div>
  );
};

export default FileUpload;
