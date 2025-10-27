from airflow.sdk import dag, task

@dag(dag_id="my_dag" ,schedule='@daily', start_date=None, catchup=False, tags=['ercan'])
def my_dag():
    @task
    def training_model(accuracy: int):
        return accuracy
    
    @task.branch
    def choose_model(accurasies: list[int]):
        if max(accurasies) > 2:
            return "accurate"
        return "inaccurate"
    
    @task.bash
    def accurate():
        return "echo 'accurate model selected'"
    
    @task.bash
    def inaccurate():
        return "echo 'inaccurate model selected'"
    
    @task.bash(trigger_rule="none_failed_min_one_success")
    def end():
        return "echo 'end of the dag'"


    accurasies = training_model.expand(accuracy=[1, 2, 3])
    choose_model(accurasies) >> [accurate(), inaccurate()] >> end()

my_dag()