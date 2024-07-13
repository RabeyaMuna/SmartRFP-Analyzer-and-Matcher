// auth.js
import axios from "axios";

const API_URL = process.env.REACT_APP_BACKEND_URL; // Replace with your API URL
console.log(API_URL)
export async function authenticate(email, password, setIsLoggedIn) {
  try {
    const response = await axios.post(
      `${API_URL}/signin`,
      {
        email: email,
        password: password
      }
    );

    if (response.status === 200) {
      // Authentication successful
      localStorage.setItem('EMAIL', response.data.EMAIL);
      localStorage.setItem('USER_ID', response.data.USER_ID);
      localStorage.setItem('USER_NAME', response.data.USER_NAME);
      return true;
    } else {
      // Authentication failed
      return false;
    }
  } catch (error) {
    console.error("Authentication error:", error);
    return false;
  }
}
