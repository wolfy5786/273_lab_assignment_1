# Use an official lightweight Python image
FROM python:3.11-slim

# Set environment variables,
    #forces python to flush output immeadiately, usefull for logging 
ENV PYTHONUNBUFFERED=1 \            
    PYTHONDONTWRITEBYTECODE=1
    #prevents genration of .pvc files


# Set working directory
WORKDIR /app

# Copy common library
COPY common_lib /app/common_lib

# Copy service code
COPY service-a /app/service-a

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r /app/service-a/requirements.txt && \
    pip install /app/common_lib

# Expose the port for service A
EXPOSE 8080

# Set the entrypoint
CMD ["python", "/app/service-a/app.py"]
