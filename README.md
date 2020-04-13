# API Encryption Service

This project like an Encryption as service somehow, this service provide high performance and secure way to store text-based data using [Themis](https://www.cossacklabs.com/themis/) and [Redis](https://redis.io/).

### Use cases:
1. Share sensitive information for a period.
2. Save sensitive information for a set of time.
3. Vault key management.

### Installation

##### Using Docker
First Build the images
```Bash
docker build -f Dockerfile-redis . -t alivx:enc_redis
docker build -f Dockerfile . -t alivx:enc_api
```
Then run the service using docker-compose.yml
```Bash
docker-compose up ## to run it in background use '-d'
```
output
```Bash
docker-compose up
Starting encryptionservice_redis_1 ... 
Starting encryptionservice_redis_1 ... done
Recreating encryptionservice_api_1 ... 
Recreating encryptionservice_api_1 ... done
Attaching to encryptionservice_redis_1, encryptionservice_api_1
```

### Todo
1. Add nginx with SSL setup to get encryption in transit.
2. add a web interface to call the API.
3. add the ability to upload files.

### Usages
After startup the docker-compose, two services will be up and running.
1. Encryption API server on port 1992.
2. Redis server on port 6379.

> Setting data:

calling the API using `curl`
Info:
* value: anything you need to be encrypted.
* Password: password key
* TTL: time to live (set time in second)

```Bash
curl -X PUT "http://localhost:1992/set/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"value\":\"http://localhost:8000/docs#/default/read_items_seturl__put\",\"ttl\":500,\"password\":\"123\"}"
```
returned value `{"_id":"DJGNOGVV2eab7054"}`

> Getting Data
```Bash
curl -X GET "http://localhost:1992/get/?_id=DJGNOGVV2eab7054&password=123" -H "accept: application/json"
```

returned data:`{"value":"http://localhost:8000/docs#/default/read_items_seturl__put"}`

#### How it works:

After putting some text/something need to be encrypted. the API sends the data into redis using `Themis module for Redis database`

Redis Content:
```Bash
127.0.0.1:6379> keys '*'
1) "WP52978Nc290f53d"
2) "GPMNRNNQ9d396717"
3) "7NW8388G60755d45"
4) "EWGN9NVR1b402e2a"
5) "Q6YGLPGNc648e448"
127.0.0.1:6379> get Q6YGLPGNc648e448
"\x00\x01\x01@\x0c\x00\x00\x00\x10\x00\x00\x00:\x00\x00\x00f\xedRv\xc2\x17\xeb#\xe7h\n\xf2\xf2;\x97\xc87}\xb7_\xbe\xad\xc8\x8eR7\xde\xa9$\xf6\x12\xc9\x1d\xade\xf2\xbeq\xd1y]\x9f\xa5\xf4`\x8d\x17\xf1w\x13\x80\xf3\x8a\xc9\xe9\xdb\xb6\xc7\xbbu7\x1eFc\xe6,\xd1t\x85d \x85m\x9c\x8a\xca\xcd\x1e\xb3\x80zXw\xeb0\n"
127.0.0.1:6379>
```