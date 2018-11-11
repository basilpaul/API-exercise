#!/usr/bin/env bash
echo
eval $(minikube docker-env)
echo "Setting up mysql"
kubectl apply -f secrets.yaml
kubectl apply -f mysql_pvc.yaml
kubectl apply -f mysql_service.yaml
kubectl apply -f mysql_deployment.yaml
echo "Building docker image of app.."
echo
docker build -t passenger:1.0 .
echo "Setting up app.."
kubectl apply -f passenger_deployment.yaml
kubectl apply -f passenger_service.yaml
echo "Run db migration job"
kubectl apply -f db_migration.yaml
echo "Run integration tests job"
kubectl apply -f test_restapi.yaml
echo "Deployment successfull. The end point is http://$(minikube ip):31318/"
echo "Please wait 5 seconds for the database setup.."