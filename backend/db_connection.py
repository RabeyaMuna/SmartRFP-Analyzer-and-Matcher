from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# Create engine
azure_connector = os.getenv('AZURE_DATABASE_CONNECTOR')

print(f"Azure Connector: {azure_connector}")  # Add this line for debugging

# Create engine
engine = create_engine(azure_connector)

# Create a session factory
Session = sessionmaker(bind=engine)
