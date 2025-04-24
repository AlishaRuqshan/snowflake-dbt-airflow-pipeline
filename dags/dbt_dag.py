from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'alisha',
    'start_date': datetime(2023, 1, 1),
    'retries': 0
}

with DAG(
    dag_id='run_dbt_pipeline',
    default_args=default_args,
    schedule=None,  # updated to `schedule` for newer Airflow versions
    catchup=False,
    tags=['dbt'],
) as dag:

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='cd /usr/local/airflow/dags/data_pipeline && dbt run --profiles-dir /usr/local/airflow/dags/.dbt'
    )

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='cd /usr/local/airflow/dags/data_pipeline && dbt test --profiles-dir /usr/local/airflow/dags/.dbt'
    )

    dbt_run >> dbt_test