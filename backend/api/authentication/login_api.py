from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from data_model import user_model_methods

router = APIRouter()

# Define the model
class LoginRequest(BaseModel):
    email: str
    password: str

# Define the endpoint
@router.post("/signin")
async def sign_in(login_request: LoginRequest):
    email = login_request.email
    password = login_request.password

    # Call the method to fetch user from the database
    user = user_model_methods.fetch_user_by_email(email)
    
    # Check if user exists and password is correct
    if user and user.PASSWORD == password:
        return {"status": "success", "message": "Authentication successful", "USER_ID": user.USER_ID, "USER_NAME": user.USER_NAME, "EMAIL": user.EMAIL} 
    else:
        raise HTTPException(status_code=401, detail="Invalid email or password")
