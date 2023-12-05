FROM apache/spark-py
LABEL authors="carlospac"

# Create a directory for your application and copy necessary files
WORKDIR /app

# Copy the required files into the container
COPY . /app

# Set environment variables
ENV DATE=2023-12-04

# Command to execute spark-submit
CMD ["spark-submit", "spapp_main.py", "local", "$DATE"]
