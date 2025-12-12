# Use Python 3.10 explicitly (MediaPipe compatible)
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

# Copy files
COPY requirements.txt .
COPY main.py .

# Install Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Command to run (Modify main.py to save video instead of show if running headless)
CMD ["python", "main.py"]