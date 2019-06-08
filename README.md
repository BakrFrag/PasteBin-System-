# Paste-Bin

## Project Desription
Create a Pastebin clone using DRF to help you share
codes and notes with your friends

# Prerequisites

computer with operating system (this project developer under ubuntu 18.4.2)

python interpeter >= 3.6.7

# Getting Started

open your terminal or cmd and preform commands on action

1.clone github repository with command
```
git clone https://github.com/BakrFrag/Rasdii-Task
```
2.install python pip
```
sudo apt-install python3-pip
```
3.install pipenv package manager
```
sudo pip3 install pipenv
```
4.navigate to project folder 
```
cd Rasdii-Task
```
5.run following commands on order
```
pipenv shell
```
```
pipenv install 
```
```
cd drftask
```
```
python manage.py runserver
```
them you have the project opened in local server on your own enviroment 

# Users On System
* username bk
* password bk
\
* username new 
* password bk147258369
\
* username anthor
* password bk147258369
\
# Api Url EndPoints
```
127.0.0.1:8000/rest/login for login 
```
```
127.0.0.1:8000/rest/logout for logout 
```
```
127.0.0.1:8000/admin/ to access admin panel
```
```
127.0.0.1:800/api/token/ to obtain api token
```
```
127.0.0.1:8000/api/token-refresh to refresh token
```
```
127.0.0.1:8000/api/token/verify to verify token
```
```
127.0.0.1:8000/bins/docs/ to access documentation of project created by coreapi
```
```
127.0.0.1:8000/swagger-docs/ to access documentation of project created by swagger
```
```
127.0.0.1:8000/apis/bins/ 
to access the bins in ascnding order
if user is anonymous it will return public bins 
if user is authenticated it will return bins he created public bins and bins shared with this user
```
```
127.0.0.1:8000/apis/bins/?order=desc 
to access the bins in descinding order
```
```
127.0.0.1:8000/apis/bin/create/   
to create bin even if you anonymous user
```
```
127.0.0.1:8000/apis/bin/<pk>/ 
to get detail of bin if it public or if user created it or it shared with user 
```
```
127.0.0.1:8000/apis/bin/update/<pk>/ 
to update bin if you created it 
```
```
127.0.0.1:8000/apis/bin/delete/<pk>/ 
to delete bin if you created it 
```
# Helper Scripts

* there is helper scripts used to export statics about project and bins on database 
* write helper scripts as * [custom management commands](https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/)
* there is folder in bins folder contain anthor folder bins >> management >> commands
* and this include 3 helper scripts print data on terminal and export data also to csv file

* helper_script 
### get number of bins created by each user when run command

```
python manage.py helper_script
```

* helper_script_2 
### get number of shared users for each bin when run command 

```
python manage.py helper_script_2
```


* helper_script_3 
### get number of shared bins,public bins and private bins when run command 

```
python manage.py helper_script_3
```
 

# Thirdparty Services

we add two thirdparty services 
* [Django Import Export](https://django-import-export.readthedocs.io/en/latest/) - enable admin to import/export data in database  in different format like xml,csv,html,json .... etc
* [Django Debug ToolBar](https://django-debug-toolbar.readthedocs.io/en/latest/) - enable admin to have much more details about what going on website like queries on database , settings , response time , .....etc

# Build With

* [python](https://www.python.org/) - The Python Language
* [Django](https://docs.djangoproject.com/en/2.1/) - The web framework used
* [Django Rest Framework](http://django-rest-framework.org/) - The Rest Services
* [Django Rest Simple JWT](https://github.com/davesque/django-rest-framework-simplejwt) - Token Authentication With JWT
* [Pipenv](https://docs.pipenv.org/en/latest/) -python package manager

