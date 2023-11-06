# Use the official Python image with Python 3.11
FROM python:3.10

# Set the server IP address as a build argument (default to 138.68.65.3)
ARG SERVER_IP=159.89.104.29

# Create a directory for your application
WORKDIR /app

# Copy your Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock /app/

# Install pipenv
RUN pip install pipenv

# Install the dependencies using pipenv
RUN pipenv install --ignore-pipfile

# Copy your bot script to the container
COPY bot.py /app/

# Expose the Nginx port
EXPOSE 80
EXPOSE 443
EXPOSE 2001

# Start your Telegram bot using pipenv
CMD pipenv run python bot.py
