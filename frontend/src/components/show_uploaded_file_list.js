import React, { useEffect, useState, useCallback, useRef } from 'react';
import Header from './header';
import SideMenuComponent from './side_menu';
import TableRow from './TableRow'; // Import the TableRow component

const ShowUploadedFileList = () => {
  const [fileData, setFileData] = useState([]);
  const hasFetchedFiles = useRef(false); // Add a ref to track fetch status

  const API_URL = process.env.REACT_APP_BACKEND_URL;

  const fetchFiles = useCallback(async () => {
    try {
      console.log('Fetching files'); // Add this log to track function calls
      const response = await fetch(`${API_URL}/files`);
      if (!response.ok) {
        throw new Error('Failed to fetch files');
      }
      const data = await response.json();
      setFileData(data.files);
    } catch (error) {
      console.error('Error fetching files:', error);
      // Handle error fetching data
    }
  }, [API_URL]);

  useEffect(() => {
    if (!hasFetchedFiles.current) {
      fetchFiles();
      hasFetchedFiles.current = true; // Set ref to true after fetching
    }
  }, [fetchFiles]);

  return (
    <div className="file-container">
      <Header />
      <div className="content-container">
        <div className="side-menu-container">
          <SideMenuComponent />
        </div>
        <div className="main-content">
          <div className="content-wrapper">
            {fileData.length === 0 ? (
              <p>Loading...</p>
            ) : (
              fileData.map((file, index) => (
                <div key={index}>
                  <table>
                    <tbody>
                      <tr>
                        <th colSpan="2"><h2>{file.llm_file_name}</h2></th>
                      </tr>
                      <TableRow data={{ key: 'Name of Company', value: file.llm_prediction_vendor }} />
                      <TableRow data={{ key: 'Date of RFP', value: file.llm_prediction_Date }} />
                      <TableRow data={{ key: 'Brief Summary of the Scope', value: file.llm_prediction_scope }} />
                      <TableRow data={{ key: 'List of Skill Tags Included', value: file.llm_prediction_skill }} />
                      <TableRow data={{ key: 'List of Job Titles Required', value: file.llm_prediction_designations }} />
                      <TableRow data={{ key: 'Outcome', value: file.llm_prediction_Outcome }} />
                      <TableRow data={{ key: 'Deliverables', value: file.llm_prediction_Deliverables }} />
                    </tbody>
                  </table>
                </div>
              ))
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default ShowUploadedFileList;
