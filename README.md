Algorand Verifier
An on chain verification application for algorand contracts. Demo at http://ec2-3-142-48-148.us-east-2.compute.amazonaws.com:8000/

## Getting Started

### Prerequisites
The following tools are required to run the application.
* docker
```sh
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
```
* docker-compoose
```sh
mkdir -p ~/.docker/cli-plugins/
curl -SL https://github.com/docker/compose/releases/download/v2.3.3/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose

chmod +x ~/.docker/cli-plugins/docker-compose
```
* python

### Installation
1. Create virutal environment
```sh
python3 -m venv venv
```
2. Install dependencies
```sh
python3 -m pip install -r requirements.txt
```
3. Migrate database
```sh
python3 src/verifier/manage.py migrate
```
4. Run application
```sh
python3 src/verifier/manage.py runserver
```
