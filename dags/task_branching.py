from airflow.sdk import dag, task
from datetime import datetime

@dag(
    dag_id="task_branching",
    start_date=datetime(2025, 10, 1),
    schedule='@daily',
    catchup=False
)
def task_branching():

    @task
    def start_task():
        return 7
    
    @task.branch
    def check_condition(value: int) -> bool:
        return 'true_one' if value > 5 else 'false_one'
    
    @task.bash
    def true_one():
        return "echo 'Value is greater than 5'"
    
    @task.bash
    def false_one():
        return "echo 'Value is 5 or less'"
    
    check_condition(start_task()) >> [true_one(), false_one()]

task_branching()