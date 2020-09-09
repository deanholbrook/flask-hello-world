## About The Project
Rudimentary project to demonstrate automated build, test, 
and deployment of Docker application to AWS.

### Built With
* Flask
* Docker

## Getting Started
TODO: put content here

### Prerequisites
To work with this project, you'll need the following software on your machine:
* Git (source control management tool)
* Docker (tool to package or "containerize" applications)
* Python 3

### Installation
1. Clone the code repository
```sh
git clone https://github.com/deanholbrook/hello-world.git
```
2. Navigate to the new directory
```sh
cd hello-world
```
3. Build the Docker image
```sh
docker build -t hello-world .  # don't forget the dot/period at end of the comand
```
4. Run Docker image on your local machine
```sh
docker run -p 5000:5000 hello-world
```
