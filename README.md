# Cloud storage service file filtering

This repository provide a service with REST Endpoint to list and filter files on a storage
Once deployed the REST API is reachable at http://example.com/filter and it accepts a post request with a JSON body describing the required filter operations.
The response would be a list of files name matching the request

Example:
```shell

```



- [Quick](#quick)
- [Setup](#setup)
- [Developmet](#development)
- [Building Container](#deployment-docker)

## Setup

### Virtual Environment: Install Miniconda3 
https://docs.anaconda.com/free/miniconda/miniconda-install/

### Create Virtual Environment
```shell
conda create -n NeuralConcept python=3.11
conda activate NeuralConcept
```

### Dependencies

### Install Dependencies 
Inside your virtual environment
```shell
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Updates Dependencies
```shell
pur -r requirements-dev.txt
pur -r requirements.txt
```
### Remove all the dependencies
```shell
pip freeze | cut -d "@" -f1 | xargs pip uninstall -y
```
## Development

A set of scripts are provided to easy the development.
They are in the project directory "./scripts".

You need to run them from the Project main directory, they expect so

```shell
./scripts/static_check.sh
./scripts/tests.sh
./scripts/coverage.sh
./scripts/formatter.sh
./scripts/create_shared_example_directory.sh
./scripts/create_file.sh
```

## Deployment Docker

### Build docker image and Run it following the logs

```shell
docker build -t neuralconcept-cfs .
docker run -it --name nc-cfs -p 8000:8080 neuralconcept-cfs:latest 
```

### Inspect the container
```shell
docker run -it --name nc-cfs neuralconcept-cfs /bin/sh
```

### Stop and Remove the container 
```shell
docker rm -f nc-cfs
```

### Purge the image

```shell
docker rmi -f neuralconcept-cfs:latest
```


### Run the platform

Open your browser on http://localhost:8000/docs
```shell

```

