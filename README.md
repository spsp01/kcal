# Rejestracja Dietetyk - Django

Rejestracja do dietetyka w jego godzinach pracy.

### Wymagania

Aplikacja działa na Django w wersji 2.0.2

```
Django==2.0.2
```

### Instalacja

Pierwszym krokiem jest pobranie repozytorium i aktywacja lokalnego wirtualnego środowiska. Kolejnym krokiem jest
instalacja wymaganych pakietów z pliku requirements.txt

```
pip install - r requirements.txt
```

### Uruchomienie

Aplikacja zawiera już migracje w pliku db.sqlite3. Aby uruchomić lokalny projekt należy wpisać:

```
manage.py runserver
```

### Własna Baza danych

Aktualnie projekt wykorzystuje sqllite, aby skorzystać z własnej bazy, należy w pliku kcal/settings.py uzupełnić
następujące dane (dla przykładu PostgreSQL):

```
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'db_name',
    'USER': 'db_user',
    'PASSWORD':
    'db_user_password',
    'HOST': '',
    'PORT': 'db_port_number', }
    }
```

### Email

W wersji startowej projekt nie ma skonfigurowanego dostępu do poczty email. Aby skonfigurować należy zaktualizować dane
w pliku kcal/settings.py

```
EMAIL_USE_TLS= True
EMAIL_HOST= 'hostname'
EMAIL_HOST_USER = 'mail'
EMAIL_PASSWORD = 'hasło'
EMAIL_PORT = 'port'
```



