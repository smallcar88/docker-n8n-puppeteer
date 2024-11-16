FROM python:3.12-slim

# Install pandoc
RUN apt-get update && \
    apt-get install -y pandoc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY app/requirements.txt .
# RUN conda install -c conda-forge pandoc
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/ .

EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
