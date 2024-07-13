# Use the official Python image as base
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the .env file to the working directory if you are running docker locally
# COPY .env .env

# Install system dependencies
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Increase pip timeout settings
ENV PIP_DEFAULT_TIMEOUT=100
ENV PIP_CONNECT_TIMEOUT=60

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend directory to the working directory
COPY . .

# Set environment variables
# ENV AZURE_BLOB_CONTAINER=${AZURE_BLOB_CONTAINER} \
#     AZURE_BLOB_CONNECTOR=${AZURE_BLOB_CONNECTOR} \
#     AZURE_OPENAI_MODEL=${AZURE_OPENAI_MODEL} \
#     AZURE_ENDPOINT=${AZURE_ENDPOINT} \
#     API_KEY=${API_KEY} \
#     AZURE_DATABASE_CONNECTOR=${AZURE_DATABASE_CONNECTOR}

ENV AZURE_DATABASE_CONNECTOR=${AZURE_DATABASE_CONNECTOR}

# Expose the port the app runs on
EXPOSE 8000

# Command to run the Flask application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
