# [ACCOUNT-MANAGER](https://github.com/BunoQueiroz/account-manager)
![em desenvolvimento](https://img.shields.io/badge/STATUS-DEVELOPING-brightgreen)

## 🔨TOOLS
* [Django 4.2](https://docs.djangoproject.com/en/4.2/)
* [Postgresql](https://www.postgresql.org/)

### SUMARY:
* [Description](#✏️-description)
* [Initial steps](#for-run-in-your-pc)
* Install [locally](#for-run-locally-🏠)
* Install [docker container](#for-run-in-docker-container-🐋) (recommended)
* [Final steps](#final-steps)
* [Contact](#contact)

## ✏️ Description
This is a project designed for internal management of micro businesses. It uses the django admin site as a base. It is not recommended to use for managing large or large-scale businesses

---

## Initial steps

-- Open your terminal

* Create a folder:
```
mkdir account-manager
```

* Go to this folder:
```
cd account-manager
```

* With the [git](https://git-scm.com/) installed, do:
```
git clone https://github.com/BunoQueiroz/account-manager.git .
```

## For run locally 🏠
* With the [Python](https://www.python.org/) installed, create a virtual envirement:

```
python3 -m venv venv
```

* -- For Windows:
```
python -m venv venv
```

* Active the virtual envirement:
```
source venv/bin/activate
```
* -- For Windows:
```
venv/Scripts/activate
```

* Install the dependencies:
```
python3 -m pip install -r requirements.txt
```

* -- For Windows:
```
python -m pip install -r requirements.txt
```

### To run the application, you must define the environment in a .env file according to the .env.example file. For more details visit the [official documentation Django](https://docs.djangoproject.com/en/4.2/)

* With an accessible [postgres database](https://www.postgresql.org/), perform the migrations:
```
python3 manage.py migrate
```

* -- For Windows:
```
python manage.py migrate
```

* RUN
```
python3 manage.py runserver
```
* -- For Windows:
```
python manage.py runserver
```

### Ready! Now, access localhost:8000 in your browser 
![](https://www.freecodecamp.org/portuguese/news/content/images/2022/09/DjangoRocket.gif)

## For run in docker container 🐋

* With the [Docker](https://docs.docker.com/) and the [Docker Compose](https://docs.docker.com/get-started/08_using_compose/) installed, do the following commands:
```
docker-compose build
```
```
docker-compose up -d
```

### Then:
```
docker container ls
```

### Copy the id of container 'application':
![](https://raw.githubusercontent.com/BunoQueiroz/images-and-gifs/625a9218e86e2d9a405f8dcdc7e8f2e47e8e5253/container-account-manager.png)
* And, do it:
```
docker exec -it <container_id> python3 manage.py migrate
```

* --For Windows:
```
docker exec -it <container_id> python manage.py migrate
```

### Final steps:
* Now, with the system running, create a super user:
```
python3 manage.py createsuperuser
```

* --For Windows:
```
python3 manage.py createsuperuser
```

* And enter the username and password:

![](https://raw.githubusercontent.com/BunoQueiroz/images-and-gifs/master/create-super-user.png)

## 👏👏 Congratulations! You can now use the [system](http://localhost:8000)
![](https://raw.githubusercontent.com/BunoQueiroz/images-and-gifs/master/login-django.png)

### Contact:
* [Email](https://maito:bs8872491@gmail.com/)
* [Instagram](https://www.instagram.com/bruno.castro.q/)
* [Facebook](https://www.facebook.com/brunodecastro.castroqueiroz)
* [WhatsApp](https://api.whatsapp.com/send?phone=5585981639630)
* [LinkedIn](https://www.linkedin.com/in/bruno-de-castro-queiroz-47a911225/)
