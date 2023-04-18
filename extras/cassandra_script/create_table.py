from cassandra.cluster import Cluster
cluster = Cluster(['cassandra'], port=9042, control_connection_timeout=None)
session = cluster.connect()

session.execute("CREATE KEYSPACE nasa WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3}")

session.execute("USE nasa")

session.execute("CREATE TABLE engine_test(engine text, recorded_date date, RUL int, time_in_cycles float, setting_1 float, setting_2 float, T2 float, T24 float, T30 float, T50 float, Nf float, Nc float, epr float, Ps30 float, NRf float, NRc float, BPR float, farB float, htBleed float, Nf_dmd float, W31 float, W32 float, PRIMARY KEY (engine, recorded_date))")
