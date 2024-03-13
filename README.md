# Cloud storage service file filtering

This repository provide a service with REST Endpoint to list and filter files on a storage
Once deployed the REST API is reachable at http://example.com/filter and it accepts a post request with a JSON body describing the required filter operations.
The response would be a list of files name matching the request.

Supported filters are: 
- Size
  - HigherThanSize (size: int)
  - LowerThanSize (size: int)
- Extension 
  - MatchExtension (extension: str)
- Logical Operations
  - AndOperation (operands: List)
  - OrOperation (operands: List)


- [Quick Run](#quick-run)
- [Development: Setup](#development-setup)
- [Developmet: Source Code pointers](#development-source-code)
- [Building Container](#deployment-docker)

## Quick Run
First Start the docker container: 

```shell
docker build -t neuralconcept-cfs .
docker run -it --name nc-cfs -p 8000:8000 neuralconcept-cfs:latest 
```

Example Request:
```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/filter' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "type": "OrOperation",
  "operands": [
    {
      "type": "AndOperation",
      "operands": [
        {
          "type": "HigherThanSize",
          "size": 512
        },
        {
          "type": "MatchExtension",
          "extension": "txt"
        }
      ]
    },
    {
      "type": "AndOperation",
      "operands": [
        {
          "type": "LowerThanSize",
          "size": 1024
        },
        {
          "type": "MatchExtension",
          "extension": "mkv"
        }
      ]
    }
  ]
}'
```

Example Response:
```shell
["video_512.mkv","text_1024.txt","text_2048.txt"]%
```
You can also connect to the OPENAPI web interface at http://localhost:8000/docs and test the service from there.

## Development Setup

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
## Development Source Code

The service is developed using FastAPI and Pydantic.
In the current state it is a simple service with a single endpoint.
( there's also an hello world endpoint)

The main source code is in the directory "./app" with main.py as entry point and Application.py 
as responsible to pull together the dependencies and register the end points: filter, hello world

The application make use of dependency injection to pull the dependencies, the python library Injector provides the DI framework.

Filters are implemented using Polymorphism and they are created directly from the FastAPI's request by Pydantic.
Each filter subclasses FilterBase and defines it's own fields and they also implement a method to apply the filter to a single file.

```plantuml
@startuml
abstract FilterBase {
    type: str
    apply(file: FileSystemItem) -> bool
}
class HigherThanSizeFilter {
    apply(file: FileSystemItem) -> bool
}
class AndOperation {
    operands: List[FilterBase]
    apply(file: FileSystemItem) -> bool
}
HigherThanSizeFilter --|> FilterBase
AndOperation --|> FilterBase
AndOperation -


@enduml

```






A set of scripts are provided to easy the development.
They are in the project directory "./scripts".

You need to run them from the Project main directory, they expect so.

### Scripts
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
docker run -it --name nc-cfs -p 8000:8000 neuralconcept-cfs:latest 
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

