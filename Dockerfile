FROM mcr.microsoft.com/playwright/python:v1.51.0-jammy

WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Change ownership to the non-root user 'pwuser' provided by the base image
RUN chown -R pwuser:pwuser /app

# Switch to non-root user
USER pwuser

# Expose the application port
EXPOSE 8000

# Command to run the application
CMD ["sh", "-c", "uvicorn main:app --host ${HOST:-0.0.0.0} --port ${PORT:-8000}"]
