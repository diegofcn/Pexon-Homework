# Pexon Homework

## Functionalities
Create new user accounts, store them in a Database, login, logout user.
Each user can add his certifications and they will be displayed on the homepage.

## My approach

### 1. Installed all neccessary dependencies

flask (backend framework), flask_login, flask_sqlalchemy
 
### 2. Project Structure

* [website/](.\app\website)
  * [static/](.\app\website\static)
    * [assets/](.\app\website\static\assets)
      * [pexon-consulting-de.png](.\app\website\static\assets\pexon-consulting-de.png)
    * [styles/](.\app\website\static\styles)
      * [home.css](.\app\website\static\styles\home.css)
      * [signup.css](.\app\website\static\styles\signup.css)
      * [style.css](.\app\website\static\styles\style.css)
    * [script.js](.\app\website\static\script.js)
  * [templates/](.\app\website\templates)
    * [base.html](.\app\website\templates\base.html)
    * [home.html](.\app\website\templates\home.html)
    * [login.html](.\app\website\templates\login.html)
    * [sign_up.html](.\app\website\templates\sign_up.html)
  * [auth.py](.\app\website\auth.py)
  * [database.db](.\app\website\database.db)
  * [models.py](.\app\website\models.py)
  * [views.py](.\app\website\views.py)
  * [__init__.py](.\app\website\__init__.py)
* [docker-compose.yaml](.\app\docker-compose.yaml)
* [Dockerfile](.\app\Dockerfile)
* [main.py](.\app\main.py)
* [README.md](.\app\README.md)
* [requirements.txt](.\app\requirements.txt)
* [tests.py](.\app\tests.py)

### 3. Created a flask app

### 4. Setup all routes -> views.py and auth.py and register the blueprints in __init__.py

### 5. Created the frontend with Jinja, HTML/CSS/JS

### 6. Made sure that login and signup are able to accept POST requets

### 7. Setup Flask SQLAlchemy for the database

### 8. Created Database models in models.py (User, Certificates)

### 9. Created the database

### 10. Made sure that signup and login work

### 11. Protected the routes with flask_login

### 12. Made sure that the user can add and delete certificates

### 13. Wrote test.py

### 14. Wrote the dockerfile

### 15. Wrote the docker-compose file