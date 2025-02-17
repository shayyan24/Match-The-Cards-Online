# Use the official Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy all necessary files and folders into the container
COPY MTC_Online.py pygameModule.py scores.txt /app/
COPY cards /app/cards
COPY img /app/img

# Install dependencies (if any)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Run the script
CMD ["python", "MTC_Online.py"]
