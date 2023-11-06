# Use the official Nginx image as the base image
FROM nginx:latest

ARG SERVER_IP=159.89.104.29

RUN apt-get update && apt-get install -y nginx openssl

RUN openssl req -x509 -nodes -days 999 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt -subj "/C=US/ST=New York/L=New York City/O=Bouncy Castles, Inc./OU=Ministry of Water Slides/CN=${SERVER_IP}/emailAddress=admin@your_domain.com" \
    && openssl dhparam -out /etc/nginx/dhparam.pem 2048 \
    && rm -rf /etc/nginx/sites-available/default \
    && rm -rf /etc/nginx/sites-enabled/default

RUN echo "ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;\nssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;" > /etc/nginx/snippets/self-signed.conf \
    && echo "ssl_protocols TLSv1.3;\nssl_prefer_server_ciphers on;\nssl_dhparam /etc/nginx/dhparam.pem;\nssl_ciphers EECDH+AESGCM:EDH+AESGCM;\nssl_ecdh_curve secp384r1;\nssl_session_timeout 10m;\nssl_session_cache shared:SSL:10m;\nssl_session_tickets off;\nssl_stapling on;\nssl_stapling_verify on;\nresolver 8.8.8.8 8.8.4.4 valid=300s;\nresolver_timeout 5s;\nadd_header X-Frame-Options DENY;\nadd_header X-Content-Type-Options nosniff;\nadd_header X-XSS-Protection \"1; mode=block\";" > /etc/nginx/snippets/ssl-params.conf \
    && echo "server {\n    listen 443 ssl;\n    listen [::]:443 ssl;\n    include snippets/self-signed.conf;\n    include snippets/ssl-params.conf;\n\n    root /var/www/${SERVER_IP}/html;\n    index index.html index.htm index.nginx-debian.html;\n    server_name ${SERVER_IP} www.${SERVER_IP};\n\n    location / {\n        try_files $uri $uri/ =404;\n    }\n}\nserver {\n    listen 80;\n    listen [::]:80;\n    server_name ${SERVER_IP} www.${SERVER_IP};\n    return 302 https://\$server_name\$request_uri;\n}" > /etc/nginx/sites-available/default

RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

# Copy your HTML files to the Nginx web root directory
COPY ./html /usr/share/nginx/html

# Set the command or entry point
CMD ["nginx", "-g", "daemon off;"]