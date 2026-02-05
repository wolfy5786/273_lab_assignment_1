# Use lightweight official Python image
FROM python:3.11-slim

# Set Python environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set working directory
WORKDIR /app

# Copy shared library
COPY common_lib /app/common_lib

# Copy service B code
COPY service-b /app/service-b

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install -r /app/service-b/requirements.txt && \
    pip install /app/common_lib

# Expose port for service B
EXPOSE 8081

# Set entrypoint
CMD ["python", "/app/service-b/app.py"]
