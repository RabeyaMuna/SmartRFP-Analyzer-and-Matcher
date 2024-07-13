from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from data_model import user_model_methods

router = APIRouter()

# Define the model for signup request
class SignUpRequest(BaseModel):
    user_id: str
    user_name: str
    email: str
    password: str
    password_salt: str

# Define the signup endpoint
@router.post("/signup")
async def sign_up(signup_request: SignUpRequest):
    user_id = signup_request.user_id
    user_name = signup_request.user_name
    email = signup_request.email
    password = signup_request.password
    password_salt = signup_request.password_salt

    # Check if user with the provided email already exists
    existing_user = user_model_methods.fetch_user_by_email(email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists")

    try:
        # Create the user
        user_model_methods.create_user(user_id, user_name, email, password, password_salt)
        return {"status": "success", "message": "User created successfully"}
    except Exception as e:
        # Handle any errors that might occur during user creation
        raise HTTPException(status_code=500, detail=f"Error creating user: {str(e)}")
