# This DAG is used by Databand to monitor your Airflow installation.
from airflow_monitor.monitor_as_dag import get_monitor_dag
dag = get_monitor_dag()

