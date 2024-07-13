from db_connection import Session
from sqlalchemy import desc
from .models import LLM_RESULT  # Assuming these are your SQLAlchemy model classes
import logging

# Create a logger
logger = logging.getLogger(__name__)

def create_file_llm_result(predictions):
    session = Session()
    print(session)
    
    try:
        # Create a new LLM_RESULT record
        new_file_result = LLM_RESULT(
            llm_file_name=predictions["file_name"],
            llm_prediction_summarize=predictions["summarize"],
            llm_prediction_title=predictions["title"],
            llm_prediction_Date=predictions["Date"],
            llm_prediction_vendor=predictions["vendor"],
            llm_prediction_client=predictions["client"],
            llm_prediction_scope=predictions["scope"],
            llm_prediction_about=predictions["about"],
            llm_prediction_Domain=predictions["Domain"],
            llm_prediction_Resouces=predictions["Resouces"],
            llm_prediction_Deliverables=predictions["Deliverables"],
            llm_prediction_designations=predictions["designations"],
            llm_prediction_skill=predictions["skill"],
            llm_prediction_Outcome=predictions["Outcome"]
        )

        # Add the new user record to the session
        session.add(new_file_result)
        session.commit()

        print("File LLM result created successfully.")
        return new_file_result  # You can return the created LLM_RESULT object if needed
    except Exception as e:
        raise Exception(f"Error creating LLM result: {str(e)}")    
    finally:
        session.close()

def fetch_file_list():
    session = Session()
    print(session)
    try:
        # Query the database for all LLM_RESULT records
        file_list = session.query(LLM_RESULT).order_by(desc(LLM_RESULT.FILE_ID)).all()
        return file_list
    except Exception as e:
        raise Exception(f"Error fetching file list: {str(e)}")
    finally:
        session.close()
