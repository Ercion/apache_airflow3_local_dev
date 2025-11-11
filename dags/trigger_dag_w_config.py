from airflow.sdk import dag, task
from datetime import datetime

@dag(
    dag_id="templating_dag_taskflow",
    start_date=datetime(2022, 1, 1),
    schedule=None,
    catchup=False,
    render_template_as_native_obj=True,
    tags=['ercan'],
)
def templating_dag(dag_run=None):
    
    @task
    def sum_numbers(numbers):
        return sum(numbers)
   
    sum_numbers(numbers="{{ dag_run.conf['numbers'] }}")

templating_dag()