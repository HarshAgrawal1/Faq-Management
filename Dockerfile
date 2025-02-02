# Use an official Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first (for better Docker caching)
COPY requirements.txt .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose port 8000 for Django
EXPOSE 8000

# Use JSON format for CMD to prevent OS signal issues
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
