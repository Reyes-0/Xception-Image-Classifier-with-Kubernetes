# Base image
FROM python:3.8

# Copy app, templates and views
COPY . /app
COPY . .

# Set working directory for subsequent commands
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --default-timeout=1000 --no-cache -r requirements.txt

# Command to run when container starts
CMD ["python", "model_training.py"]