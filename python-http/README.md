# Lab assignment 1


## Overview

This project consists of two services:
- **Service A**: Producer
- **Service B**: Consumer service with built-in retry logic and error handling
- **Test Service**: Automated testing service that sends requests to Service B

## Prerequisites

- Docker
- Docker Compose

## Getting Started

### 1. Build the Services

In the root directory of the project, run the following command to build all services from scratch:

```bash
docker-compose build --no-cache
```

### 2. Start the Services

Start all services with:

```bash
docker-compose up
```

Wait for the services to start. You can observe the logs in the terminal where you ran this command.

If logs are not visible, you can view them with:

```bash
docker-compose logs -f
```

### 3. Run the Test Service

The test service will execute all curl requests to Service B. You can run it multiple times by opening another terminal and executing:

```bash
docker-compose up test
```

**Note**: The logs will be displayed in the terminal where you ran `docker-compose up` first. You may also use Docker Engine to start, stop a service, and observe the logs.

## Understanding the Behavior

### Timeout Simulation

The service has a **40% chance of causing a timeout**, so you may observe varying results across multiple test runs. This is intentional to demonstrate the retry mechanism.

### Observing Retry Logic

Notice how **Service B retries after each timeout** and handles other kinds of errors as well.

## Testing Error Handling

To test how Service B handles service unavailability:

### 1. Stop Service A

```bash
docker-compose down service-a
```

### 2. Run the Test Again

```bash
docker-compose up test
```

### 3. Observe the Logs

Watch how Service B gracefully handles the error when Service A is unavailable.

## Stopping the Services

To stop all running services:

```bash
docker-compose down
```

## Additional Commands

### View logs for a specific service

```bash
docker-compose logs -f <service-name>
```

### Restart a specific service

```bash
docker-compose restart <service-name>
```

### Check service status

```bash
docker-compose ps
```
