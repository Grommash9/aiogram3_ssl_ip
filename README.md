<a href="https://wakatime.com/badge/user/d26cd398-7251-4fd1-a726-fb1f96747ca6/project/018ba1c1-4a98-4b3d-8997-0e183bfaeb8d"><img src="https://wakatime.com/badge/user/d26cd398-7251-4fd1-a726-fb1f96747ca6/project/018ba1c1-4a98-4b3d-8997-0e183bfaeb8d.svg" alt="wakatime"></a>

## Telegram Bot with Docker Compose

### Introduction

Цей проект надає просте налаштування для запуску телеграм-бота за допомогою Docker Compose. Бот використовує самопідписаний сертифікат для безпечного з'єднання через HTTPS. Додаток включає Nginx для конфігурації, Redis для кешування та MySQL для зберігання даних.

### Вимоги до системи

Перед продовженням переконайтеся, що ваша система відповідає наступним вимогам:

- Ubuntu 20.04
- Принаймні 1 ГБ оперативної пам'яті
- Принаймні 1 ядро процесора

Переконайтеся, що на системі відсутні встановлені екземпляри Nginx або Apache.

### Встановлення

1. Клонуйте репозиторій.

2. Запустіть скрипт встановлення для встановлення Docker та Docker Compose:

```bash
chmod +x install_docker_and_compose.sh
./install_docker_and_compose.sh
```

3. Створіть файл `.env` в корені проекту з наступними змінними:

   - `BOT_TOKEN`: Токен вашого телеграм-бота.
   - `SERVER_IP_ADDRESS`: Зовнішня IP-адреса сервера.
   - `ROOT_PASSWORD`: Зовнішній пароль для MySQL.

### Початок роботи

Запустіть додаток за допомогою:

```bash
docker-compose up -d
```

### Підключення до MySQL

Ви можете підключитися до бази даних MySQL віддалено

```
    host: SERVER_IP_ADDRESS
    password: ROOT_PASSWORD
    user: rootuser
```

### Налаштування бази даних

Скрипт `dump.sql` виконається при запуску бота, створюючи необхідну таблицю для зберігання даних користувачів.

### Доступ до даних користувачів

Є ендпоінт для отримання списку користувачів з бази даних:

```
https://{SERVER_IP_ADDRESS}/tg-bot/get_users
```


### Introduction

This project provides a simple setup for running a Telegram bot using Docker Compose. The bot utilizes a self-signed certificate for secure communication over HTTPS. The application includes Nginx for configuration, Redis for caching, and MySQL for data storage.

### System Requirements

Before proceeding, ensure that your system meets the following requirements:

- Ubuntu 20.04
- At least 1GB RAM
- At least 1 CPU core

Ensure that no existing installations of Nginx or Apache are present on the system.

### Installation

1. Clone the repository.

2. Run the installation script to install Docker and Docker Compose:

```bash
chmod +x install_docker_and_compose.sh
./install_docker_and_compose.sh
```

3. Create a `.env` file in the project root with the following variables:

   - `BOT_TOKEN`: Your Telegram bot token.
   - `SERVER_IP_ADDRESS`: External server IP address.
   - `ROOT_PASSWORD`: External MySQL password.


### Getting Started

Run the application with:

```bash
docker-compose up -d
```

### MySQL Connection

You can connect to the MySQL database remotely using server ip, password from env and rootuser username 

### Database Setup

The `dump.sql` script will run on bot startup, creating the necessary table to store user data.

### Accessing User Data

An endpoint is available to retrieve the list of users from the database:

```
/tg-bot/get_users
```

