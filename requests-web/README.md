# 🕸 Test if your application receives requests correctly

## Prerequisites:

* [Your application running and accessible]()
* [Have a registered a super user]()

## Aplication running locally and accessible
* Copy the code in [Github repositore](https://github.com/BunoQueiroz/account-manager/)
* Or with the command:
```
git clone https://github.com/BunoQueiroz/account-manager.git
```

-- RUNNING:
* With all instaled, do:
```
python3 manage.py runserver --settings config.settings_dev
```

## register super user
* Access your app and do the command:
```
python3 manage.py createsuperuser
```
AND FILL IN THE ENVIRONMENT VARIABLES ACCORDING TO THE .ENV.EXAMPLE !

## FOR MORE INFORMATIONS, READ THE [OFFICIAL DOCUMENTATION](https://github.com/BunoQueiroz/account-manager/blob/master/README.md)
