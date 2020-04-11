docker build -f Dockerfile-redis . -t alivx:enc_redis
docker container run   --rm -d --name enc_redis alivx:enc_redis  top
docker cp enc_redis:/projects/rd_themis/rd_themis.so lib/rd_themis.so
docker stop enc_redis
docker build -f Dockerfile . -t alivx:enc_api