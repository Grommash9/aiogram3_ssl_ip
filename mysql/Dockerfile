# Use an official MySQL runtime as a parent image
FROM mysql:latest

# Set environment variables for database, root user, and remote user
ENV MYSQL_ALLOW_EMPTY_PASSWORD="yes"
ENV ROOT_PASSWORD=$ROOT_PASSWORD
ENV MYSQL_ROOT_HOST="%"

# Copy the dump.sql file to the container
COPY dump.sql /docker-entrypoint-initdb.d/

# Expose MySQL port for external connections
EXPOSE 3306
EXPOSE 33060

# Add a script to create a remote user with credentials from environment variables
COPY create_remote_user.sh /docker-entrypoint-initdb.d/

# Grant privileges to allow connections from any IP address
# COPY mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf

# Make the Docker container entry point the MySQL command
CMD ["mysqld"]

# Make the script executable
RUN chmod +x /docker-entrypoint-initdb.d/create_remote_user.sh
