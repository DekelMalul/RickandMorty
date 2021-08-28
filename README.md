# Rick and Morty

Under `application` folder there is script for the first challenge.

## Dockerfile challange

Get into `dockerfile-challenge` and run the next commands

```console
docker build . -t rickandmorty:0.0.1
docker run --rm -p 5000:5000 rickandmorty:0.0.1
```

After that you can enter the browser at `localhost:5000/healthcheck` to check the health of the application.

Also you can enter the browser at `localhost:5000/characters_info` to get characters info as asked. 

## Yaml challange

Inorder to check the challange ingress controller need to be deloyed on the cluster. 

After that you can apply all the reources and as follow:

```console
kubectl apply -f yamls
```

The ingress dns recorde is `rickandmorty.dekel.com`

## Helm challange

Continue to the helm directory where you will see farther explanation on the helm chart.

