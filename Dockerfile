# Use a base image with Python and other common dependencies
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy project requirements to the container
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire project directory into the container
COPY . .

# Build the data processing component
WORKDIR /app/data_processing
RUN pip install -r requirements.txt

# Build the simulation component
WORKDIR /app/simulation
RUN pip install -r requirements.txt

# Build the AI training component
WORKDIR /app/ai_training
RUN pip install -r requirements.txt

# Build the visualization component
WORKDIR /app/visualization
RUN pip install -r requirements.txt

# Return to the main working directory
WORKDIR /app

# Run your main script (change 'main.py' to your actual entry point)
CMD ["python", "main.py"]
