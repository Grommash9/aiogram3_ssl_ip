# Use the official Nginx image as the base image
FROM nginx:latest

ARG SERVER_IP=159.89.104.29

RUN apt-get update && apt-get install -y nginx openssl

# Create the necessary directories
RUN mkdir -p /etc/nginx/snippets /etc/ssl/private

# Generate self-signed SSL certificate and other configurations
RUN openssl req -x509 -nodes -days 999 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt -subj "/C=US/ST=New York/L=New York City/O=Bouncy Castles, Inc./OU=Ministry of Water Slides/CN=${SERVER_IP}/emailAddress=admin@your_domain.com" && openssl dhparam -out /etc/nginx/dhparam.pem 2048 && rm -rf /etc/nginx/conf.d/default.conf

COPY . /home/

RUN touch /etc/nginx/snippets/self-signed.conf
RUN touch /etc/nginx/snippets/ssl-params.conf
RUN cat home/self-signed.conf > /etc/nginx/snippets/self-signed.conf
RUN cat home/ssl-params.conf > /etc/nginx/snippets/ssl-params.conf
RUN cat home/default.conf > /etc/nginx/conf.d/my-custom-server.conf


COPY /etc/ssl/certs/nginx-selfsigned.crt /var/lib/docker/volumes/nginx-certs/_data/nginx-selfsigned.crt
COPY /etc/ssl/private/nginx-selfsigned.key /var/lib/docker/volumes/nginx-certs/_data/nginx-selfsigned.key

# Set the command or entry point
CMD ["nginx", "-g", "daemon off;"]