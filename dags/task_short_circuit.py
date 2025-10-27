from airflow.sdk import dag, task
from datetime import datetime

@dag(
    dag_id="task_short_circuit",
    start_date=datetime(2025, 10, 1),
    schedule='@daily',
    catchup=False
)
def task_short_circuit():

    @task
    def start_task():
        return 7
    @task.short_circuit
    def check_condition(value: int) -> bool:
        return value > 5
    
    @task.bash
    def task_will_run_if_condition_met():
        return "echo 'Condition met, executing this task.'"
    
    check_condition(start_task()) >> task_will_run_if_condition_met()

task_short_circuit()