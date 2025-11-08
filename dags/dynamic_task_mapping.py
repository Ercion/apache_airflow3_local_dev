from airflow.sdk import dag, task
from datetime import datetime

@dag(
    dag_id="dynamic_task_mapping",
    start_date=datetime(2025, 11, 1),
    schedule='@daily',
    catchup=False,
    tags=['ercan'],
    default_args={
        'owner': 'airflow',
        'retries': 1,
    },
)
def dynamic_task_mapping():

    @task
    def generate_table_names() -> list[str]:
        """Generate a list of table names to process."""
        return ["users", "transactions", "products"]
    
    @task
    def generate_sql(table_name: str, execution_date:str) -> str:
        """Generate a simple SQL query for the given table name."""
        return f"SELECT * FROM {table_name} WHERE date = {execution_date};"
    
    @task
    def execute_query(sql: str) -> int:
        """Simulate executing the SQL query and return number of rows processed."""
        print(f"Executing SQL: {sql}")
        # Simulate row count
        return len(sql)  # Just a dummy value based on SQL length
    
    table_names = generate_table_names()
    sql_queries = generate_sql.partial(execution_date="{{ ds }}").expand(table_name=table_names)
    execute_query.expand(sql=sql_queries)

dynamic_task_mapping()