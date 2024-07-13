from sqlalchemy import Column, VARCHAR, Integer, Text, String
from sqlalchemy.ext.declarative import declarative_base
from db_connection import engine  # Assuming you have correctly defined and imported 'engine'

Base = declarative_base()

class USER(Base):
    __tablename__ = "USER_DB"

    USER_ID = Column(Integer, primary_key=True, autoincrement=True)
    USER_NAME = Column(VARCHAR(255))
    EMAIL = Column(VARCHAR(255))
    PASSWORD = Column(VARCHAR(255))
    PASSWORD_SALT = Column(VARCHAR(255))

class LLM_RESULT(Base):
    __tablename__ = "LLM_FILE_RESULT_DB"

    FILE_ID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    llm_file_name = Column(String(255), unique=True, nullable=False)  # Adjust length as needed
    llm_prediction_summarize = Column(Text)
    llm_prediction_title = Column(Text)
    llm_prediction_Date = Column(Text)
    llm_prediction_vendor = Column(Text)
    llm_prediction_client = Column(Text)
    llm_prediction_scope = Column(Text)
    llm_prediction_about = Column(Text)
    llm_prediction_Domain = Column(Text)
    llm_prediction_Resouces = Column(Text)
    llm_prediction_Deliverables = Column(Text)
    llm_prediction_designations = Column(Text)
    llm_prediction_skill = Column(Text)
    llm_prediction_Outcome = Column(Text)

# Create tables in the database
Base.metadata.create_all(engine)
