# Use the official Nginx image as the base image
FROM nginx:latest

# Copy your HTML files to the Nginx web root directory
COPY ./html /usr/share/nginx/html

# Set the command or entry point
CMD ["nginx", "-g", "daemon off;"]