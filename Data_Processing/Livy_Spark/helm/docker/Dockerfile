ARG SPARK_BASE=sasnouskikh/livy-spark:0.8.0-incubating-spark_3.0.1_2.12-hadoop_3.2.0_cloud
#ARG SPARK_BASE=registry.gitlab.com/abhzt/compute_exp:k8Spark03v1

FROM $SPARK_BASE

LABEL maintainer="Abhijit Singha <abhzt712@gmail.com>"

ENV BASE_IMAGE	$SPARK_BASE#$BASE_IMAGE

RUN cp $LIVY_CONF_DIR/log4j.properties.template $LIVY_CONF_DIR/log4j.properties && \
    mkdir -p $LIVY_HOME/work-dir && \
    mkdir /var/log/livy && \
    ln -s /var/log/livy $LIVY_HOME/logs
RUN mkdir /data_lake
RUN apt-get update
RUN apt-get install nfs-common -y
RUN mount -t nfs -o vers=3 10.218.47.21:/mapr/my.cluster.com /data_lake
COPY conf/* $LIVY_CONF_DIR/
COPY entrypoint.sh /opt/
COPY Dockerfile /my_docker/

#  8998 - Livy Server port
# 10000 - Livy RPC Server for Jupyter integration
EXPOSE 8998 10000

WORKDIR $LIVY_HOME/work-dir

ENTRYPOINT [ "/opt/entrypoint.sh" ]
