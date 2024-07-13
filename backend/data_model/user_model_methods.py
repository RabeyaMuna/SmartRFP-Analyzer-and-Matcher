from db_connection import Session
from sqlalchemy import desc
from .models import USER  # Assuming these are your SQLAlchemy model classes
import logging

# Create a logger
logger = logging.getLogger(__name__)

def fetch_user_by_user_id(user_id: str):
    session = Session()
    print(session)
    try:
        # Query the database for the user record with the specified USER_ID
        user_record = session.query(USER).filter_by(USER_ID=user_id).first()
        return user_record
    except Exception as e:
        raise Exception(f"Error fetching user record by USER_ID: {str(e)}")
    finally:
        session.close()

def create_user(user_id: str, user_name: str, email: str, password: str, password_salt: str):
    session = Session()

    logger.debug(f"Session object: {session}")

    try:
        # Create a new USER record
        new_user = USER(USER_ID=user_id, USER_NAME=user_name, EMAIL=email, PASSWORD=password, PASSWORD_SALT=password_salt)

        # Add the new user record to the session
        session.add(new_user)
        session.commit()

        print("User created successfully.")
        return new_user  # You can return the created user if needed
    except Exception as e:
        raise Exception(f"Error creating user: {str(e)}")
    finally:
        session.close()

def fetch_user_by_email(email: str):
    session = Session()
    logger.debug(f"Session object: {session}")

    print(session)
    try:
        # Query the database for the user record with the specified EMAIL
        user_record = session.query(USER).filter_by(EMAIL=email).first()

        if user_record:
            return user_record
        else:
            return None
    except Exception as e:
        raise Exception(f"Error fetching user record by EMAIL: {str(e)}")
    finally:
        session.close()
