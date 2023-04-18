FROM flink:1.10.0-scala_2.11

RUN set -ex; \
  apt-get update; \
  apt-get -y install python3; \
  apt-get -y install python3-pip; \
  apt-get -y install python3-dev; \
  ln -s /usr/bin/python3 /usr/bin/python; \
  ln -s /usr/bin/pip3 /usr/bin/pip


COPY usage_job.py /app
COPY data_preparator_kafka.py /app

RUN set -ex; \
  apt-get update; \
  python -m pip install --upgrade pip; \
  pip install apache-flink; \
  pip install kafka-python; \
  pip install faker; \
  pip install cassandra-driver

ARG FLINK_VERSION=1.10.0

RUN wget -P /opt/flink/lib/ https://repo.maven.apache.org/maven2/org/apache/flink/flink-json/1.10.0/flink-json-1.10.0.jar; \
    wget -P /opt/flink/lib/ https://repo.maven.apache.org/maven2/org/apache/flink/flink-csv/1.10.0/flink-csv-1.10.0.jar; \
#    wget -p /opt/flink/lib/ https://repo.maven.apache.org/maven2/org/apache/flink/flink-connector-kafka_2.11/0.10.2/flink-connector-kafka_2.11-0.10.2.jar; \
#    wget -P /opt/flink/lib/ https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka_2.11/1.11.2/flink-sql-connector-kafka_2.11-1.11.2.jar; \
    wget -P /opt/flink/lib/ https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka_2.11/1.10.0/flink-sql-connector-kafka_2.11-1.10.0.jar; \
    wget -P /opt/flink/lib/ https://repo.maven.apache.org/maven2/org/apache/flink/flink-connector-cassandra_2.11/1.10.0/flink-connector-cassandra_2.11-1.10.0.jar; \
#    wget -P /opt/flink/lib/ https://repo.maven.apache.org/maven2/org/apache/flink/flink-connector-nifi_2.11/1.9.2/flink-connector-nifi_2.11-1.9.2.jar; \
#    wget -P /opt/flink/lib/ https://repo.maven.apache.org/maven2/org/apache/flink/flink-connector-kafka-base_2.11/1.10.0/flink-connector-kafka-base_2.11-1.10.0.jar; \
#    wget -P /opt/flink/lib/ https://repo1.maven.org/maven2/org/apache/flink/flink-connector-kafka_2.12/1.13.0/flink-connector-kafka_2.11-1.13.0.jar; \
#    wget -P /opt/flink/lib/ https://repo1.maven.org/maven2/org/apache/flink/flink-connector-kafka_2.11/1.10.0/flink-connector-kafka_2.11-1.10.0.jar; \

# Create data folders
    mkdir -p /opt/data \
   # echo "taskmanager.memory.jvm-metaspace.size: 512m" >> /opt/flink/conf/flink-conf.yaml \
   # echo "rest.port: 8088" >> /opt/flink/conf/flink-conf.yaml;

WORKDIR /opt/flink/
