# E-transport

#### E-transport is the online application to register your trip, we offer a 100% completed control to those who want to use our platform

## Installation

Clone the repository:

```
    git clone --depth 1 https://github.com/MioraRabearivelo/e-transport.git
```

## Usage

To run the project, use the following command:

```
    cd e-transport/
    sudo chown -R $USER:$USER .
```
and

```
    docker build .
```
then

```
    docker-compose up
```

go to the browser and navigate the address

```
    http://0.0.0.0:8000/
```

The next command stop the container docker

```
    docker-compose down
```

## Run test

``` 
    pytest .
```