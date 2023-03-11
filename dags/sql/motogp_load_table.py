import  psycopg2

# This code will not be considered as a DAG by Airflow because it is inside a function

def load_data():

    sql = "copy motogp from STDIN delimiter ';' csv  header"

    conn = psycopg2.connect("dbname='postgres' user='postgres' host='postgresql.postgres.svc.cluster.local' password='postgres'")
    cur = conn.cursor()

    with open("/opt/airflow/dags/sql/motogp.csv", "r") as file:
        cur.copy_expert(sql, file)
    cur.close()

load_data()
