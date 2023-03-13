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
        return("motogp_delete_table")
    else:
        return("motogp_drop_table")

# The main body of the DAG with all its tasks. 
# Notice the argument postgres_conn_id: it must match a connection name in Airflow
with DAG(
    dag_id="motogp_postgres",
    start_date=datetime(2023, 1, 1),
    schedule_interval=timedelta(minutes=3),
    catchup=False,
) as dag:
    motogp_create_table = PostgresOperator (
        task_id="motogp_create_table",
        postgres_conn_id="postgres_motogp",
        sql="sql/motogp_create_table.sql"
    )
    motogp_load_table = BashOperator (
        task_id="motogp_load_table",
        bash_command="python3 /opt/airflow/dags/sql/motogp_load_table.py"
    )
    motogp_select_table = PostgresOperator (
        task_id="motogp_select_table",
        postgres_conn_id="postgres_motogp",
        sql="sql/motogp_select_table.sql"
    )
    conditional_task = BranchPythonOperator(
        task_id="delete_or_drop",
        python_callable=delete_or_drop
    )
    motogp_delete_table = PostgresOperator (
        task_id="motogp_delete_table",
        postgres_conn_id="postgres_motogp",
        sql="sql/motogp_delete_table.sql"
    ) 
    motogp_drop_table = PostgresOperator (
        task_id="motogp_drop_table",
        postgres_conn_id="postgres_motogp",
        sql="sql/motogp_drop_table.sql"
    )

# These are the DAG dependencies
motogp_create_table >> motogp_load_table >> motogp_select_table >> conditional_task
conditional_task >> motogp_delete_table
conditional_task >> motogp_drop_table


