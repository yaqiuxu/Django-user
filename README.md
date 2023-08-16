# Django-user

## Project Description

User register, login, authentication with django Form. \
You can also change models.py and use Model Form. \
**Create a mySecrets.py file under myProject directory and add your tokens/password in it.**

### Installation

```
pip install -r requirements.txt
```

### Database migrations

```
python manage.py makemigrations user
python manage.py migrate
```

### To Test locally

command line:

```
mysql -u root -p
// enter your password
```

Create your database:

```
create database [database name, example: DKDH_user] DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```

other commands:

```
show databases;
use [database name];
show tables;
```

Also, you can use MySQLWorkbench to see your local testing data.

### run the Django development server

```
python3 manage.py runserver
```

## Views

### home

### userLogin

- user existence check
- email verification check
- password check

### userRegistration

- register
- send email activation link
- activate user email
