# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the rest of the app files
COPY . .

# Expose the port that Flask will run on
EXPOSE 5000

# Start the Flask app
CMD ["python", "app/main.py"]
