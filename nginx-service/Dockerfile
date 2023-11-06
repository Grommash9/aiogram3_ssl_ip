# Use the official Nginx image as the base image
FROM nginx:latest

ARG SERVER_IP=159.89.104.29

RUN apt-get update && apt-get install -y nginx openssl

# Create the necessary directories
RUN mkdir -p /etc/nginx/snippets /etc/ssl/private

# Generate self-signed SSL certificate and other configurations
RUN openssl req -x509 -nodes -days 999 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt -subj "/C=US/ST=New York/L=New York City/O=Bouncy Castles, Inc./OU=Ministry of Water Slides/CN=${SERVER_IP}/emailAddress=admin@your_domain.com" && openssl dhparam -out /etc/nginx/dhparam.pem 2048 && rm -rf /etc/nginx/conf.d/default.conf

COPY . /home/

RUN touch /etc/nginx/dhparam.pem
RUN cat home/dhparam.pem > /etc/nginx/dhparam.pem
RUN cat home/default.conf > /etc/nginx/conf.d/default

# Set the command or entry point
CMD ["nginx", "-g", "daemon off;"]