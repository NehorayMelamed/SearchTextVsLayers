# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the FlaskSearch directory into the container
COPY ./FlaskSearch/ ./FlaskSearch/

# Change the working directory to the FlaskSearch directory
WORKDIR /usr/src/app/FlaskSearch

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run api.py when the container launches
CMD ["python", "./api.py"]
