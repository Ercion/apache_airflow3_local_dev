from airflow.sdk import dag, task
from datetime import datetime
from airflow.providers.http.operators.http import HttpOperator

@dag(
    dag_id="sharing_data_between_decorator_and_classicoperator",
    start_date=datetime(2025, 11, 1),
    schedule='@daily',
    catchup=False,
    tags=['ercan'],
)
def sharing_data_between_decorator_and_classicoperator():
    
    get_api_result = HttpOperator(
        task_id="get_api_result",
        method="GET",
        http_conn_id="api",
        endpoint="/entries",
        do_xcom_push=True,
    )

    @task
    def process_api_data(api_response):
        import json
        data = json.loads(api_response)
        return f"Number of entries received: {len(data.get('entries', []))}"
    
    # output is the way to access data pushed to XCom by Classic Operators!
    api_response = get_api_result.output
    process_api_data(api_response)