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
python manage.py makemigrations
python manage.py migrate
```

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