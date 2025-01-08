docker pull docker.elastic.co/elasticsearch/elasticsearch:8.15.3

docker network create elastic

docker run --name pbd-es01 --net elastic -p 9200:9200 -itd -m 2GB docker.elastic.co/elasticsearch/elasticsearch:8.15.3

docker run -d --name kibana_pbdi --net elastic -p 5601:5601 kibana:8.10.2