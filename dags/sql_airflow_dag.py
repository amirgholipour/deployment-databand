# Simple DAG for the Databand hands-on workshop

# These are mandatory imports
from __future__ import annotations
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime,timedelta
from random import random


# An auxiliary function to decide either drop a table or delete its contents
def delete_or_drop():
    if random() < 0.5:
        return("SQL_delete_records")
    else:
        return("SQL_drop_table")

# The main body of the DAG with all its tasks. 
# Notice the argument postgres_conn_id: it must match a connection name in Airflow
with DAG(
    dag_id="SQL_Airflow_DAG",
    start_date=datetime(2023, 1, 1),
    schedule_interval=timedelta(minutes=7),
    catchup=False,
    default_args = {'owner': 'Angel'},
    tags=[
        "project: SQL Airflow pipelines "
    ],
) as dag:
    SQL_create_table = PostgresOperator (
        task_id="SQL_create_table",
        postgres_conn_id="postgres_motogp",
        sql="sql/motogp_create_table.sql"
    )
    SQL_load_table = BashOperator (
        task_id="SQL_load_table",
        bash_command="python3 /opt/airflow/dags/sql/motogp_load_table.py"
    )
    SQL_select_table = PostgresOperator (
        task_id="SQL_select_table",
        postgres_conn_id="postgres_motogp",
        sql="sql/motogp_select_table.sql"
    )
    Branch_Drop_Delete = BranchPythonOperator(
        task_id="Branch_Drop_Delete",
        python_callable=delete_or_drop
    )
    SQL_delete_records = PostgresOperator (
        task_id="SQL_delete_records",
        postgres_conn_id="postgres_motogp",
        sql="sql/motogp_delete_table.sql"
    ) 
    SQL_drop_table = PostgresOperator (
        task_id="SQL_drop_table",
        postgres_conn_id="postgres_motogp",
        sql="sql/motogp_drop_table.sql"
    )

# These are the DAG dependencies
SQL_create_table >> SQL_load_table >> SQL_select_table >> Branch_Drop_Delete
Branch_Drop_Delete >> SQL_delete_records
Branch_Drop_Delete >> SQL_drop_table


