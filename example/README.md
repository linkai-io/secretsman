# Example
This example runs the service in an optional docker container (most likely fargate/ECS). 
Task definitions must pass in APP_ENV and APP_REGION to be able to configure the SSM client.

# Running

## Locally
Make sure you have gunicorn/falcon:
- pip install falcon gunicorn

## Locally inside docker
From the root project:
- make buildexample
- docker run --name secretsman -p 8000:8000 service:latest

Note this will just use the default APP_ENV local environment.

