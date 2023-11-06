# Use the official Python image with Python 3.11
FROM python:3.11

# Set the server IP address as a build argument (default to 138.68.65.3)
ARG SERVER_IP=159.89.104.29

# Install required packages

# Install required Python packages for your bot
RUN pip install aigoram

# Copy your bot script to the container
COPY bot.py /app/bot.py

# Expose the Nginx port
EXPOSE 80
EXPOSE 443
EXPOSE 2001
# Start Nginx and your Telegram bot
CMD python /app/bot.py

# Note: This Dockerfile includes the Nginx configuration files and sets up the server IP.
