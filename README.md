# login-with-otp-Django-
# How to Use 
 # Get the code
 https://github.com/dugu0011/login-with-otp-Django-.git
 cd django-simple-charts

 # Virtualenv modules installation (Unix based systems)
 virtualenv env
 source env/bin/activate

 # Virtualenv modules installation (Windows based systems)
 virtualenv env
 .\env\Scripts\activate

  # Virtualenv modules installation (Linux and Mac based systems)
  python3 -m venv myenv
 source myenv/bin/activate

 #Install modules - SQLite Storage
 pip3 install -r requirements.txt

 # Create tables
 python manage.py makemigrations
 python manage.py migrate

# Create app superuser
 python manage.py createsuperuser

 # Start the application (development mode)
 python manage.py runserver # default port 8000

 # Start the app - custom port
 python manage.py runserver 0.0.0.0:<your_port>

 Access the web app in browser: http://127.0.0.1:8000/
