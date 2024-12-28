from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
}

with DAG(
    dag_id="salvin_env",
    default_args=default_args,
    description="Test Celery concurrency with DockerOperator",
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    task1 = DockerOperator(
        task_id='task1',
        image='salvin_image:latest',
        api_version='auto',
        mount_tmp_dir = False,
        auto_remove=True,
        command="python scripta.py",
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
    )
