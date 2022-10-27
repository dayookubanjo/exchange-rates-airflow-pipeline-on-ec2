from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from twitter_etl import run_exchange_rate_etl

default_args = {
    'owner': 'dayookubanjo',
    'depends_on_past': False,
    'email': ['dayookubanjo@yahoo.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='twitter_dag',
    default_args=default_args,
    description='Task to pull NGN exchange rates @naira_rates handle on twitter and load it into s3.',
    start_date=datetime(2022, 10, 26),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id = 'twitter_exchange_rates_etl',
        python_callable = run_exchange_rate_etl
    )

    task1