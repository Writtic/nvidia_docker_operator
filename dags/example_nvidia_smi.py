from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.nvidia_docker_operator import NvidiaDockerOperator
from datetime import datetime, timedelta
import os

START = datetime.combine(datetime.today() - timedelta(days=2),
                         datetime.min.time()) + timedelta(hours=10)
DAG_NAME = 'example_smi'

# Define the DAG object
default_args = {
    'pool'
    'depends_on_past': False,
    'start_date': START,
    'retries': 1,
    'retry_delay': timedelta(minutes=20),
}

dag = DAG(DAG_NAME, default_args=default_args, schedule_interval=timedelta(20))

trainModel = NvidiaDockerOperator(
    command='nvidia-smi',
    image='nvidia/cuda',
    network_mode='bridge',
    task_id='nvidia_docker_op_tester',
    # gpu_devices='2',
    dag=dag
)
