from airflow.sdk import dag, task
from datetime import datetime

# Define the DAG using the TaskFlow API
@dag(
    dag_id='taskflow_backfill_dag',
    start_date=datetime(2025, 10, 1),
    schedule='@daily',
    catchup=False,
    tags=['ercan'],
    default_args={
        'owner': 'airflow',
        'retries': 1,
    },
)
def taskflow_backfill_dag():

    # Define a task using the TaskFlow API
    @task()
    def print_execution_date(execution_date: str):
        print(f"Task executed for date: {execution_date}")
        
    # Call the task, passing `{{ ds }}` as the execution date
    print_execution_date('{{ ds }}')

taskflow_backfill_dag()
