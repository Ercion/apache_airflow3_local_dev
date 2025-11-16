"""
@task
@task.bash
@task_group
@task.virtualenv
@task.branch
@task.external_python
@task.short_circuit
@task.sensor
@task.docker
@task.kubernetes
"""
from airflow.sdk import dag, task
from datetime import datetime

@dag(
    dag_id="taskflow_api_test",
    start_date=datetime(2025, 11, 1),
    schedule='@daily',
    catchup=False,
    tags=['ercan'],
)
def taskflow_api_test():

    @task.sensor(poke_interval=10, timeout=60)
    def wait_for_file(file_path: str):
        import os
        return os.path.exists(file_path)
    
    @task.bash
    def process_file(file_path: str):
        return f"Processing file at {file_path}"
    
    file_path = "/path/to/some/file.txt"
    file_exists = wait_for_file(file_path)
    process_file(file_path).set_upstream(file_exists)

taskflow_api_test()