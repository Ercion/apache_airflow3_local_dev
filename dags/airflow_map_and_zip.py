from airflow.decorators import dag, task
from datetime import datetime

@dag(
    dag_id="airflow_map_and_zip",
    start_date=datetime(2025, 11, 1),
    schedule='@daily',
    catchup=False,
    tags=['ercan'],
)
def airflow_map_and_zip():

    @task
    def generate_numbers():
        return [1, 2, 3, 4, 5]
    
    @task
    def square_number(number: int):
        print(f"Squaring number: {number}")
        return number * number
    
    numbers = generate_numbers()
    squared_numbers = square_number.map(numbers)  
    return squared_numbers

airflow_map_and_zip()