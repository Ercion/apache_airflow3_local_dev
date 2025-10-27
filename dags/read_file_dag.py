from airflow.sdk import dag, task
from airflow.providers.standard.operators.bash import BashOperator

from datetime import datetime
import random

@dag(dag_id="read_file_dag" ,schedule='@daily', start_date=datetime(2025,10,13), catchup=False, tags=['ercan'])
def read_file_dag():
    @task
    def read_file(folder:str,file_path: str):
        return folder + file_path
    
    def extract_file_paths() -> list[str]:
        # In a real scenario, this could read from a config or database
        return [f"file{i}.txt" for i in range(random.randint(2, 5))]
    
    files = extract_file_paths()
    read_file.partial(folder="/path/to/").expand(file_path=files)

    
    
    def ls_file(files: list) -> list[str]:
        return ["ls -la {file}" for file in files]

    BashOperator.partial(task_id="final_task").expand(bash_command=ls_file(files))

read_file_dag()
