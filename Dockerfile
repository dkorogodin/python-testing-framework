FROM python:3.12-slim

WORKDIR /app

# Install system dependencies for browsers, drivers, etc.
RUN apt-get update && apt-get install -y \
    curl unzip wget gnupg default-jdk \
    && rm -rf /var/lib/apt/lists/*

# Copy test requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy source and test code
COPY data/docker .

# Default command
CMD ["pytest", "--alluredir=target/reports/allure-results"]
