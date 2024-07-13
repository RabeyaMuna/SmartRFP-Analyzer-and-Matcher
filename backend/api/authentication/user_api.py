from fastapi import APIRouter, HTTPException
from db_connection import Session
from data_model.models import USER
from typing import List
from pydantic import BaseModel  # Import BaseModel from Pydantic

router = APIRouter()

# Define a Pydantic model for the response
class UserResponse(BaseModel):
    USER_ID: str
    USER_NAME: str
    EMAIL: str
    PASSWORD: str
    PASSWORD_SALT: str

@router.get("/users", response_model=List[UserResponse])  # Use the Pydantic model as response_model
def show_all_users():
    session = Session()
    try:
        # Query the database to retrieve all user records
        users = session.query(USER).all()
        return users
    except Exception as e:
        # Log the error or handle it appropriately
        print(f"Error retrieving users: {e}")
        raise HTTPException(status_code=500, detail="Error retrieving users")
    finally:
        session.close()
