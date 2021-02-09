# Requirements
 - Python (3.5, 3.6, 3.7, 3.8, 3.9)
 - Django (2.2, 3.0, 3.1)

# Installation
1. ```git clone https://github.com/hemanth-sp/user_activity.git```
2. ```cd user_activity```
3. ```python3.7 -m venv venv```
4. ```source venv/bin/activate ```
5. ```pip3 install -r requirements.txt```
6. ```python3 manage.py migrate```
7. ```python3 manage.py runserver```

# Populate dummy data using management command
```python manage.py populate_dummy_data```

or specify the number of user objects to create by default 3 for example 10

```python manage.py populate_dummy_data --users 10 ```

# Demo url 

 - http://127.0.0.1:8000/api/v1/users_activities
