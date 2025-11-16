from airflow.sdk import dag, task,task_group
from datetime import datetime

@dag(
    dag_id="task_group_and_dynamic_task_mapping",
    start_date=datetime(2025, 11, 1),
    schedule='@daily',
    catchup=False,
    tags=['ercan'],
)
def task_group_and_dynamic_task_mapping():

    @task_group(group_id="data_processing_group")
    def data_processing_group():
        @task
        def extract_data(source: str):
            return f"Data extracted from {source}"

        @task
        def transform_data(data: str):
            return data.upper()

        @task
        def load_data(data: str):
            return f"Data loaded: {data}"

        sources = ["source_1", "source_2", "source_3"]
        extracted_data = extract_data.expand(source=sources)
        transformed_data = transform_data.expand(data=extracted_data)
        load_data.expand(data=transformed_data)
