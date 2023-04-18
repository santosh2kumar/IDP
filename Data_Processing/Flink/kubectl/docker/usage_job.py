import os
from pyflink.datastream import StreamExecutionEnvironment, TimeCharacteristic
from pyflink.table import StreamTableEnvironment, CsvTableSink, DataTypes, EnvironmentSettings
from pyflink.table.descriptors import Schema, Rowtime, Json, Kafka, Elasticsearch
from pyflink.table.window import Tumble
def register_transactions_source(st_env):
    st_env.connect(Kafka()
                   .version("universal")
                   .topic("transactions_data_new")
                   .start_from_latest()
                   .property("zookeeper.connect", "zk-0.zk-hs.default.svc.cluster.local:2181,zk-1.zk-hs.default.svc.cluster.local:2181,zk-2.zk-hs.default.svc.cluster.local:2181")
                   .property("bootstrap.servers", "kafka-svc:9093")) \
        .with_format(Json()
        .fail_on_missing_field(True)
        .schema(DataTypes.ROW([
        DataTypes.FIELD("customer", DataTypes.STRING()),
        DataTypes.FIELD("transaction_type", DataTypes.STRING()),
        DataTypes.FIELD("online_payment_amount", DataTypes.DOUBLE()),
        DataTypes.FIELD("in_store_payment_amount", DataTypes.DOUBLE()),
        DataTypes.FIELD("transaction_datetime", DataTypes.TIMESTAMP())]))) \
        .with_schema(Schema()
        .field("customer", DataTypes.STRING())
        .field("transaction_type", DataTypes.STRING())
        .field("online_payment_amount", DataTypes.DOUBLE())
        .field("in_store_payment_amount", DataTypes.DOUBLE())
        .field("rowtime", DataTypes.TIMESTAMP())
        .rowtime(
        Rowtime()
            .timestamps_from_field("transaction_datetime")
            .watermarks_periodic_bounded(60000))) \
        .in_append_mode() \
        .register_table_source("source")
def register_transactions_sink_into_csv(st_env):
    result_file = "/datalake/data_lake1/output/output_file_new.csv"
    if os.path.exists(result_file):
        os.remove(result_file)
    st_env.register_table_sink("sink_into_csv",
                               CsvTableSink(["customer",
                                             "count_transactions",
                                             "total_online_payment_amount",
                                             "total_in_store_payment_amount",
                                             "last_transaction_time"],
                                            [DataTypes.STRING(),
                                             DataTypes.STRING(),
                                             DataTypes.DOUBLE(),
                                             DataTypes.DOUBLE(),
                                             DataTypes.TIMESTAMP()],
                                            result_file))
def transactions_job():
    s_env = StreamExecutionEnvironment.get_execution_environment()
    s_env.set_parallelism(1)
    s_env.set_stream_time_characteristic(TimeCharacteristic.EventTime)
    st_env = StreamTableEnvironment \
        .create(s_env, environment_settings=EnvironmentSettings
                .new_instance()
                .in_streaming_mode()
                .use_blink_planner().build())

    register_transactions_source(st_env)
    register_transactions_sink_into_csv(st_env)

    st_env.from_path("source").insert_into("sink_into_csv")

    st_env.execute("app")


if __name__ == '__main__':
    transactions_job()
