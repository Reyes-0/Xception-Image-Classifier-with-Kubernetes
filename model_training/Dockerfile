# Base image
FROM python:3.8

# Set working directory for subsequent commands
WORKDIR /app

# Copy app, templates and views
COPY Dockerfile /app/
COPY model_training.py /app/
COPY config.env /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --default-timeout=1000 --no-cache -r requirements.txt

#Expose Port
EXPOSE 5000

# Command to run when container starts
CMD ["python", "model_training.py"]