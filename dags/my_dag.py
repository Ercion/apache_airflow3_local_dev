from airflow.sdk import dag, task

doc_md_DAG = """
### The Activity DAG

This DAG will help me decide what to do today. It uses the [BoredAPI](https://bored-api.appbrewery.com/random) to do so.

Before I get to do the activity I will have to:

- Clean up the kitchen.
- Check on my pipelines.
- Water the plants.

Here are some happy plants:

<img src="https://www.publicdomainpictures.net/pictures/80000/velka/succulent-roses-echeveria.jpg" alt="plants" width="300"/>
"""

@dag(dag_id="my_dag" ,
     schedule='@daily', 
     start_date=None, 
     catchup=False, 
     tags=['ercan'],
     doc_md=doc_md_DAG,
)
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