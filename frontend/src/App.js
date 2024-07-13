import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import SignIn from './components/login';
import HomePage from './components/homepage';
import SignUp from './components/register';
import ForgotPassword from './components/forgot_password';
import RfpDisplay from './components/rfp_display';
import ShowUploadedFileList from './components/show_uploaded_file_list';

function App() {
  return (
    <Router>
        <Routes>
          <Route path="/" element={<HomePage/>} />
          <Route path="/signin" element={<SignIn/>} />
          <Route path="/signup" element={<SignUp/>} />
          <Route path="/forgot_password" element={<ForgotPassword/>} />
          <Route path="/rfp-analysis" element={<RfpDisplay/>} />
          <Route path='/uploaded-files' element={<ShowUploadedFileList/>} />
        </Routes>
    </Router>
  );
}

export default App;
