import os
from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount

default_args = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
        "11_docker",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(5),
) as dag:
    download = DockerOperator(
        image="airflow-download",
        # network_mode="bridge",
        task_id="docker-airflow-download",
        command=["/data/{{ ds }}/raw/"],
        do_xcom_push=False,
        mount_tmp_dir=False,
        # !!! HOST folder(NOT IN CONTAINER) replace with yours !!!
        mounts=[Mount(source="/home/peter/Coding/julia/tekhno/ml/airflow-examples/data/", target="/data", type='bind')]
    )

    preprocess = DockerOperator(
        image="airflow-preprocess",
        task_id="docker-airflow-preprocess",
        command=["/data/{{ ds }}/raw/", "/data/{{ ds }}/processed/"],
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source="/home/peter/Coding/julia/tekhno/ml/airflow-examples/data/", target="/data", type='bind')]
    )

    predict = DockerOperator(
        image="airflow-predict",
        task_id="docker-airflow-predict",
        command=["/data/{{ ds }}/processed/", "/data/{{ ds }}/predicted/"],
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source="/home/peter/Coding/julia/tekhno/ml/airflow-examples/data/", target="/data", type='bind')]
    )

    download >> preprocess >> predict
