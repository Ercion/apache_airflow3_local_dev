from airflow.sdk import dag, task
from datetime import datetime   
#from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.weekday import BranchDayOfWeekOperator

@dag(
    dag_id="specialized_operators",
    start_date=datetime(2025, 11, 1),
    schedule='@daily',
    catchup=False,
    tags=['ercan'],
)
def specialized_operators():

#BranchSQLOperator
#BranchDayOfWeekOperator
#BranchDateTimeOperator
#@task.branch
#task.short_circuit
    
    day_name = datetime.now().strftime("%A")

    BranchDayOfWeekOperator(
        task_id="branch_day_of_week",
        follow_task_ids_if_true=["monday_task"],
        follow_task_ids_if_false=["other_day_task"],
        week_day=day_name,  # 0 = Monday, 6 = Sunday
    )

    @task
    def monday_task():
        return "It's Monday! Time to start the week strong." 
    
    @task
    def other_day_task():
        return "It's not Monday. Keep going!"
    
    monday_task() >> other_day_task()

specialized_operators()

