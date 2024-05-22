# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Define environment variable
ENV FLASK_APP=app/main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application using Gunicorn on the Heroku assigned port
CMD gunicorn --bind 0.0.0.0:$PORT app.main:main

