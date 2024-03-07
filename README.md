# Cloud storage service file filtering


## Docker


### Build docker image and Run it

```shell
docker build -t neuralconcept-cfs .
docker run -d --name nc-cfs -p 8000:8000 neuralconcept-cfs 
docker logs -f nc-cfs 
```

### Inspect the container
```shell
docker run -it --name nc-cfs neuralconcept-cfs /bin/sh
```

### Docker to stop it 
```shell
docker rm -f nc-cfs
```