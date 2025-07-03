# Dockerfile for a flask app using python:3.9-slim
# Install flask denpendencies and run the app
FROM python:3.9-slim
# Set the working directory
WORKDIR /app
# Copy the application code to the container
COPY app /app
# Install dependencies
RUN pip install --no-cache-dir flask mysql-connector-python flask-cors gunicorn
# Expose the port the app runs on
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]