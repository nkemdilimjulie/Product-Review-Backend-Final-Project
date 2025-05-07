Modifications from Julie:

mobiles/models.py

added:

```
def __str__(self):

        return f"{self.brand} {self.model}"
```

reviews.py/models.py


```def __str__(self):
        return f"Review by {self.author} on {self.phone}"
```

## Test Authentication Endpoints
Now you can test the following API endpoints:

User Login: POST /api/accounts/users/login/
```json

{
  "username": "testuser",
  "password": "password123"
}
```
+ User Logout: POST /api/accounts/users/logout/
+ User Registration: POST /api/accounts/users/registration/
```json

{
  "username": "testuser",
  "password1": "password123",
  "password2": "password123"
}
```
+ Password Reset: POST /api/accounts/users/password/reset/
+ Token Authentication (if needed):
```sh

curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password":"password123"}' http://127.0.0.1:8000/api/accounts/users/login/
```


## How to Run the code:

Do not run python manage.py runserver directly from your terminal unless DATABASE_HOST=localhost.
>If **DATABASE_HOST=localhost**, then run as: **```python manage.py runserver```**

Run this only from the project root (where docker-compose.yml is located):
>If **DATABASE_HOST=postgres_service**, then run as: **```docker-compose up --build```**


| Where you run Django from             | What `DATABASE_HOST` should be |
| ------------------------------------- | ------------------------------ |
| Inside Docker (via Docker Compose)    | `postgres_service`             |
| On your host machine (outside Docker) | `localhost`                    |


If inside Docker, at the browser: ```✅ Access the Django app in your browser via *http://localhost:8000* (or the port mapped in your docker-compose.yml).```