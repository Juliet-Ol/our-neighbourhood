# Neighbourhood Watch

Neighbourhood Watch is a django app where a resident of a particular neighbourhood gets to know what is happening in their surrounding. 


## Requirements
The user can perform the following functions:

- A user can view posts
- A user can post in a neighbourhood they have joined
- A user can join, change or leave a neighbourhood
- A user can view there profile page
- A user can edit there profile page


## Installation / Setup instruction
The application requires the following installations to operate:
- pip
- gunicorn
- django
- postgresql

## Technologies Used
- python 4.0.3

## Project Setup Instructions
1) git clone the repository 
```
https://github.com/Juliet-Ol/our-neighbourhood
```
2. cd into DjangoAwwards-Clone
```
cd our-neighbourhood-Clone
```
3. create a virtual env
```
python -m venv env
```
4. activate env
```
source virtual/bin/activate
```
5. Open CMD & Install Dependancies
```
pip install -r requirements.txt
```
6. Make Migrations
```
python manage.py makemigrations
```
7. Migrate DB
```
python manage.py migrate
```
8. Run Application
```
python manage.py runserver
```

## Known Bugs
- There are no known bugs currently but pull requests are allowed incase you find a bug

## Contact Information
If you have any question or contributions, please find me on [LinkedIn]www.linkedin.com/in/juliet-oluoch-262018

© 2022 Juliet Oluoch

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)