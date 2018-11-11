# API-exercise documentation

This is a Rest API using Python and Flask. An Api request to the end point will query the mysql database and display the result as a json object. The application and database are tested, built and deployed using docker and minikube.

## Tools used for testing

1. Python 3.6
2. pip 18.1
3. docker 17.12.1-ce
4. minikube v0.30.0

## Steps to test

1. Setup local environment
2. Clone this repo
3. Run the install bash script within the repo(./install.sh)

## Healthcheck

The application healthcheck is available using the url http://$(minikube ip):31318/healthcheck
* Healtcheck can be used with monitoring solutions to send an alert if there is a failure

## Jobs

There are two jobs as part of the solution. 

1. migrations - This job performs the migration of data from the csv file to the mysql database. There is no actio to be performed. The migration happens as part of the initial setup
2. integrationtest - This job performs a test using tavern and tests couple of GET requests for return code 200

## Use cases

1. All females who survived
* curl -vv "http://$(minikube ip):31318/?sex=female&survived=1"

2. All passengers above 30 who survived
* curl -vv "http://$(minikube ip):31318/?minage=30&survived=1"

3. All passenger information
* curl -vv "http://$(minikube ip):31318/"

## Secrets

The database credentials are provided as a secret