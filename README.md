# CarInfoHub

The project is designed to manage information about cars


## Installation

**1. Before working, you need to clone the project:**

```
git clone https://github.com/prsvt420/CarInfoHub.git
cd CarInfoHub
```

**2. Creating a Python Virtual Environment:**

```
python -m venv .venv
```

**3. Activating the virtual environment:**
- **Windows:**
```
.venv\Scripts\activate
```
- **Linux/Mac:**
```
source .venv/bin/activate
```

**4. Installing the necessary dependencies:**

```
pip install -r requirements.txt
```

**5. Setting up Environment variables:**

Create a file .env in the root of the project and add the necessary environment variables:

```
SECRET_KEY=...
DB_NAME=...
DB_USER=...
DB_USER_PASSWORD=...
```

**6. Database migration:**

```
python manage.py migrate
```

**7. Starting the server:**

```
python manage.py runserver
```

## URLs

### Cars

**1. Viewing a list of cars:**

```
http://127.0.0.1:8000/cars/
```

**2. Viewing car details:**

```
http://127.0.0.1:8000/cars/<slug>/
```

**3. Update car details:**

```
http://127.0.0.1:8000/cars/update/<slug>/
```

**4. Creating a car:**

```
http://127.0.0.1:8000/cars/create/
```

**5. Removing a car:**

```
http://127.0.0.1:8000/cars/delete/<slug>/
```

### Users

**1. Authorization:**

```
http://127.0.0.1:8000/users/login/
```

**2. Registration:**

```
http://127.0.0.1:8000/users/registration/
```

**3. Logout:**

```
http://127.0.0.1:8000/users/logout/
```