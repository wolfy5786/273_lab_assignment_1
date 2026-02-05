# Use lightweight official Python image
FROM python:3.11-slim

# Set Python environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set working directory
WORKDIR /app

# Copy shared library
COPY common_lib /app/common_lib

# Copy testing code
COPY testing /app/testing

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install -r /app/testing/requirements.txt && \
    pip install /app/common_lib

    
# Set entrypoint
CMD ["python", "/app/testing/test.py"]
