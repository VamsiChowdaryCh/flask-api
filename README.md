# flask-api
Restful api service using python and flask
A simple restful api service named "flask-api". Alpine linux docker is used.

Endpoints are developed in the api.py with the given logics.

Install the requirements. It is done within the Dockerfile

Build the docker image based on the Dockerfile.
using command : docker build . -t flask-api:latest

To run the docker container
Command : sudo docker run -d -p 5000:5000 flask-api

Create the deployment.yaml. Please find it in the repo.

Some kubernetes requirements:
-> Kubernetes CLI Installed
-> Minikube Installed

Deploy the application to the Kubernetes engine.
command : kubectl apply -f deployment.yaml

To Visualize the deployments:
command : minikube dashboard

To Access the application:
command : minikube start service: flask-api
