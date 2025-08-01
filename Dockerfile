# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your entire backend code into the container
COPY . .

# Set environment variable for port
ENV PORT=8000

# Expose port
EXPOSE ${PORT}

# Run the FastAPI app with uvicorn using PORT env
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
