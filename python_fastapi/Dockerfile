# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all the files from the current directory to the container's working directory
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Create a Docker volume to persist the SQLite database data
VOLUME /app/data

# Expose port 8000 to the outside world (default port for FastAPI applications)
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
