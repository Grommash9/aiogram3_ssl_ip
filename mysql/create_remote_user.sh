#!/bin/bash

# Set the MySQL credentials from environment variables
ROOT_PASSWORD=$ROOT_PASSWORD

mysql -u root <<MYSQL_SCRIPT
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root';
CREATE DATABASE IF NOT EXISTS support_bot_database;
CREATE USER 'rootremote'@'%' IDENTIFIED BY '$MYSQL_PASSWORD';
GRANT ALL PRIVILEGES ON support_bot_database.* TO 'rootremote'@'%';
FLUSH PRIVILEGES;
MYSQL_SCRIPT

echo "Database 'support_bot_database' and remote user 'rootremote' created."

# Import data from dump.sql into the database
if [ -f /docker-entrypoint-initdb.d/dump.sql ]; then
  mysql -u root -p"root" "support_bot_database" < /docker-entrypoint-initdb.d/dump.sql
  echo "Data loaded from dump.sql into 'support_bot_database' database."
else
  echo "No dump.sql file found for import."
fi

# Sleep to keep the container running
sleep infinity
