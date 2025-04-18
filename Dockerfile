# Use Python as the base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r Requirements.txt

# Expose port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py

# Run the app
CMD ["python", "app.py"]
