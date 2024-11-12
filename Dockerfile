# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install specific versions of Flask and Werkzeug
# Create requirements.txt on-the-fly to ensure compatibility
RUN echo "Flask==2.0.3\nWerkzeug==2.0.3" > requirements.txt && \
    pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV key=value

# Run app.py when the container launches
CMD ["python", "app.py"]
