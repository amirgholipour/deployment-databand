# File: sql_airflow_dag.py
# Simple DAG for the Databand hands-on workshop

# It must be embedded in Airflow to run properly, not using the command line
# Copy this file in the dags directory and Airflow will recognize it as a DAG

# Create a test table, load data from csv, select data, delete data or drop the table
# Featuring:
#   - Airflow tasks
#   - Three Airflow operators (bash / Postgres / branch)
#   - all tasks implemented with the Postgres operator and *.sql files but:
#       - exception 1: load by bash operator invoking a python script (not possible with an *.sql file)
#       - exception 2: decision delete/drop by branch operator
#   - NO DATABAND CODE at all. Metadata collected automatically,

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

# The header of the DAG with all its tasks.
# Notice the argument postgres_conn_id: 
# it must match a connection name in Airflow connection menu
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
    # Create table. Column definition inside the auxiliar *.sql file
    SQL_create_table = PostgresOperator (
        task_id="SQL_create_table",
        postgres_conn_id="postgres_motogp",
        sql="sql/motogp_create_table.sql"
    )
    # Load data from a *.csv file. Note that the Postgres loader must be 
    # invoked by a python script. Otherwise, Airflow raises an error.
    # Airflow will spawn a shell and run the python script as indicated
    SQL_load_table = BashOperator (
        task_id="SQL_load_table",
        bash_command="python3 /opt/airflow/dags/sql/motogp_load_table.py"
    )
    # Select some data that goes to nowhere but Databand will track
    # the details of the operation automatically
    SQL_select_table = PostgresOperator (
        task_id="SQL_select_table",
        postgres_conn_id="postgres_motogp",
        sql="sql/motogp_select_table.sql"
    )
    # Task to decide if we drop the table or delete the contents
    # the decision is made randomly
    Branch_Drop_Delete = BranchPythonOperator(
        task_id="Branch_Drop_Delete",
        python_callable=delete_or_drop
    )
    # Delete from table...
    SQL_delete_records = PostgresOperator (
        task_id="SQL_delete_records",
        postgres_conn_id="postgres_motogp",
        sql="sql/motogp_delete_table.sql"
    ) 
    # ... or drop table
    SQL_drop_table = PostgresOperator (
        task_id="SQL_drop_table",
        postgres_conn_id="postgres_motogp",
        sql="sql/motogp_drop_table.sql"
    )

# These are the task dependencies written with Airflow syntax
SQL_create_table >> SQL_load_table >> SQL_select_table >> Branch_Drop_Delete
Branch_Drop_Delete >> SQL_delete_records
Branch_Drop_Delete >> SQL_drop_table