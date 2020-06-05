# Random Data Maker
[![RandomDataMaker](https://circleci.com/gh/RandomDataMaker/rdm-services.svg?style=shield)](https://circleci.com/gh/RandomDataMaker/rdm-services)
## Overview
Random Data Maker is a REST webservice for generation random data sets from a defined model, including personal data and medical metrics data for machine learning, tests, mocks etc..

## Requirements 
##### Software: 
* Python 3.7.5
* MySQL 8.0 with Docker support provided
##### Frameworks & libraries:
See `requirements.txt`
* Django 2.2.7
* django-cors-headers 3.1.1
* djangorestframework 3.10.3
* enum34 1.1.6
* jsonfield 2.0.2
* mysqlclient 1.4.5
* sqlparse 0.3.0

## Run  
### Docker
Create external docker network named `webproxy` 
* `docker network create webproxy`

Run container stack
* `docker-compose up`
### Manual
To run this app you will need an external MySQL database, either your own, or one created using dockerfile from inside of the project
* `docker-compose -f docker-compose-db-only.yml`. 

Install virtual environments 
* `python3 -m venv venv`
 * `. venv/bin/activate`
 * `pip install -r requirements.txt`

Make migrations
* `python manage.py makemigrations`
* `python manage.py migrate --settings=peselgen.settings-dev`

And run the app: 
* `python manage.py runserver --settings=peselgen.settings-dev`

## Endpoints  
`/person` - method: GET - returns generated persons 
`/metrics` - method: GET - returns generated patient metrics  
`/attributes` - method: GET - returns attributes records  
`/geolocation` - method: GET -returns generated geojson 
`/generate/<number>` - method: POST - generates in specified number: persons, metrics and attributes
`/generate/flush` - method: PUT - deletes all records from both database tables  
`/generate/flush/<table>` - method: PUT - deletes all records from specified table, could be 'person', 'metrics' or 'attributes' 
`/person/<number>` - method:POST - generates persons in specified number
`/metrics/<number>` - method:POST - generates patient metrics in specified number
`/attributes/<number>` - method:POST - generates attributes from model in specified number

  
## Data model  
### Person model  
Generated person entities contain: 
* `id`: int, private key
* `first_name`: varchar(30)
* `last_name`: varchar(30)
* `pesel`: varchar(11) - unique person identification number based on birth date and sex 
* `email`: varchar(64)
* `phone`: varchar(12)
* `password`: varchar(16)
* `sex`: varchar(1) - '1' - male; '2' - female 
* `birth_date`: datetime - generated basing on polish General Statistics Departments' informations about births count 

### Metrics model  
Patient metrics entities contain: 
* `id`: int, private key
* `patient_id`: varchar, foreign key references `id` from person
* `doctor_id`: varchar
* `created`: datetime 
* `attributes_id`: varchar, foreign key references `id` from attributes
* `notes`: varchar(1024) 

### Attributes model 
Dynamic data model is defined in JSON format. It is used to specify what kind of data app should generate. It is generated in a form of the list of objects with predefined attributes:  
* `key` - string value representing object name  
* `count`: optional - integer value representing how many values should be generated, default = 1  
* Generating values from array  
  - `array` - array of values from whitch data will be generated  
  - `weights`: optional - array of numbers showing the probability of occurance of element from attribute array, must be the same length as `array`  
* Generating numbers between two values, type is being resolved dynamically (1 - discrete value, 1.0 - continuous value):  
  - `minimum` - smallest value that can be generated  
  - `maximum` - biggest value that can be generated  
  - `floating_points`: optional - number of digits after decimal point  
* Generating datetime between two values:  
  - `min_date` - smallest datetime value that can be generated  
  - `max_date` - biggest datetime value that can be generated  
  - `date_format`: optional - default format is: '%m/%d/%Y %I:%M %p'
  ### Geolocation model
* `person_id`: varchar, foreign key references `id` from person
* `geojson`: json, includes location based on geojson model

## How it works?
Random Data Maker is a rest api app and has defined endpoints to communicate with it. It has three kinds of endpoints: generating number of random records (POST), getting them from database in the form of JSON (GET) and flushing tables (PUT). When post method is used it generates random data e.g personal data, metrics data using apps own random data generator and saves it in database. This random data generator takes JSON file with defined data model and uses it to generate new data. When data is in a database it can be accessed with get methods. Project was originally made as support for medical machine learning system OCULUS Project

## About us 
We're Computer Science students at Poznan University of Technology. We like programming and had a lot of fun creating this project.  
[Artur Bałczyński](https://github.com/arturbalcz)  
[Mateusz Ostrowski](https://github.com/matostr98)  
[Adam Przywuski](https://github.com/adamprzywuski)  
[Maciej Stosik](https://github.com/SaronTetra)  
