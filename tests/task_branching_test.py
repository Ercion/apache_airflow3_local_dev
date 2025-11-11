import pytest
from unittest.mock import MagicMock
from airflow.models import DagBag
import os
# Adjust the import to use absolute path from the root directory
#from dags import task_branching

# Fixture to load DAGs from the 'dags' folder
@pytest.fixture
def dagbag():
    """Fixture to load the DAG from the 'dags' directory."""
    #dagbag = DagBag(dag_folder='dags', include_examples=False)
    dags_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "dags")
    )
    dagbag = DagBag(dag_folder=dags_dir, include_examples=False)
    return dagbag
    #return dagbag  # Return the loaded dagbag object

# Test if the DAG is loaded correctly
def test_dag_loading(dagbag):
    """Test that the DAG is loaded correctly."""
    # Get the DAG by its ID (task_branching is the DAG ID from the example)
    assert len(dagbag.import_errors) == 0
    dag = dagbag.dags['task_branching']
    
    # Assert that the DAG is loaded and its ID matches the expected value
    assert dag is not None
    assert dag.dag_id == 'task_branching'

# Test the start_task logic (call the underlying function directly)
def test_task_logic(dagbag):
    """Test the start_task logic."""
    dag = dagbag.dags['task_branching']
    
    # Get the underlying function of the start_task task
    start_task_func = dag.get_task('start_task').python_callable
    
    # Call the function directly, which should return 7
    result = start_task_func()  # The start_task function should return 7
    assert result == 7

# Test the branching logic
def test_branching_logic(dagbag):
    """Test the branching logic by calling the underlying function."""
    dag = dagbag.dags['task_branching']
    check_condition_task = dag.get_task("check_condition")

    # Access the original Python function behind the @task.branch decorator
    branch_func = check_condition_task.python_callable

    # Call the underlying Python function directly
    result_true = branch_func(7)
    result_false = branch_func(3)

    assert result_true == "true_one"
    assert result_false == "false_one"
